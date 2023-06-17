#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	xapp
Summary:	Python 2 XApp library
Summary(pl.UTF-8):	Biblioteka XApp dla Pythona 2
Name:		python-%{module}
Version:	1.8.1
Release:	3
License:	LGPL v2+
Group:		Libraries/Python
#Source0Download: https://github.com/linuxmint/python-xapp/tags
#Source0:	https://github.com/linuxmint/python-xapp/archive/%{version}/%{name}-%{version}.tar.gz
Source0:	https://github.com/linuxmint/python-xapp/archive/%{version}.tar.gz
# Source0-md5:	f6a59d8f7177cfb9b89b3097ed176061
URL:		https://github.com/linuxmint/python-xapp/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules >= 1:2.6
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
%endif
Requires:	python-psutil
Requires:	python-pygobject3 >= 3.0
# gir modules
Requires:	gtk+3 >= 3.0
Requires:	xapps-libs >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python 2 XApp library.

%description -l pl.UTF-8
Biblioteka XApp dla Pythona 2.

%package -n python3-%{module}
Summary:	Python 3 XApp library
Summary(pl.UTF-8):	Biblioteka XApp dla Pythona 3
Group:		Libraries/Python
Requires:	python3-psutil
Requires:	python3-pygobject3 >= 3.0
# gir modules
Requires:	gtk+3 >= 3.0
Requires:	xapps-libs >= 1.0

%description -n python3-%{module}
Python 3 XApp library.

%description -n python3-%{module} -l pl.UTF-8
Biblioteka XApp dla Pythona 3.

%prep
%setup -q

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%{py_sitescriptdir}/xapp
%{py_sitescriptdir}/python_xapp-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%{py3_sitescriptdir}/xapp
%{py3_sitescriptdir}/python_xapp-%{version}-py*.egg-info
%endif
