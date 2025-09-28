pkgname = "cosmic-panel"
pkgver = "0.1.1"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "libxkbcommon-devel",
    "pkgconf",
]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-panel"
source = f"{url}/archive/refs/tags/epoch-1.0.0-beta.1.1.tar.gz"
sha256 = "7ca7fda8f45f0dd49f1b7afb76c7e62f0a414bbfac096ecc2de1b71650dea7b0"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-panel")
    self.install_files("data/default_schema", "usr/share/cosmic")
