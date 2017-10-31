with import <nixpkgs> {};

let
  python = pkgs.python36;
in (python.withPackages (ps: [])).env
