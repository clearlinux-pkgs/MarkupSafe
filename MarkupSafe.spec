#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : MarkupSafe
Version  : 1.0
Release  : 30
URL      : https://pypi.debian.net/MarkupSafe/MarkupSafe-1.0.tar.gz
Source0  : https://pypi.debian.net/MarkupSafe/MarkupSafe-1.0.tar.gz
Summary  : Implements a XML/HTML/XHTML Markup safe string for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MarkupSafe-legacypython
Requires: MarkupSafe-python3
Requires: MarkupSafe-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
==========

%package legacypython
Summary: legacypython components for the MarkupSafe package.
Group: Default
Requires: python-core

%description legacypython
legacypython components for the MarkupSafe package.


%package python
Summary: python components for the MarkupSafe package.
Group: Default
Requires: MarkupSafe-legacypython
Requires: MarkupSafe-python3
Provides: markupsafe-python

%description python
python components for the MarkupSafe package.


%package python3
Summary: python3 components for the MarkupSafe package.
Group: Default
Requires: python3-core

%description python3
python3 components for the MarkupSafe package.


%prep
%setup -q -n MarkupSafe-1.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1507159692
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
PYTHONPATH=%{buildroot}/usr/lib/python3.6/site-packages python3 setup.py test
%install
export SOURCE_DATE_EPOCH=1507159692
rm -rf %{buildroot}
python2 -tt setup.py build -b py2 install --root=%{buildroot} --force
python3 -tt setup.py build -b py3 install --root=%{buildroot} --force
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files legacypython
%defattr(-,root,root,-)
/usr/lib/python2*/*

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
