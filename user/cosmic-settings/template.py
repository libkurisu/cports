pkgname = "cosmic-settings"
pkgver = "0.0.7"
pkgrel = 0
build_style = "cargo"
hostmakedepends = [
    "cargo-auditable",
    "libinput-devel",
    "libxkbcommon-devel",
    "pipewire-devel",
    "pkgconf",
    "udev-devel",
]
pkgdesc = "Settings application for the COSMIC desktop"
license = "MPL-2.0"
url = "https://github.com/pop-os/cosmic-settings"
source = f"{url}/archive/refs/tags/epoch-1.0.0-alpha.7.tar.gz"
sha256 = "95e632d20cf802fe293014dd9707e65bd7d6ab9e7459957f40b01c928908e34a"


def install(self):
    self.install_bin(f"target/{self.profile().triplet}/release/cosmic-settings")
    self.install_file(
        "resources/com.system76.CosmicSettings.desktop", "usr/share"
    )
    self.install_file(
        "resources/com.system76.CosmicSettings.metainfo.xml", "usr/share/metainfo"
    )
    self.install_files(
        "resources/icons", "usr/share/icons/hicolor/symbolic/apps"
    )
    self.install_files("resources/default_schema", "usr/share/cosmic")
    # TODO: Install desktop files (theres a lot of them)
