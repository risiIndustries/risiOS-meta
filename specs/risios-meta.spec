Name:           risios-meta
Version:        36
Release:        %autorelease
Summary:        General files for risiOS
License:        GPL3
URL:            http://risi.io/
Source0:        https://github.com/risiOS/risiOS-meta/archive/refs/heads/main.tar.gz
BuildArch:      noarch

Requires:		risi-zsh
Requires:		risios-bookmarks
Requires:		risios-logos
Requires:		risios-release
Requires:		risifetch
Requires:		zsh
Requires:		risios-repositories

Recommends:		adw-gtk-theme
Recommends: 	gnome-shell-extension-dock-from-dash
Recommends: 	gnome-shell-extension-risi-gnome
Recommends: 	risi-script
Recommends:		risi-settings
Recommends:		risi-tweaks
Recommends:		risi-welcome
Recommends:		mozilla-risiSearx

%description
Provides some extra files by default in the home dir.
 
%prep
%autosetup -n risiOS-meta-main

%build
%install
%{__mkdir_p} %{buildroot}%{_sysconfdir}
%{__mkdir_p} %{buildroot}%{_libdir}/firefox/distribution

cp -a skel %{buildroot}%{_sysconfdir}
cp -a firefox/policies.json %{buildroot}%{_libdir}/firefox/distribution

%files
%{_libdir}/firefox/distribution/policies.json
%dir %{_sysconfdir}/skel/Templates
%{_sysconfdir}/skel/Templates/*
 
%changelog
%autochangelog
