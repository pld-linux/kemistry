Summary:	A collection of chemical applications for KDE
Summary(pl):	Kolekcja aplikacji chemicznych dla KDE
Name:		kemistry
Version:	0.7
Release:	2
License:	GPL
Group:		X11/Applications/Science
Source0:	http://dl.sourceforge.net/kemistry/%{name}-%{version}.tar.bz2
# Source0-md5:	daa7c379a7ac6a866fe0c63f021bbd7e
URL:		http://kemistry.sourceforge.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	kdesdk-po2xml
BuildRequires:	libtool
BuildRequires:	rpmbuild(macros) >= 1.129
Requires:	openbabel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kemistry is a collection of chemical applications for the K Desktop
Environment. The included applications are:

- KMolCalc - a molecular weight calculator
- KemBabel - a conversion program for chemical file formats based on
  Open Babel
- KDrawchem - a molecular structure drawing program based on XDrawChem

%description -l pl
Kemistry jest kolekcj± aplikacji chemicznych dla KDE. Zawiera
aplikacje:
 - KMolCalc - kalkulator wagi molowej,
 - KemBabel - program do konwersji miêdzy chemicznymi formatami
   plików, oparty na Open Babel,
 - KDrawchem - program do rysowania struktury molekularnej, oparty na
   XDrawChem.

%package kdrawchem
Summary:	Molecular structure drawing program based on XDrawChem
Summary(pl):	Program do rysowania struktury molekularnej, bazowany na XDrawChem
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}
Provides:	kdrawchem

%description kdrawchem
A molecular structure drawing program based on XDrawChem.

%description kdrawchem -l pl
Program do rysowania struktury molekularnej, oparty na XDrawChem.

%package kembabel
Summary:	Conversion program for chemical file formats
Summary(pl):	Program do konwersji miêdzy chemicznymi formatami plików
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}
Provides:	kembabel

%description kembabel
A conversion program for chemical file formats based on Open Babel.

%description kembabel -l pl
Program do konwersji miêdzy chemicznymi formatami plików, oparty na
Open Babel.

%package kmolcalc
Summary:	Molecular weight calculator
Summary(pl):	Kalkulator wagi molowej
Group:		X11/Applications/Science
Requires:	%{name} = %{version}-%{release}
Provides:	kmolcalc

%description kmolcalc
A molecular weight calculator.

%description kmolcalc -l pl
Kalkulator wagi molowej.

%prep
%setup -q

# kill libtool.m4
# -Wbad-function-cast (invalid in C++) causes -fPIC misdetection
head -n 4875 acinclude.m4 | grep -v Wbad-function-cast > acinclude.m4.tmp
mv -f acinclude.m4.tmp acinclude.m4

%build
kde_htmldir="%{_kdedocdir}"; export kde_htmldir
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%{__perl} admin/am_edit
# doesn't work with am > 1.6
#%{__make} -f admin/Makefile.common cvs
%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_desktopdir}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT{%{_datadir}/applnk/Applications/Kemistry/*,%{_desktopdir}}

cp openbabel/ChangeLog ChangeLog.openbabel

%find_lang kdrawchem	--with-kde
%find_lang kembabel	--with-kde
%find_lang kmolcalc	--with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%post	kdrawchem -p /sbin/ldconfig
%postun	kdrawchem -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README ChangeLog* openbabel/CHANGES.openbabel
%attr(755,root,root) %{_libdir}/libopenbabel_kemistry.so*
%attr(755,root,root) %{_libdir}/libkemistry.so*
%{_libdir}/libopenbabel_kemistry.la
%{_libdir}/libkemistry.la
%{_iconsdir}/*/*/*/kemistry.png

%files kdrawchem -f kdrawchem.lang
%defattr(644,root,root,755)
%doc kdrawchem/ChangeLog
%attr(755,root,root) %{_bindir}/kdrawchem
%attr(755,root,root) %{_libdir}/libkdrawchem.so*
%{_libdir}/libkdrawchem.la
%{_datadir}/apps/kdrawchem
%{_iconsdir}/*/*/*/kdrawchem.png
%{_desktopdir}/kdrawchem.desktop

%files kembabel -f kembabel.lang
%defattr(644,root,root,755)
%doc kembabel/ChangeLog
%attr(755,root,root) %{_bindir}/kembabel
%{_datadir}/mimelnk/chemical/*openbabel*
%{_iconsdir}/*/*/*/kembabel.png
%{_desktopdir}/kembabel.desktop

%files kmolcalc -f kmolcalc.lang
%defattr(644,root,root,755)
%doc kmolcalc/ChangeLog
%attr(755,root,root) %{_bindir}/kmolcalc
%dir %{_datadir}/apps/kmolcalc/*
%{_iconsdir}/*/*/*/kmolcalc.png
%{_desktopdir}/kmolcalc.desktop
