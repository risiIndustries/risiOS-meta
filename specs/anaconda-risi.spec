Summary:	risiOS Anaconda Config Files
Name:     	anaconda-risi
Version:	0.2
Release:	4%{?dist}
License:	GPLv2+ and MIT
URL: 		https://github.com/risiOS/rpm-spec-files

BuildArch: 	noarch
Requires: 	anaconda
Requires:	risios-logos

%description
risiOS Anaconda Config Files

%prep
%build
cat > risiOS.conf <<EOF
# Anaconda configuration file for risiOS.

[Profile]
# Define the profile.
profile_id = risios
base_profile = fedora-workstation

[Profile Detection]
# Match os-release values.
os_id = risios

[User Interface]
custom_stylesheet = /usr/share/anaconda/pixmaps/risiOS.css
EOF

%install
mkdir -p %{buildroot}%{_sysconfdir}/anaconda/profile.d
install -m 655 risiOS.conf %{buildroot}%{_sysconfdir}/anaconda/profile.d/risiOS.conf

%files
%{_sysconfdir}/anaconda/profile.d/risiOS.conf

%changelog
* Wed Aug 11 2021 PizzaLovingNerd
- spec file created
