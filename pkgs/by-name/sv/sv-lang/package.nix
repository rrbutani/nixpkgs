{ lib
, stdenv
, fetchFromGitHub
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
, doCheck ? true
}: stdenv.mkDerivation (finalAttrs: {
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
  #
  # slang's `includedir` and `libdir` in `sv-lang.pc` are hardcoded to be
  # `${prefix}`-relative paths; when using multiple outputs (i.e. `lib`, `dev`)
  # these directories do not share a prefix. So, we strip `${prefix}` from the
  # pkg-config template — `CMAKE_INSTALL_INCLUDEDIR` and `CMAKE_INSTALL_LIBDIR`
  # are (when set by the cmake setup hook) already absolute paths.
  patchPhase = ''
    runHook prePatch

    substituteInPlace ./scripts/sv-lang.pc.in \
      --replace-fail \
        "\''${prefix}/@CMAKE_INSTALL_INCLUDEDIR@" '@CMAKE_INSTALL_INCLUDEDIR@' \
      --replace-fail \
        "\''${prefix}/@CMAKE_INSTALL_LIBDIR@" '@CMAKE_INSTALL_LIBDIR@'

    runHook postPatch
  '';

  cmakeFlags = [
    (lib.cmakeBool "SLANG_INCLUDE_TESTS" finalAttrs.doCheck)
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

  passthru.tests = {
    version = testers.testVersion { package = finalAttrs.finalPackage; };
  };

  meta = with lib; {
    description = "SystemVerilog compiler and language services";
    homepage = "https://github.com/MikePopoloski/slang";
    license = licenses.mit;
    maintainers = with maintainers; [ sharzy ];
    mainProgram = "slang";
    platforms = platforms.all;
  };
})
