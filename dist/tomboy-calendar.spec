Name:         tomboy-calendar
License:      GPLv2
Group:        Productivity/Office/Other
Version:      0.1
Release:      1
Summary:      Simple calendar with tomboy integration
Source:	      %{name}-%{version}.tar.gz
URL:          http://www.beatniksoftware.com/tomboy/
BuildRoot:    %{_tmppath}/%{name}-%{version}-root
Packager:     Humberto Henrique Campos Pinheiro

%description
Simple calendar with tomboy integration.

%prep
%setup -q 

%install
mkdir -p $RPM_BUILD_ROOT/usr/share/pixmaps/
mkdir -p $RPM_BUILD_ROOT/usr/share/applications/
mkdir -p $RPM_BUILD_ROOT/usr/share/%{name}/

install -m 644 %{name}.png $RPM_BUILD_ROOT/usr/share/pixmaps
install -m 644 %{name}.desktop $RPM_BUILD_ROOT/usr/share/applications
install -m 644 calendar.py tomboy.py $RPM_BUILD_ROOT/usr/share/%{name}
install -m 644 interface.glade $RPM_BUILD_ROOT/usr/share/%{name}
install -m 644 calendar.gif $RPM_BUILD_ROOT/usr/share/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-, root, root)
/usr/share/applications/%{name}.desktop
/usr/share/pixmaps/%{name}.png
/usr/share/%{name}/*

%changelog
* Fri Sep 11 2009 - Humberto H. C. Pinheiro <humberto@syst.com.br> - 0.1-1
- First release.
