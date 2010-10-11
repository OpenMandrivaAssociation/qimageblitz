%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %{unstable}
%define dont_strip 1
%endif

Name:    qimageblitz
Version: 0.0.6
Release: %mkrel 2
Epoch:   1
Summary: Graphics manipulation library 
License: GPL
Group:   Development/KDE and Qt
Source:  %name-%version.tar.bz2
BuildRoot: %{_tmppath}/%{name}-buildroot
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

%if %mdkversion < 200900
%post -n %libblitz -p /sbin/ldconfig
%endif
%if %mdkversion < 200900
%postun -n %libblitz -p /sbin/ldconfig
%endif

%files -n %libblitz
%defattr(-,root,root)
%{_libdir}/*.so.4
%{_libdir}/*.so.4.*

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d qimageblitz

%package -n %libblitzdev
Requires: %libblitz
Summary: Development files for %name
Group: Development/KDE and Qt
Requires: %libblitz = %epoch:%version-%release
Provides: lib%name-devel = %epoch:%version-%release
Provides: %name-devel = %epoch:%version-%release
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
%cmake_qt4 \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DIB_INSTALL_DIR=%_libdir
%make

%install
rm -fr %buildroot
%makeinstall_std -C build

%clean
rm -fr %buildroot
