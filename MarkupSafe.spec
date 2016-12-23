#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : MarkupSafe
Version  : 0.23
Release  : 17
URL      : https://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-0.23.tar.gz
Source0  : https://pypi.python.org/packages/source/M/MarkupSafe/MarkupSafe-0.23.tar.gz
Summary  : Implements a XML/HTML/XHTML Markup safe string for Python
Group    : Development/Tools
License  : BSD-3-Clause
Requires: MarkupSafe-python
BuildRequires : pbr
BuildRequires : pip
BuildRequires : python-dev
BuildRequires : python3-dev
BuildRequires : setuptools

%description
MarkupSafe
==========
Implements a unicode subclass that supports HTML strings:
>>> from markupsafe import Markup, escape
>>> escape("<script>alert(document.cookie);</script>")
Markup(u'&lt;script&gt;alert(document.cookie);&lt;/script&gt;')
>>> tmpl = Markup("<em>%s</em>")
>>> tmpl % "Peter > Lustig"
Markup(u'<em>Peter &gt; Lustig</em>')

%package python
Summary: python components for the MarkupSafe package.
Group: Default
Provides: markupsafe-python

%description python
python components for the MarkupSafe package.


%prep
%setup -q -n MarkupSafe-0.23

%build
python2 setup.py build -b py2
python3 setup.py build -b py3

%check
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
python2 setup.py test
%install
rm -rf %{buildroot}
python2 setup.py build -b py2 install --root=%{buildroot}
python3 setup.py build -b py3 install --root=%{buildroot}

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)
/usr/lib/python*/*
