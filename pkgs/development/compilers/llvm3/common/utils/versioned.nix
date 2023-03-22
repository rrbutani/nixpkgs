{ lib, release_version }: let

  emptyValMap = {
    path = null;
    list = [];
    set = {};
    string = "";
  };
  emptyVals = builtins.attrValues emptyValMap;


  # Note: we do the typecheck upfront so that we don't have latent type errors that
  # are masked (for now) by `bool` being true.
  gated = bool: val: let
    ty = builtins.typeOf val;
    value = if builtins.elem val emptyVals then
      throw ''
        please don't use ${ty} empty value with `gated`; `select` cannot
        differentiate between values that _happen_ to be empty and predicates
        which don't match the current version
      ''
    else val;

    fallback = x: if bool then value else x;
    valueOrEmpty = lib.mapAttrs (_: fallback) emptyValMap;
  in valueOrEmpty.${ty} or throw "don't know how to gate a value of type ${ty}";

  # This trims `release_version` to match the fields specified in `ver`.
  #
  # i.e. `compareVersions 15` with `release_version = "15.0.7"` will return `0`
  # (exact match) while `compareVersions "15.0.0"` would return `1` (release
  # version is newer).
  compareVersions = ver: let
    rhs = builtins.toString ver; # so we can accept numbers (i.e. just major version)
    lhs = let
      parts = builtins.length (lib.splitVersion release_version);
    in lib.versions.pad parts release_version;
  in builtins.compareVersions lhs rhs;
in rec {

  major = lib.versions.major release_version;
  minor = lib.versions.minor release_version;
  patch = lib.versions.patch release_version;

  # rel == ver
  llvmIs = ver: gated ((compareVersions ver) == 0);

  # rel < max
  llvmOlderThan = max: gated ((compareVersions max) == -1);
  # rel <= max
  llvmUpTo = ver: gated ((compareVersions max) <= 0);
  # rel > min
  llvmNewerThan = min: gated ((compareVersions ver) == 1);
  # rel >= min
  llvmAtLeast = min: gated ((compareVersions min) >= 0);

  # a <= ... <= b
  llvmRange = lower: upper: val: lib.pipe val [
    (verAtLeast lower)
    (verUpTo upper)
  ];

  # Selects the first non-"empty" value (or throws).
  #
  # NOTE: does not check that the potential values are of the same type!
  #
  # For example:
  # ```nix
  # # See: https://releases.llvm.org/
  # selectOrThrow [
  #   (verIs "3.9" "2016: last release before 6-month release cycle")
  #   (verOlderThan 4 "before 2017")
  #   (verRange 4 "5.0.1" "2017")
  #   (verUpTo "7.0" "2018") # 5.0.2, 6, 7, 7.0.1
  #   (verUpTo 9 "2019") # 8.0, 7.1, 8.0.1, 9, 9.0.1
  #   (verUpTo "11.0.0" "2020") # 10, 10.0.1, 11
  #   (verUpTo "13.0.0" "2021") # 11.0.1, 11.1, 12, 12.0.1, 13
  #   (verUpTo "15.0.6" "2022")
  #   ("2023")
  # ]
  # ```
  #
  # Type: a (default) -> [a] -> a
  select = lib.findFirst (x: !(builtins.elem x emptyVals));

  selectOrThrow = list: select (throw ''
    Unable to find a matching predicate for LLVM version ${release_version}.
  '');
}
