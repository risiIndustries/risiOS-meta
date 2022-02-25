%global extuuid		dock-from-dash@fthx
%global extdir		%{_datadir}/gnome-shell/extensions/%{extuuid}
%global gschemadir	%{_datadir}/glib-2.0/schemas
%global gitname		dock-from-dash
%global giturl		https://github.com/fthx/%{gitname}
%global srcdir		%{_builddir}/%{gitname}-%{version}/src

Name:		gnome-shell-extension-dock-from-dash
Version:	22
Release:	1%{?dist}
Summary:	GNOME Shell Extension - Dock From Dash by fthx

License:	GPLv2+
URL:		https://extensions.gnome.org/extension/4703/dock-from-dash/
Source0:	%{giturl}/archive/v%{version}.tar.gz#/%{gitname}-v%{version}.tar.gz

BuildArch:	noarch
BuildRequires:  glib2
Requires:	gnome-shell-extension-common

%description
Dock for GNOME 40+. Does use native GNOME Shell Dash. Very light extension.

Hover the bottom of your screen and GNOME Shell dash will appear without overview.
Native GNOME Shell click behavior is modified: minimize if one window is open, overview if many windows are open.

%prep
%autosetup -n dock-from-dash-%{version}
rm dock-from-dash@fthx.zip

%install
mkdir -p %{buildroot}%{_datadir}/gnome-shell/extensions
mkdir -p %{buildroot}/usr/share/licenses/%{NAME}
cp %{_builddir}/%{gitname}-%{version}/LICENSE %{buildroot}/usr/share/licenses/gnome-shell-extension-dock-from-dash/
cp -ar %{srcdir} %{buildroot}%{_datadir}/gnome-shell/extensions/%{extuuid}

%files
%license LICENSE
%{extdir}

%changelog
* Thu Feb 24 2022 PizzaLovingNerd
- Spec file built
