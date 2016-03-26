%define debug_package %nil
%define unstable 1
%{?_unstable:	%{expand:	%%global unstable 1}}

%define branch 1
%{?_branch:	%{expand:	%%global branch 1}}

%define git 1393389

%if %{unstable}
# We cannot use it when debug is set to nil
#define dont_strip 1
%endif
%bcond_with qt5

Summary:	Graphics manipulation library 
Name:		qimageblitz
Epoch:		1
Release:	10
License:	GPLv2
Group:		Development/KDE and Qt
# svn://anonsvn.kde.org/home/kde/trunk/kdesupport/qimageblitz
%if %{git}
Source0:	%{name}-%{git}.tar.xz
Version:	0.0.6.%{git}
%else
Source0:	%{name}-%{version}.tar.bz2
Version:	0.0.6
%endif
BuildRequires:	cmake >= 2.4.5
%if %{with qt5}
BuildRequires:	qt5-devel
%endif
BuildRequires:	qt4-devel

%libpackage qimageblitz 4
%if %{with qt5}
%libpackage qimageblitz 5
%endif

%description
Blitz is a graphics manipulation library.

%files 
%{_bindir}/blitztest

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d qimageblitz
%define libblitz4dev %mklibname -d qimageblitz-qt4
%if %{with qt5}
%define libblitz5dev %mklibname -d qimageblitz-qt5
%endif

%package -n %{libblitzdev}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
%if %{with qt5}
Requires:	%{mklibname qimageblitz 5} = %{EVRD}
%endif
Requires:	%{name}-devel = %{EVRD}

%description -n %{libblitzdev}
Development files for %{name}.

%files -n %{libblitzdev}
%if %{with qt5}
%ghost %{_libdir}/libqimageblitz.so
%ghost %{_libdir}/pkgconfig/qimageblitz.pc
%endif
%{_includedir}/qimageblitz

%package -n %{libblitz4dev}
Summary:	Development files for the Qt4 version of %{name}
Group:		Development/KDE and Qt
Requires:	%{mklibname qimageblitz 4} = %{EVRD}
Requires:	%{libblitzdev} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
%ifarch %arm
Provides:	devel(libqimageblitz)
%endif
Provides:	pkgconfig(qimageblitz) = 4.0.0-1
Conflicts:	pkgconfig(qimageblitz) > 5.0.0-0

%description -n %{libblitz4dev}
Development files for the Qt4 version of %{name}

%files -n %{libblitz4dev}
%if !%{with qt5}
%{_libdir}/libqimageblitz.so
%{_libdir}/pkgconfig/qimageblitz.pc
%endif

%if %{with qt5}
%{_libdir}/libqimageblitz-qt4.so
%{_libdir}/pkgconfig/qimageblitz-qt4.pc

%post -n %{libblitz4dev}
ln -sf libqimageblitz-qt4.so %{_libdir}/libqimageblitz.so
ln -sf qimageblitz-qt4.pc %{_libdir}/pkgconfig/qimageblitz.pc
%endif

%if %{with qt5}
%package -n %{libblitz5dev}
Summary:	Development files for the Qt5 version of %{name}
Group:		Development/KDE and Qt
Requires:	%{mklibname qimageblitz 5} = %{EVRD}
Requires:	%{libblitzdev} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}
Provides:	pkgconfig(qimageblitz) = 5.0.0-1
Conflicts:	pkgconfig(qimageblitz) < 5.0.0-0

%description -n %{libblitz5dev}
Development files for the Qt5 version of %{name}

%files -n %{libblitz5dev}
%{_libdir}/libqimageblitz-qt5.so
%{_libdir}/pkgconfig/qimageblitz-qt5.pc

%post -n %{libblitz5dev}
ln -sf libqimageblitz-qt5.so %{_libdir}/libqimageblitz.so
ln -sf qimageblitz-qt5.pc %{_libdir}/pkgconfig/qimageblitz.pc
%endif
#--------------------------------------------------------------------

%prep
%setup -q -n %{name}

%build
%if %{with qt5}
%cmake \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DINCLUDE_INSTALL_DIR=%{_includedir}
%make

cd ..
%endif

# We can install both versions into the same prefix
# because the headers are actually identical
mkdir build-qt4
cd build-qt4
cmake .. \
	-DQT4_BUILD:BOOL=ON \
	-DCMAKE_INSTALL_PREFIX:PATH=%{_prefix} \
	-DCMAKE_INSTALL_LIBDIR:PATH=%{_lib} \
	-DLIB_INSTALL_DIR:PATH=%{_lib} \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DINCLUDE_INSTALL_DIR=%{_includedir}
%make

%install
%makeinstall_std -C build-qt4
%if %{with qt5}
mv %{buildroot}%{_libdir}/pkgconfig/qimageblitz.pc %{buildroot}%{_libdir}/pkgconfig/qimageblitz-qt4.pc
mv %{buildroot}%{_libdir}/libqimageblitz.so %{buildroot}%{_libdir}/libqimageblitz-qt4.so
%makeinstall_std -C build
mv %{buildroot}%{_libdir}/pkgconfig/qimageblitz.pc %{buildroot}%{_libdir}/pkgconfig/qimageblitz-qt5.pc
mv %{buildroot}%{_libdir}/libqimageblitz.so %{buildroot}%{_libdir}/libqimageblitz-qt5.so
%endif

touch %{buildroot}%{_libdir}/pkgconfig/qimageblitz.pc
touch %{buildroot}%{_libdir}/libqimageblitz.so
