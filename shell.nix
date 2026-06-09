let pkgs = import <nixpkgs> { };
in
let
	packageOverrides = pkgs.callPackage ./python-packages.nix { };
	python = pkgs.python3.override { inherit packageOverrides; };
	pythonWithPackages = python.withPackages (ps: [
		ps.asn1crypto
		ps.axmlparserpy
		ps.certifi
		ps.pycparser
		ps.pycryptodomex
		# ps.pyinstaller
		ps.pyusb
		ps.pyyaml
		ps.tlslite-ng
	] ++ pkgs.lib.optionals pkgs.stdenv.hostPlatform.isLinux [
		ps.libusb
		ps.libusb1
	] ++ pkgs.lib.optionals pkgs.stdenv.hostPlatform.isWindows [
		ps.comtypes
		ps.pywin32
	]);
in
pkgs.mkShell {
  nativeBuildInputs = [ pythonWithPackages ];
	LD_LIBRARY_PATH = pkgs.lib.makeLibraryPath ([
	] ++ pkgs.lib.optionals pkgs.stdenv.hostPlatform.isLinux [
		pkgs.libusb1
	] ++ pkgs.lib.optionals pkgs.stdenv.hostPlatform.isDarwin [
	] ++ pkgs.lib.optionals pkgs.stdenv.hostPlatform.isWindows [
	]);
}
