%global extuuid		dock-from-dash@fthx
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		dock-from-dash
%global giturl		https://github.com/risiIndustries/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-dock-from-dash
Version:	64
Release:	7%{?dist}
Summary:	GNOME Shell Extension - Dock From Dash by fthx

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/4703/dock-from-dash/
Source0:	%{giturl}/archive/refs/tags/v%{version}.zip
BuildArch:	noarch
BuildRequires:  glib2
BuildRequires:	meson

%description
Dock for GNOME 40+. Does use native GNOME Shell Dash. Very light extension.

Hover the bottom of your screen and GNOME Shell dash will appear without overview.
Native GNOME Shell click behavior is modified: minimize if one window is open, overview if many windows are open.

%prep
%autosetup -n dock-from-dash-%{version}

%build
meson --prefix=%{buildroot}%{_exec_prefix} --localedir=share/gnome-shell/extensions/ding@rastersoft.com/locale .build

%install
ninja -C .build install

%files
%license LICENSE
%{extdir}

%changelog
* Tue Aug 09 2022 PizzaLovingNerd
- Install using meson instead of manually

* Thu Feb 24 2022 PizzaLovingNerd
- Spec file built
