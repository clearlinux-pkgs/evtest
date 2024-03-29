#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : evtest
Version  : 1.35
Release  : 4
URL      : https://gitlab.freedesktop.org/libevdev/evtest/-/archive/evtest-1.35/evtest-evtest-1.35.tar.gz
Source0  : https://gitlab.freedesktop.org/libevdev/evtest/-/archive/evtest-1.35/evtest-evtest-1.35.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-2.0
Requires: evtest-bin = %{version}-%{release}
Requires: evtest-license = %{version}-%{release}
Requires: evtest-man = %{version}-%{release}
BuildRequires : asciidoc
BuildRequires : xmlto

%description
evtest — Kernel input device debugging
======================================
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
%setup -q -n evtest-evtest-1.35
cd %{_builddir}/evtest-evtest-1.35

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1666028643
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
export SOURCE_DATE_EPOCH=1666028643
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/evtest
cp %{_builddir}/evtest-evtest-%{version}/COPYING %{buildroot}/usr/share/package-licenses/evtest/06877624ea5c77efe3b7e39b0f909eda6e25a4ec || :
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
