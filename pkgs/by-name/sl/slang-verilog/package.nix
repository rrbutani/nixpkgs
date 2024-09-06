{ lib
, stdenv
, fetchFromGitHub
, fetchpatch
, testers
, nix-update-script

# build deps:
, cmake
, ninja
, python3

# runtime deps:
, boost182
, catch2_3
, fmt
, mimalloc
, pythonPackages

# options
, doCheck ? includeTools
, includeTools ? true
, useMimalloc ? !enablePython
, enablePython ? false
, generatePythonBindingStubs ? enablePython
}:
  assert doCheck -> includeTools; # the regression tests need `slang::driver`
  assert enablePython -> !useMimalloc; # mimalloc is incompatible w/py bindings
  assert generatePythonBindingStubs -> enablePython;

stdenv.mkDerivation (finalAttrs: {
  pname = "slang-verilog"; # https://repology.org/project/slang-verilog
  version = "6.0";

  src = fetchFromGitHub {
    owner = "MikePopoloski";
    repo = "slang";
    rev = "v${finalAttrs.version}";
    sha256 = "sha256-mT8sfUz0H4jWM/SkV/uW4kmVKE9UQy6XieG65yJvIA8=";
  };

  outputs = [ "out" "lib" "dev" ]
    ++ lib.optional enablePython "python";

  # See: https://github.com/NixOS/nixpkgs/issues/144170
  # See: https://github.com/MikePopoloski/slang/blob/v6.0/scripts/sv-lang.pc.in#L2-L3
  # See: https://github.com/dtzWill/slang/commit/36138d6775be144968dd9d126ba4089277c14054
  #
  # slang's `includedir` and `libdir` in `sv-lang.pc` are hardcoded to be
  # `${prefix}`-relative paths; when using multiple outputs (i.e. `lib`, `dev`)
  # these directories do not share a prefix. So, we strip `${prefix}` from the
  # pkg-config template — `CMAKE_INSTALL_INCLUDEDIR` and `CMAKE_INSTALL_LIBDIR`
  # are (when set by the cmake setup hook) already absolute paths.
  patches = [
    (fetchpatch {
      url = "https://github.com/MikePopoloski/slang/commit/36138d6775be144968dd9d126ba4089277c14054.patch";
      hash = "sha256-U540bNyOonR0WJJlqudojDNSgldka4l85LTtZWDNZJk=";
    })
  ];

  # When building with `mimalloc`, slang includes `mimalloc-new-delete.h` which
  # (re)defines the C++ `new` and `delete` operators:
  #   - https://github.com/MikePopoloski/slang/blob/v6.0/source/util/Util.cpp#L12-L14
  #   - https://github.com/microsoft/mimalloc/blob/v2.1.7/include/mimalloc-new-delete.h#L8-L20
  #
  # Because our (nixpkgs') `mimalloc` is built with `-DMI_OVERRIDE=On` (the
  # default), `libmimalloc.a`'s `alloc.c.o` contains redefinitions of the `new`
  # and `delete` operators as well:
  #   - https://github.com/microsoft/mimalloc/blob/v2.1.7/CMakeLists.txt#L10
  #   - https://github.com/microsoft/mimalloc/blob/v2.1.7/CMakeLists.txt#L589-L591
  #   - https://github.com/microsoft/mimalloc/blob/v2.1.7/src/alloc.c#L20
  #   - https://github.com/microsoft/mimalloc/blob/v2.1.7/src/alloc-override.c#L152-L237
  #
  # This leads to duplicate symbol errors when linking `slang` binaries:
  # ```
  # slang> .../bin/ld: <mimalloc>/lib/libmimalloc.a(alloc.c.o): in function `mi_new':
  # slang> (.text+0x2c10): multiple definition of `operator new(unsigned long)'; <slang>/lib/libsvlang.a(Util.cpp.o):Util.cpp:(.text+0x40): first defined here
  # ```
  #
  # Also see:
  #   - https://github.com/microsoft/mimalloc/issues/535#issuecomment-1020553023
  #   - https://github.com/microsoft/mimalloc/issues/559#issuecomment-1916408486
  #
  # `slang` — when building `mimalloc` itself — sets `MI_OVERRIDE` to `OFF` to
  # avoid this issue:
  #   - https://github.com/MikePopoloski/slang/blob/v6.0/external/CMakeLists.txt#L78-L80
  #
  # To work around this we "inhibit" `mimalloc-new-delete.h` by manually
  # defining its preprocessor include guard symbol:
  env.NIX_CFLAGS_COMPILE = lib.optionalString
    finalAttrs.useMimalloc "-DMIMALLOC_NEW_DELETE_H=1";

  inherit includeTools useMimalloc enablePython generatePythonBindingStubs;
  cmakeFlags = [
    (lib.cmakeBool "SLANG_INCLUDE_TESTS" finalAttrs.doCheck)
    (lib.cmakeBool "SLANG_INCLUDE_TOOLS" finalAttrs.includeTools)
    (lib.cmakeBool "SLANG_USE_MIMALLOC" finalAttrs.useMimalloc)
    (lib.cmakeBool "SLANG_INCLUDE_PYLIB" finalAttrs.enablePython)
  ];

  nativeBuildInputs = [
    cmake
    ninja
    python3
  ] ++ lib.optional (
    finalAttrs.enablePython &&
    (stdenv.buildPlatform.canExecute stdenv.hostPlatform)
  ) pythonPackages.pythonImportsCheckHook;

  buildInputs = [
    boost182
    fmt
  ] ++ lib.optional finalAttrs.useMimalloc mimalloc
    ++ lib.optionals finalAttrs.enablePython [
      pythonPackages.python
      pythonPackages.pybind11
    ];

  nativeCheckInputs = [ catch2_3 ];
  inherit doCheck;

  pythonImportsCheck = lib.optional finalAttrs.enablePython [ "pyslang" ];

  postInstall = lib.optionalString (!finalAttrs.includeTools) ''
    mkdir -p $out/.empty
  '' + lib.optionalString (finalAttrs.enablePython) ''
    py_ver=${lib.versions.majorMinor pythonPackages.python.version}
    py_dir="$python/lib/python$py_ver/site-packages/"
    mkdir -p "$py_dir"
    mv $out/*.cpython* "$py_dir"
  ''
  # TODO: do this the right way (pybind11-stubgen + fixups?)
  + (lib.optionalString finalAttrs.generatePythonBindingStubs ''
    mkdir -p "$py_dir/pyslang/"
    cp ${./pyslang.pyi} "$py_dir/pyslang/__init__.pyi"
  '');

  passthru.tests = let
    withOpts = opts: finalAttrs.finalPackage.overrideAttrs (_: opts);
  in {
    # ensure that the options work:
    noTests = (withOpts { doCheck = false; }).tests.version;
    systemAllocator = (withOpts { useMimalloc = false; }).tests.version;
    noTools = withOpts { includeTools = false; doCheck = false; };
    small = withOpts {
      includeTools = false; doCheck = false; useMimalloc = false;
    };
  } // lib.optionalAttrs finalAttrs.includeTools {
    version = testers.testVersion { package = finalAttrs.finalPackage; };
  };

  passthru.updateScript = nix-update-script { };

  meta = with lib; {
    description = "SystemVerilog compiler and language services";
    longDescription = ''
      slang is a software library that provides various components for lexing,
      parsing, type checking, and elaborating SystemVerilog code. It comes with
      an executable tool that can compile and lint any SystemVerilog project,
      but it is also intended to be usable as a front end for synthesis tools,
      simulators, linters, code editors, and refactoring tools.
    '';
    homepage = "https://sv-lang.com/";
    changelog = "https://github.com/MikePopoloski/slang/releases/tag/v${finalAttrs.version}";
    license = licenses.mit;
    maintainers = with maintainers; [ sharzy rrbutani ];
    platforms = platforms.all;
  } // lib.optionalAttrs finalAttrs.includeTools {
    mainProgram = "slang";
  };
})
