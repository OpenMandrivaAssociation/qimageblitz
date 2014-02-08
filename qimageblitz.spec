%define unstable 1
%{?_unstable: %{expand: %%global unstable 1}}

%define branch 1
%{?_branch: %{expand: %%global branch 1}}

%if %{unstable}
# We cannot use it when debug is set to nil
#define dont_strip 1
%endif

Name:		qimageblitz
Version:	0.0.6
Release:	7
Epoch:		1
Summary:	Graphics manipulation library 
License:	GPL
Group:		Development/KDE and Qt
Source:		%{name}-%{version}.tar.bz2
BuildRequires:	cmake >= 2.4.5
BuildRequires:	qt4-devel >= 4.3.0

%description
Blitz is a graphics manipulation library.

%files 
%_bindir/blitztest

#--------------------------------------------------------------------

%define blitz_major 4
%define libblitz %mklibname qimageblitz %{blitz_major}

%package -n %{libblitz}
Summary:	Blitz library
Group:		System/Libraries

%description -n %{libblitz}
Blitz library.

%files -n %{libblitz}
%{_libdir}/*.so.%{blitz_major}*

#--------------------------------------------------------------------

%define libblitzdev %mklibname -d qimageblitz

%package -n %{libblitzdev}
Summary:	Development files for %{name}
Group:		Development/KDE and Qt
Requires:	%{libblitz} = %{EVRD}
Provides:	lib%{name}-devel = %{EVRD}
Provides:	%{name}-devel = %{EVRD}

%description -n %{libblitzdev}
Development files for %{name}.

%files -n %libblitzdev
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

%changelog
* Thu May 05 2011 Oden Eriksson <oeriksson@mandriva.com> 1:0.0.6-4mdv2011.0
+ Revision: 669380
- mass rebuild

* Wed Oct 13 2010 Funda Wang <fwang@mandriva.org> 1:0.0.6-3mdv2011.0
+ Revision: 585274
- specify includedir

* Mon Oct 11 2010 Funda Wang <fwang@mandriva.org> 1:0.0.6-2mdv2011.0
+ Revision: 584877
- rebuild

* Tue Aug 17 2010 Nicolas Lécureuil <nlecureuil@mandriva.com> 1:0.0.6-1mdv2011.0
+ Revision: 571021
- New version
  Add epoch because of new version
  Fix requires

* Sat Feb 20 2010 Funda Wang <fwang@mandriva.org> 4.0.0-7mdv2010.1
+ Revision: 508725
- bump rel
- new snapshot (sync with kdesupport-for-4.4-tag)

* Thu Sep 03 2009 Christophe Fergeau <cfergeau@mandriva.com> 4.0.0-5mdv2010.0
+ Revision: 426795
- rebuild

* Thu Aug 07 2008 Thierry Vignaud <tv@mandriva.org> 4.0.0-4mdv2009.0
+ Revision: 265588
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Tue May 27 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-3mdv2009.0
+ Revision: 212066
- Libraries are now in _libdir

* Mon Feb 18 2008 Thierry Vignaud <tv@mandriva.org> 4.0.0-2mdv2008.1
+ Revision: 171073
- rebuild
- fix "foobar is blabla" summary (=> "blabla") so that it looks nice in rpmdrake

* Mon Jan 07 2008 Helio Chissini de Castro <helio@mandriva.com> 4.0.0-1mdv2008.1
+ Revision: 146288
- Update for current svn
- Proper version naming ( was inverted )
- New qimageblitz
- Upstream library changed name

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Tue Aug 21 2007 Helio Chissini de Castro <helio@mandriva.com> 0.0.4-1mdv2008.0
+ Revision: 68619
- Proper soname
- Changed dev library name
- import blitz-0.0.4-1mdv2008.0

