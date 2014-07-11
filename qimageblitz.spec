%define unstable 1
%{?_unstable:	%{expand:	%%global unstable 1}}

%define branch 1
%{?_branch:	%{expand:	%%global branch 1}}

%if %{unstable}
# We cannot use it when debug is set to nil
#define dont_strip 1
%endif

Summary:	Graphics manipulation library 
Name:		qimageblitz
Epoch:		1
Version:	0.0.6
Release:	12
License:	GPLv2
Group:		Development/KDE and Qt
Source0:	%{name}-%{version}.tar.bz2
BuildRequires:	cmake >= 2.4.5
BuildRequires:	qt4-devel >= 4.3.0

%description
Blitz is a graphics manipulation library.

%files 
%{_bindir}/blitztest

#--------------------------------------------------------------------

%define blitz_major 4
%define libblitz %mklibname qimageblitz %{blitz_major}

%package -n %{libblitz}
Summary:	Blitz library
Group:		System/Libraries

%description -n %{libblitz}
Blitz library.

%files -n %{libblitz}
%{_libdir}/libqimageblitz.so.%{blitz_major}*

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d qimageblitz

%package -n %{libblitzdev}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libblitz} = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{libblitzdev}
Development files for %{name}.

%files -n %{libblitzdev}
%{_libdir}/*.so
%{_includedir}/qimageblitz
%{_libdir}/pkgconfig/*

#--------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_qt4 \
	-DCMAKE_SKIP_RPATH:BOOL=ON \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DINCLUDE_INSTALL_DIR=%{_includedir}
%make

%install
%makeinstall_std -C build

