{ lib
, stdenv
, fetchFromGitHub
, fetchpatch
, testers

# build deps:
, cmake
, ninja
, python3

# runtime deps:
, boost182
, catch2_3
, fmt

# options
, doCheck ? includeTools
, includeTools ? true
}:
  assert doCheck -> includeTools; # the regression tests need `slang::driver`

stdenv.mkDerivation (finalAttrs: {
  pname = "sv-lang";
  version = "6.0";

  src = fetchFromGitHub {
    owner = "MikePopoloski";
    repo = "slang";
    rev = "v${finalAttrs.version}";
    sha256 = "sha256-mT8sfUz0H4jWM/SkV/uW4kmVKE9UQy6XieG65yJvIA8=";
  };

  outputs = [ "out" "lib" "dev" ];

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

  inherit includeTools;
  cmakeFlags = [
    (lib.cmakeBool "SLANG_INCLUDE_TESTS" finalAttrs.doCheck)
    (lib.cmakeBool "SLANG_INCLUDE_TOOLS" finalAttrs.includeTools)
    (lib.cmakeBool "SLANG_USE_MIMALLOC" false)
  ];

  nativeBuildInputs = [
    cmake
    ninja
    python3
  ];

  buildInputs = [
    boost182
    fmt
  ];

  nativeCheckInputs = [ catch2_3 ];
  inherit doCheck;

  postInstall = lib.optionalString (!finalAttrs.includeTools) ''
    mkdir -p $out/.empty
  '';

  passthru.tests = let
    withOpts = opts: finalAttrs.finalPackage.overrideAttrs (_: opts);
  in {
    # ensure that the options work:
    noTests = (withOpts { doCheck = false; }).tests.version;
    noTools = withOpts { includeTools = false; doCheck = false; };
  } // lib.optionalAttrs finalAttrs.includeTools {
    version = testers.testVersion { package = finalAttrs.finalPackage; };
  };

  meta = with lib; {
    description = "SystemVerilog compiler and language services";
    homepage = "https://github.com/MikePopoloski/slang";
    license = licenses.mit;
    maintainers = with maintainers; [ sharzy ];
    platforms = platforms.all;
  } // lib.optionalAttrs finalAttrs.includeTools {
    mainProgram = "slang";
  };
})
