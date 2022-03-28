#
# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module	xapp
Summary:	Python bindings for xapps
Name:		python-%{module}
Version:	1.8.1
Release:	1
License:	LGPL v2+
Group:		Libraries/Python
Source0:	https://github.com/linuxmint/python-xapp/archive/%{version}.tar.gz
# Source0-md5:	f6a59d8f7177cfb9b89b3097ed176061
URL:		https://github.com/linuxmint/python-xapp/
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.710
%if %{with python2}
BuildRequires:	python-distribute
BuildRequires:	python-modules
%endif
%if %{with python3}
BuildRequires:	python3-modules
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Python bindings for xapps.

%package -n python3-%{module}
Summary:	Python bindings for xapps.
Group:		Libraries/Python

%description -n python3-%{module}
Python bindings for xapps.

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
%dir %{py_sitescriptdir}/xapp
%{py_sitescriptdir}/xapp/*.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitescriptdir}/python_xapp-%{version}-py*.egg-info
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%dir %{py3_sitescriptdir}/xapp
%{py3_sitescriptdir}/xapp/*.py
%dir %{py3_sitescriptdir}/xapp/__pycache__
%{py3_sitescriptdir}/xapp/__pycache__/*.py[co]
%{py3_sitescriptdir}/python_xapp-%{version}-py*.egg-info
%endif
