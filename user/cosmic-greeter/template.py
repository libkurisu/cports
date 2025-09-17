pkgname = "cosmic-greeter"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cargo"
make_build_args = [
    "--no-default-features",
]
hostmakedepends = [
    "cargo-auditable",
    "clang-devel",
    "git",
    "libxkbcommon-devel",
    "linux-pam-devel",
    "pkgconf",
    "udev-devel",
]
pkgdesc = "Libcosmic greeter for greetd"
license = "GPL-3.0-or-later"
url = "https://github.com/pop-os/cosmic-greeter"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "dfb1ce08f0fb4c1047f1a3e011e8428bfe45b150dbaf848e1f29abee183a2c4d"

#TODO: FIX "not withen suitable git worktree" error

def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-greeter")
    # self.install_file("data/com.system76.CosmicBackground.desktop", "usr/share")
    # self.install_file(
    #     "data/com.system76.CosmicBackground.metainfo.xml", "usr/share/metainfo"
    # )
    # self.install_files("data/icons", "usr/share/icons/hicolor/symbolic/apps")
    # self.install_files("data/v1", "usr/share/cosmic")
