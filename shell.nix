# shell.nix

{ pkgs ? import <nixpkgs> {} }:
let
  requirements = ps: with ps; [
    click
    Flask
    numpy
    Pillow
    requests
    tomli
  ];
  my-python = pkgs.python310.withPackages requirements;
in my-python.env
