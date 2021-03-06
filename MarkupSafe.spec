#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
# Source0 file verified with key 0x7A1C87E3F5BC42A8 (davidism@gmail.com)
#
Name     : MarkupSafe
Version  : 2.0.1
Release  : 75
URL      : https://files.pythonhosted.org/packages/bf/10/ff66fea6d1788c458663a84d88787bae15d45daa16f6b3ef33322a51fc7e/MarkupSafe-2.0.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/bf/10/ff66fea6d1788c458663a84d88787bae15d45daa16f6b3ef33322a51fc7e/MarkupSafe-2.0.1.tar.gz
Source1  : https://files.pythonhosted.org/packages/bf/10/ff66fea6d1788c458663a84d88787bae15d45daa16f6b3ef33322a51fc7e/MarkupSafe-2.0.1.tar.gz.asc
Summary  : Safely add untrusted strings to HTML/XML markup.
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MarkupSafe-license = %{version}-%{release}
Requires: MarkupSafe-python = %{version}-%{release}
Requires: MarkupSafe-python3 = %{version}-%{release}
BuildRequires : buildreq-distutils3
BuildRequires : pluggy
BuildRequires : py-python
BuildRequires : pytest
BuildRequires : tox
BuildRequires : virtualenv

%description
==========
        
        MarkupSafe implements a text object that escapes characters so it is
        safe to use in HTML and XML. Characters that have special meanings are
        replaced so that they display as the actual characters. This mitigates
        injection attacks, meaning untrusted user input can safely be displayed
        on a page.
        
        
        Installing
        ----------

%package license
Summary: license components for the MarkupSafe package.
Group: Default

%description license
license components for the MarkupSafe package.


%package python
Summary: python components for the MarkupSafe package.
Group: Default
Requires: MarkupSafe-python3 = %{version}-%{release}
Provides: markupsafe-python

%description python
python components for the MarkupSafe package.


%package python3
Summary: python3 components for the MarkupSafe package.
Group: Default
Requires: python3-core
Provides: pypi(markupsafe)

%description python3
python3 components for the MarkupSafe package.


%prep
%setup -q -n MarkupSafe-2.0.1
cd %{_builddir}/MarkupSafe-2.0.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1621434567
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/MarkupSafe
cp %{_builddir}/MarkupSafe-2.0.1/LICENSE.rst %{buildroot}/usr/share/package-licenses/MarkupSafe/e32a549b135c4b2b268107adc12d13cca2ca1e8c
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/MarkupSafe/e32a549b135c4b2b268107adc12d13cca2ca1e8c

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
