final: prev: let
  ### Cuda Toolkit

  # Function to build the class cudatoolkit package
  buildCudaToolkitPackage = final.callPackage ./common.nix;

  # Version info for the classic cudatoolkit packages that contain everything that is in redist.
  cudatoolkitVersions = final.lib.importTOML ./versions.toml;

  finalVersion = cudatoolkitVersions.${final.cudaVersion};

  # Exposed as cudaPackages.backendStdenv.
  # This is what nvcc uses as a backend,
  # and it has to be an officially supported one (e.g. gcc11 for cuda11).
  #
  # It, however, propagates current stdenv's libstdc++ to avoid "GLIBCXX_* not found errors"
  # when linked with other C++ libraries.
  # E.g. for cudaPackages_11_8 we use gcc11 with gcc12's libstdc++
  # Cf. https://github.com/NixOS/nixpkgs/pull/218265 for context
  backendStdenv = final.callPackage ./stdenv.nix {
    gccWithNixpkgsCompatibleLibstdcxx = final.pkgs.buildPackages.gcc12.cc;
    nvccCompatibleCC = final.pkgs.buildPackages."${finalVersion.gcc}".cc;
  };
  # Should be final (unless you're concerned about cycles?)
  # Shouldn't be buildPackages or targetPackages?
  # `libcxx` doesn't work how you think it does; see comments; it does add it to propagatedBuildInputs but other than that it gets ignored
  # `passthru` should be used in an override here but I don't think it's necessary anymore
  # why is this (in jax) necessary?

  ### Add classic cudatoolkit package
  cudatoolkit =
    let
      attrs = builtins.removeAttrs finalVersion [ "gcc" ];
      attrs' = attrs // { inherit backendStdenv; };
    in
    buildCudaToolkitPackage attrs';

  cudaFlags = final.callPackage ./flags.nix {};

in
{
  inherit
    backendStdenv
    cudatoolkit
    cudaFlags;
}
