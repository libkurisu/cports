pkgname = "cosmic-edit"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "git",
    "libxkbcommon-devel",
    "oniguruma-devel",
    "pkgconf",
    "zstd-devel",
]
pkgdesc = "COSMIC text editor"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-edit"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "e98b7a6bea4ace6f9d0ea24e96d190c45bca1cdf085086ebbea3fd665757086e"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-edit")
    self.install_file(
        "res/com.system76.CosmicEdit.desktop", "usr/share/applications"
    )
    self.install_file(
        "res/com.system76.CosmicEdit.metainfo.xml", "usr/share/metainfo"
    )
    self.install_files("res/icons", "usr/share")
