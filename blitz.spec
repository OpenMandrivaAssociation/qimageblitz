%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 702955

%if %{unstable}
%define dont_strip 1
%endif

Name: blitz
Version: 0.0.4
Release: %mkrel 1 
Summary: Blitz is a graphics manipulation library 
License: GPL
Group: Development/KDE and Qt
Source: %name-%version.%revision.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.3.0
BuildRequires: pkgconfig

%description
Blitz is a graphics manipulation library.

%files 
%defattr(-,root,root)
%_bindir/blitztest

#--------------------------------------------------------------------

%define libblitz %mklibname blitz 4

%package -n %libblitz
Summary: Blitz library
Group: System/Libraries

%description -n %libblitz
Blitz library.

%post -n %libblitz -p /sbin/ldconfig
%postun -n %libblitz -p /sbin/ldconfig

%files -n %libblitz
%defattr(-,root,root)
%{_libdir}/libblitz.so.*

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d blitz

%package -n %libblitzdev
Requires: %libblitz
Summary: Development files for %name
Group: Development/KDE and Qt
Provides: lib%name-devel = %version
Provides: %name-devel = %version

%description -n %libblitzdev
Development files for %name.

%files -n %libblitzdev
%defattr(-,root,root)
%_libdir/*.so
%_includedir/blitz
%_libdir/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4

%make

%install
cd build && make DESTDIR=%buildroot install

%clean
rm -fr %buildroot


