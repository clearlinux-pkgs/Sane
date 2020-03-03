#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : Sane
Version  : 2.8.3
Release  : 5
URL      : https://github.com/python-pillow/Sane/archive/v2.8.3.tar.gz
Source0  : https://github.com/python-pillow/Sane/archive/v2.8.3.tar.gz
Summary  : Scanner Access Now Easy
Group    : Development/Tools
License  : HPND
Requires: Sane-license = %{version}-%{release}
Requires: Sane-python = %{version}-%{release}
Requires: Sane-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : sane-backends-dev

%description
Python SANE module 2.8.3
========================
.. image:: https://travis-ci.org/python-pillow/Sane.svg
:target: https://travis-ci.org/python-pillow/Sane

%package license
Summary: license components for the Sane package.
Group: Default

%description license
license components for the Sane package.


%package python
Summary: python components for the Sane package.
Group: Default
Requires: Sane-python3 = %{version}-%{release}
Provides: sane-python

%description python
python components for the Sane package.


%package python3
Summary: python3 components for the Sane package.
Group: Default
Requires: python3-core

%description python3
python3 components for the Sane package.


%prep
%setup -q -n Sane-2.8.3
cd %{_builddir}/Sane-2.8.3

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1583222792
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/Sane
cp %{_builddir}/Sane-2.8.3/COPYING %{buildroot}/usr/share/package-licenses/Sane/459b82d6ee708b18521463ba4243bdf9a2a6e48e
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/Sane/459b82d6ee708b18521463ba4243bdf9a2a6e48e

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
