{ lib
, stdenv
, pkg-config
, fetchFromGitHub
, libusb1
, darwin
# For testing:
, testers
, lm4tools
# As per the README, `lmicdiusb` is not supported on Windows since it needs
# `poll`:
# https://github.com/utzig/lm4tools/blob/61a7d17b85e9b4b040fdaf84e02599d186f8b585/README.md#L15
, buildLmicdiusb ? !stdenv.targetPlatform.isWindows
}:

stdenv.mkDerivation rec {
  pname = "lm4tools";
  version = "0.1.3";
  src = fetchFromGitHub {
    owner = "utzig";
    repo = pname;
    rev = "v${version}";
    sha256 = "ZjuCH/XjQEgg6KHAvb95/BkAy+C2OdbtBb/i6K30+uo=";
  };

  patches = [
    # We don't want the Makefile to assume `libusb` lives in /usr/local/lib.
    ./macOS-use-pkg-config.patch
    # When cross compiling `pkg-config` may have a prefix; we want to get its
    # name/path from `$PKG_CONFIG`.
    ./use-pkg-config-env-var.patch
    # Build with `-O2`:
    ./use-release-config-for-build.patch
    # Have the `Makefile`s pass `pkg-config` the right flags when doing a
    # static build.
    #
    # See the comment on `configurePhase` below.
    ./pkg-config-static-build-support.patch
  ] ++ lib.optionals stdenv.targetPlatform.isWindows [
    # The minGW toolchain appends a `.exe` if it's not present which confuses
    # `install`.
    ./windows-file-ext.patch
  ] ++ lib.optionals (!buildLmicdiusb) [
    ./disable-lmicdiusb-build.patch
  ];
  makeFlags = [ "PREFIX=${placeholder "out"}" ];

  # We want to communicate to the `Makefile`s whether we are doing a static
  # build or not so that it can pass `--static` to `pkg-config` if we are.
  # If the `Makefile` does not do this, it will not include "private"
  # dependencies from `libusb1` (some macOS frameworks) and the build will
  # fail.
  #
  # There doesn't seem to be a canonical way to tell if the stdenv is
  # configured to make static binaries. The `makeStatic` stdenv adapters,
  # for example, do not set `stdenv.targetPlatform` and add different
  # flags for macOS/Linux/etc.
  # See: https://github.com/NixOS/nixpkgs/blob/0c4d65b21efd3ae2fcdec54492cbaa6542352eb9/pkgs/stdenv/adapters.nix#L56-L135
  #
  # So, we look for the `--disable-shared` configure flag as an indicator
  # that we're linking statically (even though the `makeStaticDarwin` adapter
  # in isolation does *not* add this configure flag):
  configurePhase = ''
    if [[ "$configureFlags" =~ "--enable-static" ]]; then
      makeFlagsArray+=(STATIC_BUILD=1)
    fi
  '';

  nativeBuildInputs = [ pkg-config ];
  buildInputs = [ libusb1 ] ++ lib.optionals stdenv.isDarwin
    (with darwin.apple_sdk.frameworks; [
      AppKit Carbon IOKit
    ]);

  # `lmicdiusb` has no help text so we don't check that it can run.
  doCheck = true;
  passthru.tests = {
    lm4flash = testers.testVersion {
      package = lm4tools;
      command = "${lm4tools.meta.mainProgram} -V";
    };
  };

  meta = with lib; rec {
    longDescription = ''
      Tools to enable multi-platform development on the TI Stellaris
      Launchpad boards (lm4f) and TI Tiva C boards (tm4c).

      Includes `lm4flash` and `lmicdiusb`.
    '';
    description  = "Tools for TI Stellaris boards";
    homepage     = "https://github.com/utzig/lm4tools";
    downloadPage = "https://github.com/utzig/lm4tools/releases/tag/v${version}";
    changelog    = downloadPage;
    license      = with licenses; [ gpl2Plus bsd3 ];
    maintainers  = with lib.maintainers; [ rrbutani ];
    mainProgram  = "lm4flash";
    platforms    = with lib.platforms; unix ++ windows;
  };
}
