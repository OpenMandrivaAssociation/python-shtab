%undefine _debugsource_packages
Name:		python-shtab
Version:	1.8.0
Release:	2
Source0:	https://files.pythonhosted.org/packages/source/s/shtab/shtab-%{version}.tar.gz
Summary:	Automagic shell tab completion for Python CLI applications
URL:		https://pypi.org/project/shtab/
License:	Apache-2.0
Group:		Development/Python
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(setuptools)
BuildRequires:  python%{pyver}dist(setuptools_scm)
BuildArch:	noarch

%description
Automagic shell tab completion for Python CLI applications

%prep
%autosetup -p1 -n shtab-%{version}

%build
%py_build

%install
%py_install

%files
%{_bindir}/shtab
%{py_sitedir}/shtab
#{py_sitedir}/shtab-%{version}.dist-info
