%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}
%define revision 705291

%if %{unstable}
%define dont_strip 1
%endif

Name: qimageblitz
Version: 0.0.4
Release: %mkrel 1 
Summary: Blitz is a graphics manipulation library 
License: GPL
Group: Development/KDE and Qt
Source: %name-%version.%revision.tar.bz2
BuildRequires: cmake >= 2.4.5
BuildRequires: qt4-devel >= 4.3.0
BuildRequires: pkgconfig
Obsoletes: blitz

%description
Blitz is a graphics manipulation library.

%files 
%defattr(-,root,root)
%_bindir/blitztest

#--------------------------------------------------------------------

%define libblitz %mklibname qimageblitz 4

%package -n %libblitz
Summary: Blitz library
Group: System/Libraries
Obsoletes: %{_lib}blitz4

%description -n %libblitz
Blitz library.

%post -n %libblitz -p /sbin/ldconfig
%postun -n %libblitz -p /sbin/ldconfig

%files -n %libblitz
%defattr(-,root,root)
%{_libdir}/*.so.*

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d qimageblitz

%package -n %libblitzdev
Requires: %libblitz
Summary: Development files for %name
Group: Development/KDE and Qt
Provides: lib%name-devel = %version
Provides: %name-devel = %version
Obsoletes: %{_lib}blitz-devel

%description -n %libblitzdev
Development files for %name.

%files -n %libblitzdev
%defattr(-,root,root)
%_libdir/*.so
%_includedir/qimageblitz
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


