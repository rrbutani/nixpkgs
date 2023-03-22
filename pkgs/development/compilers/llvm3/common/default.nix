# For specific llvm package sets (i.e. `llvmPackages_15`) to specify:
{ officialRelease ? null
, gitRelease ? null
, monorepoSrc ? null
} @ defaults:

# This is what `callPackage` should see (and thus what users should be able to
# `.override`):
{ stdenv, lib, pkgs, lowPrio, newScope, fetchFromGitHub
, gccForLibs, overrideCC, wrapCCWith, wrapBintoolsWith

# This is a partial list of the dependencies used in the `llvmPackages` set;
# individual packages can still get at other dependencies via the `callPackage`
# we use from `newScope`.
#
# The idea is to hoist packages that it might be desirable to override across
# the entire package set (i.e. deps used in multiple places) up to this list.
, cmake, ninja, libxml2, python3, darwin

# "Tying the knot" for cross-compilation:
, buildLlvmTools # tools, but from the previous stage, for cross
, targetLlvmLibraries # libraries, but from the next stage, for cross
, targetLlvm # LLVM, but from the next stage, for cross
, preLibcCrossHeaders # some platforms need headers for building `compiler-rt`

# This is the default binutils, but with *this* version of LLD rather than the
# default LLVM version's, if LLD is the choice. We use these for the `useLLVM`
# bootstrapping below. # TODO: commit with: https://github.com/NixOS/nixpkgs/commit/18c38f8aee732b6202042383fc35997a39361830#diff-2417d11feadd08f3fd71bce64e7094ebafab593fbca96f2a04e412ef3777616e
, bootBintoolsNoLibc ?
    if stdenv.targetPlatform.linker == "lld"
    then null
    else pkgs.bintoolsNoLibc
, bootBintools ?
    if stdenv.targetPlatform.linker == "lld"
    then null
    else pkgs.bintools

# LLVM release information; specify one of these but not both:
, gitRelease ? defaults.gitRelease or null
  # i.e.:
  # {
  #   version = /* i.e. "15.0.0" */;
  #   rev = /* commit SHA */;
  #   rev-version = /* human readable version; i.e. "unstable-2022-07-26" */;
  #   hash = /* checksum for this release, can omit if specifying your own `monorepoSrc` */;
  # }
, officialRelease ? defaults.officialRelease or null
  # i.e.:
  # {
  #   version = /* i.e. "15.0.0" */;
  #   candidate = /* optional; if specified, should be: "rcN" */
  #   hash = /* checksum for this release, can omit if specifying your own `monorepoSrc` */;
  # }
# By default, we'll try to fetch a release from `github:llvm/llvm-project`
# corresponding to the `gitRelease` or `officialRelease` specified.
#
# You can provide your own LLVM source by specifying this arg but then you'll
# need to make sure that the LLVM repo given matches the release configuration
# specified (we attempt to check this during the LLVM package's build, too).
, monorepoSrc ? defaults.monorepoSrc or null
}: let
  originalMonorepoSrc = monorepoSrc;
