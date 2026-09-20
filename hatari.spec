Summary:	An Atari ST/STE/TT/Falcon emulator
Name:		hatari
Version:	2.6.1
Release:	1
License:	GPLv2+
Group:		Emulators
URL:		https://www.hatari-emu.org/
Source0:	https://framagit.org/hatari/releases/-/raw/main/v%{version}/%{name}-%{version}.tar.bz2
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(sdl2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(udev)
BuildRequires:	pkgconfig(capstone)
BuildRequires:	pkgconfig(gtk+-3.0)
BuildRequires:	readline-devel
BuildRequires:	desktop-file-utils
BuildRequires:	python
BuildRequires:	python-gobject3
# zip2st / atari-hd-image
Requires:	unzip
Requires:	mtools
Requires:	dosfstools
Requires:	python
Requires:	python-gobject3
Requires:	gtk+3.0

%description
Hatari is an Atari ST, STE, TT and Falcon emulator.
The Atari ST was a 16/32 bit computer system which was first released by
Atari in 1985. Using the Motorola 68000 CPU, it was a very popular computer
having quite a lot of CPU power at that time. Unlike many other Atari ST
emulators which try to give you a good environment for running GEM
applications, Hatari tries to emulate the hardware of a ST as close as
possible so that it is able to run most of the old ST games and demos.

%prep
%autosetup -p1

%cmake -G Ninja \
	-DBUILD_SHARED_LIBS:BOOL=OFF

%build
%ninja_build -C build

%install
%ninja_install -C build

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

%files
%{_docdir}/%{name}
%{_bindir}/hatari
%{_bindir}/hatariui
%{_bindir}/hatari-prg-args
%{_bindir}/hatari_profile
%{_bindir}/hmsa
%{_bindir}/gst2ascii
%{_bindir}/zip2st
%{_bindir}/atari-hd-image
%{_bindir}/atari-convert-dir
%{_datadir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/applications/%{name}ui.desktop
%{_datadir}/mime/packages/%{name}.*
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-st-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.fastcopy-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-vnd.msa-disk-image.*
%{_iconsdir}/hicolor/*/mimetypes/application-x-stx-disk-image.*
%{_mandir}/man1/*.1*
%{_mandir}/fr/man1/*.1*
