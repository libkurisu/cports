pkgname = "cosmic-bg"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "libxkbcommon-devel",
    "pkgconf",
]
pkgdesc = "COSMIC session service which applies backgrounds to displays"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-bg"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "9a514472379412635a1d75325c9bb03313ed170634b841c75a65f73de62d0b1d"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-bg")
    self.install_file("data/com.system76.CosmicBackground.desktop", "usr/share")
    self.install_file(
        "data/com.system76.CosmicBackground.metainfo.xml", "usr/share/metainfo"
    )
    self.install_files("data/icons", "usr/share/icons/hicolor/symbolic/apps")
    self.install_files("data/v1", "usr/share/cosmic")
