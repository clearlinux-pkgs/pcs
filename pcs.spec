#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : pcs
Version  : 0.10.8
Release  : 13
URL      : https://github.com/ClusterLabs/pcs/archive/0.10.8/pcs-0.10.8.tar.gz
Source0  : https://github.com/ClusterLabs/pcs/archive/0.10.8/pcs-0.10.8.tar.gz
Summary  : Pacemaker command line interface and GUI
Group    : Development/Tools
License  : GPL-2.0
Requires: pcs-bin = %{version}-%{release}
Requires: pcs-license = %{version}-%{release}
Requires: pcs-python = %{version}-%{release}
Requires: pcs-python3 = %{version}-%{release}
Requires: pcs-services = %{version}-%{release}
Requires: Pacemaker
Requires: astroid
Requires: black
Requires: dacite
Requires: distro
Requires: dlm
Requires: mypy
Requires: pylint
Requires: python-dateutil
Requires: tornado
BuildRequires : Pacemaker
BuildRequires : astroid
BuildRequires : black
BuildRequires : buildreq-distutils3
BuildRequires : dacite
BuildRequires : distro
BuildRequires : dlm
BuildRequires : mypy
BuildRequires : pylint
BuildRequires : pyparsing
BuildRequires : python-dateutil
BuildRequires : tornado

%description
## PCS - Pacemaker/Corosync Configuration System
Pcs is a Corosync and Pacemaker configuration tool. It permits users to
easily view, modify and create Pacemaker based clusters. Pcs contains pcsd, a
pcs daemon, which operates as a remote server for pcs and provides a web UI.

%package bin
Summary: bin components for the pcs package.
Group: Binaries
Requires: pcs-license = %{version}-%{release}
Requires: pcs-services = %{version}-%{release}

%description bin
bin components for the pcs package.


%package license
Summary: license components for the pcs package.
Group: Default

%description license
license components for the pcs package.


%package python
Summary: python components for the pcs package.
Group: Default
Requires: pcs-python3 = %{version}-%{release}

%description python
python components for the pcs package.


%package python3
Summary: python3 components for the pcs package.
Group: Default
Requires: python3-core

%description python3
python3 components for the pcs package.


%package services
Summary: services components for the pcs package.
Group: Systemd services

%description services
services components for the pcs package.


%prep
%setup -q -n pcs-0.10.8
cd %{_builddir}/pcs-0.10.8

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1613615089
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/pcs
cp %{_builddir}/pcs-0.10.8/COPYING %{buildroot}/usr/share/package-licenses/pcs/4cc77b90af91e615a64ae04893fdffa7939db84c
cp %{_builddir}/pcs-0.10.8/pcs/COPYING %{buildroot}/usr/share/package-licenses/pcs/4cc77b90af91e615a64ae04893fdffa7939db84c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----
## install_append content
mkdir -p %{buildroot}/usr/lib/systemd/system
install pcsd/pcsd.service %{buildroot}/usr/lib/systemd/system/
## install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/pcs
/usr/bin/pcs_internal
/usr/bin/pcs_snmp_agent
/usr/bin/pcsd

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/pcs/4cc77b90af91e615a64ae04893fdffa7939db84c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/pcsd.service
