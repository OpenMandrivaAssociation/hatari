Summary:	An Atari ST emulator
Name:		hatari
Version:	2.3.1
Release:	2
License:	GPLv2+
Group:		Emulators
URL:		http://hatari.tuxfamily.org/
Source0:	http://download.tuxfamily.org/%{name}/%{version}/%{name}-%{version}.tar.bz2
# Hatari comes with an outdated version of emutos (1.0) -- let's replace it
%define emutos_version 1.1.1
Source1:	https://netcologne.dl.sourceforge.net/project/emutos/emutos/%{emutos_version}/emutos-512k-%{emutos_version}.zip
Patch0:		hatari-1.7.0-static.patch
BuildRequires:	cmake ninja
BuildRequires:	pkgconfig(libpng)
BuildRequires:	pkgconfig(portaudio-2.0)
BuildRequires:	pkgconfig(sdl)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(zlib)
BuildRequires:	pkgconfig(udev)
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
%autosetup -p1 -a 1
# Update emutos
cp -f emutos-512k-%{emutos_version}/etos512us.img src/tos.img

# Now stuff should be sane
%cmake -G Ninja

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

%find_lang %{name} --with-man

%files -f %{name}.lang
%doc readme.txt doc/changelog.txt doc/fr/clavier-exemple.txt
%doc tools/hmsa/readme-hmsa.txt
%doc %{_docdir}/%{name}
%{_bindir}/%{name}*
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
