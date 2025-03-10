%define		module	dom_toml
Summary:	Dom’s tools for Tom’s Obvious, Minimal Language
Name:		python3-%{module}
Version:	2.0.1
Release:	1
License:	MIT
Group:		Libraries/Python
Source0:	https://pypi.debian.net/dom-toml/dom_toml-%{version}.tar.gz
# Source0-md5:	c344abe4af64faf71e651843cf9a6219
URL:		https://pypi.org/project/dom-toml/
BuildRequires:	python3-build
BuildRequires:	python3-installer
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 2.044
Requires:	python3-modules >= 1:3.2
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Dom's tools for Tom's Obvious, Minimal Language.

%prep
%setup -q -n dom_toml-%{version}

%build
%py3_build_pyproject

%install
rm -rf $RPM_BUILD_ROOT

%py3_install_pyproject

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{module}-%{version}.dist-info
