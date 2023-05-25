Name:           risios-copr-fix
Version:        38
Release:        1%{?dist}
Summary:        Copr fix
License:        GPL3
URL:            http://risi.io/
BuildArch:      noarch

%description
Adds a copr vendor config to use Fedora copr repos

%prep
%build
cat > copr.vendor.conf <<EOF
[main]
distribution = fedora
releasever = 38
EOF

%install
mkdir -p %{buildroot}%{_datadir}/dnf/plugins
install -m 655 copr.vendor.conf %{buildroot}%{_datadir}/dnf/plugins/copr.vendor.conf

%files
%{_datadir}/dnf/plugins/copr.vendor.conf

%changelog
* Wed May 24 2023 PizzaLovingNerd
- spec file created
