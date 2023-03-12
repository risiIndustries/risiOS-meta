Name:		adw-gtk-theme
Version:	99
Release:	5%{?dist}
Summary:	Metapackage that installs adw-gtk3 and adw-gtk4

License:	GPLv2+
URL:		https://github.com/lassekongo83/adw-gtk3

Requires: adw-gtk3
Requires: adw-gtk4

BuildArch:	noarch

%description
Metapackage that installs adw-gtk3 and adw-gtk4

%prep
%install
%files

%changelog
* Sat Feb 4 2023 PizzaLovingNerd
- Converted to metapackage

* Wed Mar 2 2022 PizzaLovingNerd
- Spec file built
