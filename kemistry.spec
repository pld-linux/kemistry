Summary:	A collection of chemical applications for KDE
Summary(pl):	Kolekcja aplikacji chemicznych dla KDE
Name:		kemistry
Version:	0.6
Release:	1
License:	GPL
Group:		X11/Applications/Science
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.bz2
URL:		http://kemistry.sourceforge.net/
BuildRequires:	fam-devel
BuildRequires:	kdelibs-devel >= 3.0.3
BuildRequires:	kdesdk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_htmldir	/usr/share/doc/kde/HTML

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
 - KemBabel - program do konwersji miêdzy chemicznymi formatami plików,
   bazowany na Open Babel,
 - KDrawchem - program do rysowania struktury molekularnej, bazowany na
   XDrawChem.

%package kdrawchem
Summary:	molecular structure drawing program based on XDrawChem
Summary(pl):	program do rysowania struktury molekularnej, bazowany na XDrawChem
Group:		X11/Applications/Science
Requires:	kemistry = %{version}
Provides:	kdrawchem

%description kdrawchem
A molecular structure drawing program based on XDrawChem.

%description kdrawchem -l pl
Program do rysowania struktury molekularnej, bazowany na XDrawChem.

%package kembabel
Summary:	conversion program for chemical file formats
Summary(pl):	program do konwersji miêdzy chemicznymi formatami plików
Group:		X11/Applications/Science
Requires:	kemistry = %{version}
Provides:	kembabel

%description kembabel
A conversion program for chemical file formats based on Open Babel.

%description kembabel -l pl
Program do konwersji miêdzy chemicznymi formatami plików, bazowany na
Open Babel.

%package kmolcalc
Summary:	molecular weight calculator
Summary(pl):	kalkulator wagi molowej
Group:		X11/Applications/Science
Requires:	kemistry = %{version}
Provides:	kmolcalc

%description kmolcalc
A molecular weight calculator.

%description kmolcalc -l pl
Kalkulator wagi molowej.

%prep
%setup -q -n %{name}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_applnkdir}/Scientific/Chemistry

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
mv $RPM_BUILD_ROOT%{_applnkdir}/{Applications/Kemistry/*,Scientific/Chemistry}

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
%doc README ChangeLog
%{_pixmapsdir}/*/*/*/kemistry.png
%attr(755,root,root) %{_libdir}/libopenbabel_kemistry.*

# This should be from openbabel:
%attr(755,root,root) %{_bindir}/babel
%{_datadir}/apps/openbabel/*.txt

%files kdrawchem -f kdrawchem.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kdrawchem
%attr(755,root,root) %{_libdir}/libkdrawchem.*
%dir %{_datadir}/apps/kdrawchem/*
%dir %{_datadir}/apps/kdrawchem/rings/*.cml
%{_pixmapsdir}/*/*/*/kdrawchem.png
%{_applnkdir}/Scientific/Chemistry/kdrawchem.desktop

%files kembabel -f kembabel.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kembabel
%{_datadir}/mimelnk/chemical/*openbabel*
%{_applnkdir}/Scientific/Chemistry/kembabel.desktop

%files kmolcalc -f kmolcalc.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kmolcalc
%dir %{_datadir}/apps/kmolcalc/*
%{_pixmapsdir}/*/*/*/kmolcalc.png
%{_applnkdir}/Scientific/Chemistry/kmolcalc.desktop