in let
  releaseInfo = import ./utils/process-release-options.nix {
    inherit lib fetchFromGitHub;
    inherit gitRelease officialRelease;
    monorepoSrc = originalMonorepoSrc;
  };
  inherit (releaseInfo) monorepoSrc release_version version;

  llvm_meta = with lib; {
    # TODO: link to PR/comment/LLVM blog posts.
    license     = licenses.ncsa;
    maintainers = teams.llvm.members;

    # See `llvm/cmake/config-ix.cmake`.
    platforms   = with platforms;
      aarch64 ++ arm ++ m68k ++ mips ++ power ++ riscv ++ s390x ++ wasi ++ x86;
  };

  inherit (import ./utils/versioned.nix { inherit lib release_version; })
    llvmIs llvmOlderThan llvmUpTo llvmNewerThan llvmAtLeast llvmRange
    select selectOrThrow
    major
  ;

  # TODO: revise this comment to be more coherent or just remove.
  # Note: the `tools` vs `libraries` distinction is really more about
  # cross-compilation than about binaries vs libraries.
  #
  # `tools` (mostly) contains packages whose _target_ matches the platform we're
  # using LLVM to generate code for but whose _host_ is independent. For
  # example, a `clang` binary that produces code for aarch64 (target) needn't
  # itself run on aarch64 (host).
  #
  # `libraries` contains packages whose _host_ platform matches the platform
  # we're targeting. For example, `compiler-rt` needs to be compiled for the
  # platform we're targetting. This is why the `stdenv`s fall under `libraries`
  # instead of tools.

  ##############################################################################
  tools = lib.makeExtensible (tools: let
    callPackage = newScope (tools // {
      inherit stdenv lib cmake ninja libxml2 python3
        llvm_meta release_version version monorepoSrc buildLlvmTools;
    });
  in
    # Packages:
    {
      # TODO: should we not specify the lib output here?
      # see: https://github.com/NixOS/nixpkgs/commit/6b3b7940ff3050aefc343dd0e855b5a7dc79f6d4
      # https://github.com/NixOS/nixpkgs/pull/218551
      # (commit)

      # TODO: do we need `pkgs.python3` for these? (commit)

      # Note: LLVM is under the `tools` attrset because it, in addition to
      # providing `libllvm`, provides the binaries.
      llvm = callPackage ./llvm {}; # TODO: set mainProgram... (commit)
      libllvm = tools.llvm.lib;
      llvm-manpages = lowPrio (tools.llvm.override { enableManpages = true; });

      clang-unwrapped = callPackage ./clang {};
      libclang = tools.clang-unwrapped.lib;
      clang-manpages = lowPrio (tools.clang-unwrapped.override {
        enableManpages = true;
      });

      lld = callPackage ./lld {}; # TODO: manpages...

      lldb = callPackage ./lldb {};
      lldb-manpages = lowPrio (tools.lldb.override { enableManpages = true; });
      # TODO: python bindings? lua bindings?

      bintools-unwrapped = callPackage ./bintools {};
      bintoolsNoLibc = wrapBintoolsWith {
        bintools = tools.bintools-unwrapped;
        # See `all-packages.nix` for details; some platforms need *some* headers
        # to be present (in lieu of a full libc) in order for `compiler-rt` to
        # build.
        libc = preLibcCrossHeaders;
      };
      bintools = wrapBintoolsWith {
        bintools = tools.bintools-unwrapped;
      };
    }

    # Wrapped `bintools` and `clang`s:
    // (let
      # Extra commands to run when constructing a `cc-wrapper` wrapping clang:
      mkExtraCcWrapperBuildCommands = cc: { includeCompilerRt ? false }: let
        # Changed in LLVM 16: https://reviews.llvm.org/D125860
        resourceDir = selectOrThrow [
          (llvmOlderThan 16 "${cc.lib}/lib/clang/${release_version}/include")
          (llvmAtLeast   16 "${cc.lib}/lib/clang/${major}/include")
        ];
      in ''
        rsrc="$out/resource-root"
        mkdir "$rsrc"
        ln -s "${resourceDir}" "$rsrc"
        echo "-resource-dir=$rsrc" >> $out/nix-support/cc-cflags;
      '' + lib.optionalString includeCompilerRt ''
        ln -s "${targetLlvmLibraries.compiler-rt.out}/lib" "$rsrc/lib"
        ln -s "${targetLlvmLibraries.compiler-rt.out}/share" "$rsrc/share"
      '';

      # See the top of this file; here we select an appropriate bintools
      # depending on whether the stdenv uses `lld`.
      bintoolsNoLibc =
        # `bootBintoolsNoLibc` is set to `null` if the stdenv uses `lld`
        if bootBintoolsNoLibc == null
        # the stdenv's `lld` may be coming from our wrapped `cc` so: use our
        # `bintools` directly to avoid potential cycles
        then tools.bintoolsNoLibc
        else bootBintoolsNoLibc;
      bintools =
        # Same as above but *with* libc.
        if bootBintools == null
        then tools.bintools
        else bootBintools;

      wrapClang =
        { includeCompilerRt ? false
        , useCompilerRtForCompilerBuiltins ? includeCompilerRt # in lieu of `lgcc_s`?
        , includeLibc ? false
        , cxxStdlib ? "none" # "none", "libstdc++", "libc++"
        , extraPackages ? []
        , extraCflags ? []
        }: let
          cxxStdlibMap = {
            none = {
              libcxx = null;
              # Note: `gccForLibs` gets used for `libgcc_s` too so we cannot set
              # this to `null` here despite us instructing `cc-wrapper` not to
              # use `gccForLibs` to pull in `libstdc++`.
              inherit gccForLibs;
              useCcForLibs = false;
            };
            "libstdc++" = { # TODO: what about non-linux? it's gated in cc-wrapper but still..
              libcxx = null;
              # `cc-wrapper` pulls libstdc++ from `gccForLibs`
              inherit gccForLibs;
              useCcForLibs = true;
            };
            "libc++" = {
              libcxx = targetLlvmLibraries.libcxx;
              gccForLibs = null; # TODO: verify..
              useCcForLibs = false;
            };
          };
        in
          assert useCompilerRtForCompilerBuiltins -> includeCompilerRt;
          assert cxxStdlibMap ? ${cxxStdlib};
          assert (cxxStdlib != "none") -> includeLibc;
        wrapCCWith rec {
          cc = tools.clang-unwrapped;
          inherit (cxxStdlibMap.${cxxStdlib}) libcxx gccForLibs useCcForLibs;
          bintools = if !includeLibc then bintoolsNoLibc else bintools;
          extraPackages = [] # these are `depsTargetTargetPropagated`
            ++ lib.optional includeCompilerRt targetLlvmLibraries.compiler-rt
            ++ lib.optional (cxxStdlib == "libc++") libcxx.cxxabi
            ++ extraPackages
          ;
          extraBuildCommands = mkExtraCcWrapperBuildCommands cc {
            inherit includeCompilerRt;
          };
          nixSupport.cc-cflags = []
            ++ lib.optionals useCompilerRtForCompilerBuiltins [
              "-rtlib=compiler-rt"

              # TODO: is this actually necessary? seems like we don't need this
              # *and* the symlink into the resource dir... this alone seems
              # preferable if that works.
              # https://github.com/NixOS/nixpkgs/pull/110251
              "-B${targetLlvmLibraries.compiler-rt}/lib"
            ]
            ++ lib.optional (!includeLibc) "-nostartfiles"
            ++ lib.optionals (cxxStdlib == "none") (
              # https://reviews.llvm.org/D35780
              # https://github.com/llvm/llvm-project/commit/0ee47d92b20019bed49841f93df1b5e4635061fc
              llvmAtLeast 6 [ "-nostdlib++" ]
            )
          ;
        };
    in {

      # TODO: update/source this comment (commit) or remove
      # Below, is the LLVM bootstrapping logic. It handles building a fully LLVM
      # toolchain from scratch. No GCC toolchain should be pulled in. As a
      # consequence, it is very quick to build different targets provided by
      # LLVM and we can also build for what GCC doesn’t support like LLVM.
      # Probably we should move to some other file.

      # Below are various wrappings of `clang` from this package set, working
      # our way up to a `clang` that has `compiler-rt`, `libc`, and a C++
      # stdlib.

      # TODO: add columns for bintools, compiler builtins (rename from
      # compiler-rt), libunwind (?)

      # Used to build `compiler-rt` (for most platforms) and for `stdenvNoLibs`
      # (see `all-packages.nix`).
      #
      # compiler-rt: ❌, libc: ❌, C++ stdlib: ❌
      clangNoCompilerRtNoLibc = wrapClang { };
      /* clangNoCompilerRtNoLibc = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = null;
        bintools = bintoolsNoLibc;
        extraPackages = [ ];
        extraBuildCommands = mkExtraCcWrapperBuildCommands cc {};
        nixSupport.cc-cflags = [ "-nostartfiles" ];
      }; */

      # Used to build `compiler-rt` on _some_ platforms (Android) and used to
      # build `libcxxabi`.
      #
      # (on macOS libcxxabi is a dep of compiler-rt so we need to use a compiler
      # *without* compiler-rt to build libcxxabi; see the note below)
      #
      # compiler-rt: ❌, libc: ✅, C++ stdlib: ❌
      clangNoCompilerRtWithLibc = wrapClang {
        includeLibc = true;
      };
      /* clangNoCompilerRtWithLibc = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = null;
        bintools = bintools;
        extraPackages = [ ];
        extraBuildCommands = mkExtraCcWrapperBuildCommands cc {};
      }; */

      #
      # compiler-rt: ✅, libc: ❌, C++ stdlib: ❌
      clangNoLibc = wrapClang {
        includeCompilerRt = true;
      };
      /* clangNoLibc = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = null;
        bintools = bintoolsNoLibc;
        extraPackages = [
          targetLlvmLibraries.compiler-rt
        ];
        extraBuildCommands = mkExtraCcWrapperBuildCommands cc {
          includeCompilerRt = true;
        };
        nixSupport.cc-cflags = [
          "-rtlib=compiler-rt"
          "-B${targetLlvmLibraries.compiler-rt}/lib"
        ];
      }; */

      #
      # compiler-rt: ✅, libc: ✅, C++ stdlib: ❌
      clangNoLibcxx = wrapClang {
        includeCompilerRt = true;
        includeLibc = true;
      };
      /* clangNoLibcxx = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = null;
        bintools = bintools';
        extraPackages = [
          targetLlvmLibraries.compiler-rt
        ];
        extraBuildCommands = mkExtraBuildCommands cc;
        nixSupport.cc-cflags = [
          "-rtlib=compiler-rt"
          "-B${targetLlvmLibraries.compiler-rt}/lib"
        ] ++ llvmAtLeast 6 [
          # https://reviews.llvm.org/D35780
          # https://github.com/llvm/llvm-project/commit/0ee47d92b20019bed49841f93df1b5e4635061fc
          "-nostdlib++"
        ];
      }; */

      #
      # compiler-rt: ✅, libc: ✅, C++ stdlib: libc++

      # TODO: should we also use LLVM bintools here, unconditionally? (commit)
      clangUseLLVM = wrapClang {
        includeCompilerRt = true;
        includeLibc = true;
        cxxStdlib = "libc++";
        extraPackages = lib.optionals (!stdenv.targetPlatform.isWasm) [
          targetLlvmLibraries.libunwind  # TODO: why does this condition not match the below (i.e. `useLLVM`)?
        ];
        extraCflags = [ "-Wno-unused-command-line-argument" ] # TODO: can this apply to other places?
          ++ lib.optional (!stdenv.targetPlatform.isWasm) "--unwindlib=libunwind"
          ++ lib.optional
            (!stdenv.targetPlatform.isWasm && stdenv.targetPlatform.useLLVM or false)
            "-lunwind"
          ++ lib.optional stdenv.targetPlatform.isWasm "-fno-exceptions";
      };

      /* clangUseLLVM = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = targetLlvmLibraries.libcxx;
        bintools = bintools';
        extraPackages = [
          libcxx.cxxabi
          targetLlvmLibraries.compiler-rt
        ] ++ lib.optionals (!stdenv.targetPlatform.isWasm) [
          targetLlvmLibraries.libunwind
        ];
        extraBuildCommands = mkExtraBuildCommands cc;
        nixSupport.cc-cflags =
          [ "-rtlib=compiler-rt"
            "-Wno-unused-command-line-argument"
            "-B${targetLlvmLibraries.compiler-rt}/lib"
          ]
          ++ lib.optional (!stdenv.targetPlatform.isWasm) "--unwindlib=libunwind"
          ++ lib.optional
            (!stdenv.targetPlatform.isWasm && stdenv.targetPlatform.useLLVM or false)
            "-lunwind"
          ++ lib.optional stdenv.targetPlatform.isWasm "-fno-exceptions";
      }; */

      # Pick clang appropriate for package set we are targeting (match
      # bintools/C++ stdlib implementation):
      clang =
        /**/ if stdenv.targetPlatform.useLLVM or false then tools.clangUseLLVM
        else if (pkgs.targetPackages.stdenv or stdenv).cc.isGNU then tools.libstdcxxClang
        else tools.libcxxClang;

      # compiler-rt: ✅, libc: ✅, C++ stdlib: stdlibc++
      libstdcxxClang = wrapClang {
        includeCompilerRt = true;
        useCompilerRtForCompilerBuiltins = false;
        includeLibc = true;
        cxxStdlib = "libstdc++";
      };
      /* libstdcxxClang = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        # libstdcxx is taken from gcc in an ad-hoc way in cc-wrapper.
        libcxx = null;
        extraPackages = [
          targetLlvmLibraries.compiler-rt
        ];
        extraBuildCommands = mkExtraCcWrapperBuildCommands cc {

        };
      }; */
      # Note: does *not* include the compiler-rt flag (but still puts it in
      # extra packages and still adds the extra build command for it's symlnk...
      # why?). TODO
      #
      # I think we may actually want to exclude `-rtlib` for these two so that
      # we don't use `rtlib` in lieu of gcc_s (but still use `rtlib` for the
      # sanitizer runtimes); not sure how the `-B` flag factors into that (or
      # if it's even necessary)

      # TODO: we should gate this on `isLinux`? or rename to `systemClang` or
      # platformClang or something?

      # Note: unlike these two we set `bintools` explicitly but I think it's
      # fine?
      #
      # It'd only be different in cases where `useLLVM` is true? in which case
      # we'd use our own bintools instead of the package set's (LLVM)
      # pkgs.bintools. TODO

      # compiler-rt: ✅, libc: ✅, C++ stdlib: libc++ (but still libgcc_s?)
      libcxxClang = wrapClang {
        includeCompilerRt = true;
        useCompilerRtForCompilerBuiltins = false;
        includeLibc = true;
        cxxStdlib = "libc++";
      };

      /* libcxxClang = wrapCCWith rec {
        cc = tools.clang-unwrapped;
        libcxx = targetLlvmLibraries.libcxx;
        extraPackages = [
          libcxx.cxxabi
          targetLlvmLibraries.compiler-rt
        ];
        extraBuildCommands = mkExtraBuildCommands cc;
      }; */
    })
  );

  ##############################################################################
  libraries = lib.makeExtensible (libraries: let
    callPackage = newScope (libraries // buildLlvmTools // {
      inherit stdenv lib cmake ninja libxml2 python3
        llvm_meta release_version version monorepoSrc targetLlvm;
    });
  in {
    # TODO: commit: make `compiler-rt`/`compiler-rt-no-libc` an internal detail.

    # TODO: add android cross-comp to the test matrix.
    compiler-rt = callPackage ./compiler-rt {
      # If we're building `compiler-rt` for a `useLLVM` platform, use clang from
      # `buildLlvmTools` as the compiler (instead of the compiler in `stdenv`):
      stdenv = let
        # Some platforms need libc to build `compiler-rt`:
        clangCcWrapper = with buildLlvmTools; if stdenv.hostPlatform.isAndroid
          then clangNoCompilerRtWithLibc # TODO: explain; does Android still even need libc to build its `compiler-rt`? why?
          else clangNoCompilerRtNoLibc;
      in if stdenv.hostPlatform.useLLVM or false
        then overrideCC stdenv clangCcWrapper
        else stdenv;
    };

    libcxxabi = let
      # CMake "require"s a working C++ compiler though `cxx-header`'s does not
      # actually use one; it doesn't matter what stdenv we use here, as long
      # as CMake is happy.
      cxx-headers = callPackage ./libcxx {
        # Using the regular stdenv here yields cycle errors when attempting to
        # use this package set's clang in a stdenv.
        #
        # In this scenario, the final stdenv pulls `cxx-headers` from the
        # package set where hostPlatform *is* the target platform which means
        # that `stdenv` at that point attempts to use this toolchain.
        #
        # So, we use `stdenv_` (the stdenv containing `clang` from this package
        # set, defined below) to sidestep this issue.
        stdenv = stdenv_;
        headersOnly = true;
      };

      # `libcxxabi` *doesn't* need a compiler with a working C++ stdlib but it
      # *does* need a relatively modern C++ compiler (see:
      # https://releases.llvm.org/15.0.0/projects/libcxx/docs/index.html#platform-and-compiler-support).
      #
      # So, we use the clang from this LLVM package set, like libc++
      # "boostrapping builds" do:
      # https://releases.llvm.org/15.0.0/projects/libcxx/docs/BuildingLibcxx.html#bootstrapping-build
      #
      # We cannot use `clangNoLibcxx` because that contains `compiler-rt` which,
      # on macOS, depends on `libcxxabi`, thus forming a cycle.
      #
      # We cannot use `clangNoCompilerRtNoLibc` because we need `libc` to build
      # `libcxxabi`.
      stdenv_ = overrideCC stdenv buildLlvmTools.clangNoCompilerRtWithLibc;
    in callPackage ./libcxxabi {
      stdenv = stdenv_;
      inherit cxx-headers;
    };

    # Like `libcxxabi` above, `libcxx` requires a fairly modern C++ compiler,
    # so: we use the clang from this LLVM package set instead of the regular
    # stdenv's compiler.
    libcxx = callPackage ./libcxx {
      stdenv = overrideCC stdenv buildLlvmTools.clangNoLibcxx;
    };

    # Likewise for `libunwind`.
    libunwind = callPackage ./libunwind {
      stdenv = overrideCC stdenv buildLlvmTools.clangNoLibcxx;
    };

    openmp = callPackage ./openmp {};

    # `stdenv`s:
    stdenv = overrideCC stdenv buildLlvmTools.clang; # same bintools, libc, C++ stdlib, compiler builtins, libunwind as the host
    libcxxStdenv = overrideCC stdenv buildLlvmTools.libcxxStdenv;
  });

  ##############################################################################
# Note: the `tools` and `libraries` sets actually do not reference each other
# directly (only via `buildLlvmTools`, `targetLlvmLibraries`, etc.) so the
# `makeExtensible` here isn't _really_ necessary but we use it anyways to make
# overriding packages within the set a little more convenient for users.
in lib.makeExtensible (llvmPackageSet:
  { inherit tools libraries monorepoSrc release_version; } # TODO: is it okay to include monorepoSrc here?
  # // llvmPackageSet.tools
  # // llvmPackageSet.libraries
)
