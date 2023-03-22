let
  np = import ../../../.. {};
  lib = np.lib;
  llvms = lib.pipe 17 [
    (builtins.genList lib.id)
    (builtins.filter (x: x >= 5))
    (x: x ++ ["git"])
    (builtins.map (x: "llvmPackages2_${builtins.toString x}"))
    (builtins.map (x: builtins.trace x x))
    (builtins.map (x: np.${x}))
  ];
  srcs = np.writeTextFile {
    name = "llvm-srcs";
    text = lib.pipe llvms [
      (builtins.map (x: x.monorepoSrc.outPath))
      builtins.toString
    ];
  };
in srcs
