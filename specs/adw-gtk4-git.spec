Name:           adw-gtk4-git
# Match Current Libadwaita Version
Version:        main
Release:        2%{?dist}
Summary:        The theme from libadwaita ported to stock GTK-4
License:        GPLv2+
URL:            https://github.com/lassekongo83/adw-gtk3/blob/main/gtk4.md
BuildRequires: sassc
BuildRequires: git
BuildRequires: vala
BuildRequires: gobject-introspection-devel
BuildRequires: gtk4-devel
BuildRequires: cmake
BuildRequires: meson
BuildRequires: ninja-build
Requires: adw-gtk3
Provides:	adw-gtk4

%description
The theme from libadwaita ported to stock GTK-4

%prep
git clone https://gitlab.gnome.org/GNOME/libadwaita.git

%build
cd libadwaita
meson . _build
ninja -C _build

%install
cd libadwaita
mkdir -p %{buildroot}%{_datadir}/themes/adw-gtk3
mkdir -p %{buildroot}%{_datadir}/themes/adw-gtk3-dark
cp -a _build/src/stylesheet %{buildroot}%{_datadir}/themes/adw-gtk3/gtk-4.0
cp -a _build/src/stylesheet %{buildroot}%{_datadir}/themes/adw-gtk3-dark/gtk-4.0
mv %{buildroot}%{_datadir}/themes/adw-gtk3/gtk-4.0/base.css %{buildroot}%{_datadir}/themes/adw-gtk3/gtk-4.0/gtk.css
mv %{buildroot}%{_datadir}/themes/adw-gtk3-dark/gtk-4.0/base.css %{buildroot}%{_datadir}/themes/adw-gtk3-dark/gtk-4.0/gtk.css
sed -i '1 i\@import url("/usr/share/themes/adw-gtk3-dark/gtk-4.0/defaults-light.css");\n' %{buildroot}%{_datadir}/themes/adw-gtk3/gtk-4.0/gtk.css
sed -i '1 i\@import url("/usr/share/themes/adw-gtk3-dark/gtk-4.0/defaults-dark.css");\n' %{buildroot}%{_datadir}/themes/adw-gtk3-dark/gtk-4.0/gtk.css

%files
%{_datadir}/themes/adw-gtk3/gtk-4.0/
%{_datadir}/themes/adw-gtk3-dark/gtk-4.0/
