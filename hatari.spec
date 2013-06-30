Summary:	An Atari ST emulator
Name:		hatari
Version:	1.7.0
Release:	1
License:	GPLv2+
Group:		Emulators
URL:		http://hatari.berlios.de/
Source0:	http://prdownload.berlios.de/%{name}/%{name}-%{version}.tar.bz2
Patch0:		hatari-1.7.0-static.patch
BuildRequires:	cmake
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	readline-devel
BuildRequires:	desktop-file-utils

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
%patch0 -p1

%build
%cmake
%make

%install
%makeinstall_std -C build

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

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc readme.txt doc/changelog.txt doc/fr/clavier-exemple.txt
%doc tools/hmsa/readme-hmsa.txt
%{_bindir}/%{name}*
%{_bindir}/hmsa
%{_bindir}/gst2ascii
%{_bindir}/zip2st
%{_bindir}/atari-hd-image
%{_datadir}/%{name}
%{_datadir}/applications/%{name}ui.desktop
%{_iconsdir}/hicolor/32x32/apps/%{name}-icon.png
%{_mandir}/man1/*.1*
