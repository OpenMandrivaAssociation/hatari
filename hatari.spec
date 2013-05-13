Name:			hatari
Version:		1.6.2
Release:		%mkrel 1

Summary:	An Atari ST emulator
License:	GPLv2+
Group:		Emulators
URL:		http://hatari.berlios.de/
Source0:	http://prdownload.berlios.de/%{name}/%{name}-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	SDL-devel
BuildRequires:	zlib-devel
BuildRequires:	pkgconfig(libpng)
BuildRequires:	portaudio-devel
BuildRequires:	pkgconfig(x11)
BuildRequires:	readline-devel
BuildRequires:	desktop-file-utils
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Hatari is an Atari ST and STE emulator.
The Atari ST was a 16/32 bit computer system which was first released by
Atari in 1985. Using the Motorola 68000 CPU, it was a very popular computer
having quite a lot of CPU power at that time. Unlike many other Atari ST
emulators which try to give you a good environment for running GEM
applications, Hatari tries to emulate the hardware of a ST as close as
possible so that it is able to run most of the old ST games and demos.

%prep
%setup -q

%build
./configure --prefix=%{_prefix}
%make

%install
rm -rf %{buildroot}
%makeinstall_std

#fr man pages
install -d -m 755 %{buildroot}/%{_mandir}/fr/man1
install -m 644 doc/fr/%{name}.1 %{buildroot}/%{_mandir}/fr/man1/

#desktop file
desktop-file-install --vendor="" \
  --remove-key="Version" \
  --remove-key="Encoding" \
  --add-category="Game" \
  --add-category="Emulator" \
  --add-category="X-MandrivaLinux-MoreApplications-Emulators" \
  --dir %{buildroot}%{_datadir}/applications/ \
  %{buildroot}%{_datadir}/applications/*

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc readme.txt doc/changelog.txt doc/fr/clavier-exemple.txt
%doc tools/hmsa/readme-hmsa.txt
%{_mandir}/man1/*.1*
%lang(fr) %{_mandir}/fr/man1/%{name}*.1*
%{_bindir}/%{name}*
%{_bindir}/hmsa
%{_bindir}/zip2st
%{_bindir}/atari-hd-image
%{_datadir}/%{name}
%{_iconsdir}/hicolor/32x32/apps/%{name}-icon.png
%{_datadir}/applications/%{name}ui.desktop



%changelog
* Sat Jun 30 2012 Zombie Ryushu <ryushu@mandriva.org> 1.6.2-1mdv2011.0
+ Revision: 807608
- Upgrade to 1.6.2

* Sun Jan 15 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.1-1
+ Revision: 760880
- New version 1.6.1

* Wed Jan 04 2012 Andrey Bondrov <abondrov@mandriva.org> 1.6.0-1
+ Revision: 753983
- New version 1.6.0

* Fri Jul 29 2011 Andrey Bondrov <abondrov@mandriva.org> 1.5.0-1
+ Revision: 692294
- Fix BuildRequires
- Fix BuildRequires
- imported package hatari


* Sun Jul 24 2011 Andrey Bondrov <bondrov@math.dvgu.ru> 1.5.0-1mdv2011.0
- 1.5.0
- Import from PLF
- Remove PLF reference

* Thu Dec  2 2010 Guillaume Bedot <littletux@zarb.org> 1.4.0-1plf2011.0
- 1.4.0
- fix build reqs, update patch, files list...

* Sat Sep  5 2009 Guillaume Bedot <littletux@zarb.org> 1.3.1-1plf2010.0
- Release 1.3.1
- Drop string-literal patch
- Add hatariui, new menu item and more doc and tools

* Mon Jan 26 2009 Guillaume Bedot <littletux@zarb.org> 1.2.0-1plf2009.1
- Release 1.2.0
- Fix menu tip
- Add zip2st

* Tue Jan  6 2009 Guillaume Bedot <littletux@zarb.org> 1.1.0-2plf2009.1
- Fix build for cooker

* Tue Jan  6 2009 Guillaume Bedot <littletux@zarb.org> 1.1.0-1plf2009.1
- New release 1.1.0

* Thu Apr 17 2008 Guillaume Bedot <littletux@zarb.org> 1.0.1-1plf2008.1
- 1.0.1

* Wed Mar 19 2008 Guillaume Bedot <littletux@zarb.org> 1.0.0-2plf2008.1
- fix 2007.1 build

* Tue Mar 18 2008 Guillaume Bedot <littletux@zarb.org> 1.0.0-1plf2008.1
- Release 1.0.0, build fixes, icon comment

* Mon May 14 2007 Guillaume Bedot <littletux@zarb.org> 0.95-1plf2008.0
- First PLF package

