{
  description = "Python matplotlib flake";

  inputs = {
    nixpkgs.url = "github:NixOS/nixpkgs?ref=nixpkgs-unstable";
  };

  outputs = { self, nixpkgs, flake-utils }: let
    pkgs = nixpkgs.legacyPackages.x86_64-linux;

    pythonDeps = with pkgs; [
      (python.withPackages (ps: with ps; [
        matplotlib
      ]))
    ];

    python = pkgs.python312;
  in {
    devShells.x86_64-linux = {
      default = pkgs.mkShell {
        buildInputs = [ pythonDeps ];
        shellHook = "$SHELL";
      };
    };
  };
}