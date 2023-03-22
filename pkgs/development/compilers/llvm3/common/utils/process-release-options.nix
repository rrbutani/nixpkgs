# See `../default.nix` for more info about these args.
{ lib, fetchFromGitHub
  # { version = ...; rev = ...; rev-version = ...; hash = ...; }
, gitRelease
  # { version = ...; candidate = ...; hash = ...; }
, officialRelease
, monorepoSrc
} @ args: let

# Check that `gitRelease` OR `officialRelease` are specified:
  int = a: if a then 1 else 0;
  xor = a: b: ((builtins.bitXor (int a) (int b)) == 1);
  src = if gitRelease != null then gitRelease else officialRelease;
in assert
  (xor
    (gitRelease != null)
    (officialRelease != null))
  ("must specify `gitRelease` or `officialRelease`" +
    (lib.optionalString (gitRelease != null) " — not both"));

# Compute `release_version`, `version`, and `monorepoSrc`:
rec {
  # version triple; i.e. `15.0.7`
  #
  # this is the same for git sources and official releases:
  release_version = src.version;

  # human readable version; i.e. `unstable-2022-07-26`, `15.0.0-rc3`
  #
  # for git sources this is given to us directly; for official releases this is
  # computed by tacking on the release candidate number (if present)
  #
  # Note: we need to draw a distinction between `release` and `release_version`
  # because release version ends up getting used in paths (like the clang
  # sysroot path) that the LLVM build generates.
  version = if gitRelease != null then
    gitRelease.rev-version
  else if officialRelease ? candidate then
    "${release_version}-${officialRelease.candidate}"
  else
    release_version;

  # if we weren't given a monorepo source, pull from the LLVM github:
  monorepoSrc = if args.monorepoSrc != null then args.monorepoSrc else
    fetchFromGitHub {
      inherit (src) hash;
      rev = if gitRelease != null then gitRelease.rev else
        # See here for tag names: https://github.com/llvm/llvm-project/tags
        #
        # Note that `version` includes `-rcN` in cases where a release candidate
        # number was given to us.
        "llvmorg-${version}"
      ;
      owner = "llvm";
      repo = "llvm-project";
    };
}
