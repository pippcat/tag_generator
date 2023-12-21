# shell.nix

{ pkgs ? import <nixpkgs> {} }:
let
  requirements = ps: with ps; [
    click
    flask
    numpy
    pillow
    opencv4
    pyzbar
    requests
    tomli
  ];
  my-python = pkgs.python310.withPackages requirements;
in my-python.env
