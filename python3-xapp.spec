%define		module	xapp
Summary:	Python 3 XApp library
Summary(pl.UTF-8):	Biblioteka XApp dla Pythona 3
Name:		python3-%{module}
Version:	2.4.1
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
#Source0Download: https://github.com/linuxmint/python3-xapp/tags
Source0:	https://github.com/linuxmint/python3-xapp/archive/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	1d1b2fc7ea3e7d3f0a709017f73628dc
URL:		https://github.com/linuxmint/python3-xapp/
BuildRequires:	meson >= 0.47.0
BuildRequires:	ninja >= 1.5
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.736
Requires:	python3-psutil
Requires:	python3-pygobject3 >= 3.0
# gir modules
Requires:	gtk+3 >= 3.0
Requires:	xapps-libs >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 3 XApp library.

%description -l pl.UTF-8
Biblioteka XApp dla Pythona 3.

%prep
%setup -q

%build
%meson build

%ninja_build -C build

%install
rm -rf $RPM_BUILD_ROOT

%ninja_install -C build

%py3_comp $RPM_BUILD_ROOT%{py3_sitescriptdir}
%py3_ocomp $RPM_BUILD_ROOT%{py3_sitescriptdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{py3_sitescriptdir}/xapp
