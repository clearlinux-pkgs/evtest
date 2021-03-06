#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evtest
Version  : 1.34
Release  : 3
URL      : https://gitlab.freedesktop.org/libevdev/evtest/-/archive/evtest-1.34/evtest-evtest-1.34.tar.gz
Source0  : https://gitlab.freedesktop.org/libevdev/evtest/-/archive/evtest-1.34/evtest-evtest-1.34.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: evtest-bin = %{version}-%{release}
Requires: evtest-license = %{version}-%{release}
Requires: evtest-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : libxslt-bin
BuildRequires : xmlto

%description
Summary
=======
evtest is a tool to print evdev kernel events. It reads directly from the
kernel device and prints a device description and the events with the value
and the symbolic name.

%package bin
Summary: bin components for the evtest package.
Group: Binaries
Requires: evtest-license = %{version}-%{release}

%description bin
bin components for the evtest package.


%package license
Summary: license components for the evtest package.
Group: Default

%description license
license components for the evtest package.


%package man
Summary: man components for the evtest package.
Group: Default

%description man
man components for the evtest package.


%prep
%setup -q -n evtest-evtest-1.34
cd %{_builddir}/evtest-evtest-1.34

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1604358537
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
%autogen --disable-static
make  %{?_smp_mflags}

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make %{?_smp_mflags} check

%install
export SOURCE_DATE_EPOCH=1604358537
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/evtest
cp %{_builddir}/evtest-evtest-1.34/COPYING %{buildroot}/usr/share/package-licenses/evtest/06877624ea5c77efe3b7e39b0f909eda6e25a4ec
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/evtest

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/evtest/06877624ea5c77efe3b7e39b0f909eda6e25a4ec

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/evtest.1
