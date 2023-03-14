Name:           risios-meta
Version:        38
Release:        10%{?dist}
Summary:        General files for risiOS
License:        GPL3
URL:            http://risi.io/
Source0:        https://github.com/risiOS/risiOS-meta/archive/refs/heads/main.tar.gz
BuildArch:      noarch

Requires:		risios-bookmarks
Requires:		risios-logos
Requires:		risios-release
Requires:		risifetch
Requires:		zsh
Requires:		risios-repositories
Requires:  flatpak-timeout-fix
Requires:		rtheme-d
Requires:		rtheme-lib
Requires:		rtheme-plugin-gtk3
Requires:		rtheme-plugin-gtk4
Requires:		rtheme-plugin-gnome-shell

Recommends:		risi-zsh-plugins
Recommends:		adw-gtk-theme
Recommends: 	gnome-shell-extension-dock-from-dash
Recommends: 	gnome-shell-extension-risi-gnome
Recommends: 	risi-script
Recommends:		risi-settings
Recommends:		risi-tweaks
Recommends:		risi-welcome

%description
Provides some extra files by default in the home dir.
 
%prep
%autosetup -n risiOS-meta-main

%build
%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}/chromium/policies/recommended
%{__mkdir_p} %{buildroot}%{_sysconfdir}/gnome-initial-setup

cp gnome-initital-setup.conf %{buildroot}%{_sysconfdir}/gnome-initial-setup/vendor.conf
cp -a skel %{buildroot}%{_sysconfdir}
cp chromium-risios.json %{buildroot}%{_sysconfdir}/chromium/policies/recommended/risios.json

%files
%{_sysconfdir}/chromium/policies/recommended/risios.json
%dir %{_sysconfdir}/skel/Templates
%{_sysconfdir}/skel/Templates/*
%{_sysconfdir}/gnome-initial-setup/vendor.conf
 
%changelog
%autochangelog
