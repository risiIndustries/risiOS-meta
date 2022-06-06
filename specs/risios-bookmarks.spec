Name:           risios-bookmarks
Version:        36
Release:        %autorelease
Summary:        risiOS bookmarks
License:        GFDL
URL:            http://risi.io/
Source0:        https://raw.githubusercontent.com/risiOS/risiOS-meta/main/firefox/policies.json
BuildArch:      noarch
Provides:       system-bookmarks
 
 
%description
This package contains the default bookmarks for Fedora.
 
%prep
# We are nihilists, Lebowski.  We believe in nassing.
 
%build
# We are nihilists, Lebowski.  We believe in nassing.
 
%install
%{__rm} -rf $RPM_BUILD_ROOT
%{__mkdir_p} $RPM_BUILD_ROOT%{_datadir}/bookmarks
install -p -m 644 %{SOURCE0} $RPM_BUILD_ROOT%{_datadir}/bookmarks/default-bookmarks.html
 
 
 
%files
%dir %{_datadir}/bookmarks
%{_datadir}/bookmarks/default-bookmarks.html
 
%changelog
%autochangelog

