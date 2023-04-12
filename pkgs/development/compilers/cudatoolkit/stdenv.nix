{ gccWithNixpkgsCompatibleLibstdcxx
, nvccCompatibleCC
, overrideCC
, stdenv
, wrapCCWith
, lib
}:

# We can safely use a _newer_ libstdc++ than is used in the package set's
# default stdenv:
assert
  # Only bother doing this check if the default stdenv is libstdc++ based:
  if (stdenv.cc.cxxStdlib.kind or null) == "stdlibc++"
    then lib.versionAtLeast
      gccWithNixpkgsCompatibleLibstdcxx.lib.version
      stdenv.cxxStdlib.lib
    else true;

let
  cc = wrapCCWith {
    cc = nvccCompatibleCC;

    # Note: normally the `useCcForLibs`/`gccForLibs` mechanism is used to get a
    # clang based `cc` to use `libstdc++` (from gcc).
    #
    # Here we (ab)use it to use a `libstdc++` from a _different_ `gcc` than our
    # `cc`.
    #
    # Note that this does not inhibit our `cc`'s lib dir from being added to
    # cflags/ldflags (see `cc_solib` in `cc-wrapper`) but this is okay: our
    # `gccForLibs`'s paths should take precedence.
    useCcForLibs = true;
    gccForLibs = gccWithNixpkgsCompatibleLibstdcxx;
  };
in overrideCC stdenv cc

