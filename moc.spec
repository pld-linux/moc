#
# bconds:
%bcond_without	home_etc    # disable HOME_ETC support
#
Summary:	Console audio player with simple ncurses interface
Summary(pl.UTF-8):	Konsolowy odtwarzacz audio z prostym interfejsem ncurses
Name:		moc
Version:	2.4.4
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	647c770a5542a4ae5437386807a89796
Patch0:		%{name}-home_etc.patch
URL:		http://moc.daper.net/
BuildRequires:	a52dec-libs-devel
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	ffmpeg-devel >= 0.4.9-4.20080822.1
BuildRequires:	flac-devel >= 1.1.3
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel >= 1.2
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libtool
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	speex-devel
BuildRequires:	taglib-devel >= 1.3.1
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_decoder_plugins	%{_libdir}/%{name}/decoder_plugins

%description
MOC is a console audio player with simple ncurses interface in
playmp3list style. It supports MP3, Ogg, FLAC, Musepack, Speex, WAV
and other less popular formats supported by libsndfile. It has all
functions one may expect from simple audio player. Now it supports net
streams (shoutcast, icecast, regular HTTP, FTP) also.

%description -l pl.UTF-8
MOC to konsolowy odtwarzacz audio z prostym interfejsem budzącym
skojarzenia z playmp3list. Obsługuje formaty MP3, Ogg, FLAC, Musepack,
Speex, WAV oraz inne mniej popularne formaty wspierane przez
bibliotekę libsndfile. Ma wszystkie funkcje, których można spodziewać
się w prostym odtwarzaczu audio. Teraz także obsługuje strumienie
sieciowe (shoutcast, icecast, HTTP, FTP).

%package mp3
Summary:	MP3 decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder MP3 dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description mp3
This package contains the MP3 decoder. After install you should reload
MOC player.

%description mp3 -l pl.UTF-8
Ten pakiet zawiera dekodowanie formatu MP3. Po zainstalowaniu należy
uruchomić ponownie MOC.

%package musepack
Summary:	Musepack (MPC) decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder Musepack (MPC) dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description musepack
This package contains the Musepack (MPC) decoder. After install you
should reload MOC player.

%description musepack -l pl.UTF-8
Ten pakiet zawiera dekodowanie formatu Musepack (MPC). Po
zainstalowaniu należy uruchomić ponownie MOC.

%package ogg
Summary:	Ogg decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder Ogg dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description ogg
This package contains the Ogg decoder. After install you should reload
MOC player.

%description ogg -l pl.UTF-8
Ten pakiet zawiera dekodowanie formatu Ogg. Po zainstalowaniu należy
uruchomić ponownie MOC.

%package flac
Summary:	FLAC decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder FLAC dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description flac
This package contains the FLAC decoder. After install you should
reload MOC player.

%description flac -l pl.UTF-8
Ten pakiet zawiera dekodowanie formatu FLAC. Po zainstalowaniu należy
uruchomić ponownie MOC.

%package ffmpeg
Summary:	ffmpeg decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder ffmpeg dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description ffmpeg
This package contains module to decode WMA (and others) files. After
install you should reload MOC player.

%description ffmpeg -l pl.UTF-8
Ten pakiet zawiera moduł dekodujący pliki w formacie WMA (i nie tylko)
Po zainstalowaniu należy uruchomić ponownie MOC.

%package sndfile
Summary:	Decoder of the sndfile formats for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder plików WAV/AIFF
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description sndfile
This package contains the decoders of sndfile. After install you
should reload MOC player.

%description sndfile -l pl.UTF-8
Ten pakiet zapewnia dekodowanie plików WAV/AIFF. Po zainstalowaniu
należy uruchomić ponownie MOC.

%package speex
Summary:	Speex decoder for MoC - Music on Console
Summary(pl.UTF-8):	Dekoder formatu Speex dla MOC
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}
Provides:	%{name}-input = %{version}-%{release}

%description speex
This package contains the Speex decoder. After install you should
reload MOC player.

%description speex -l pl.UTF-8
Ten pakiet zapewnia dekodowanie formatu Speex. Po zainstalowaniu
należy uruchomić ponownie MOC.

%prep
%setup -q
%{?with_home_etc:%patch0 -p1}

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%{__libtoolize}
%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/%{name}
rm -f $RPM_BUILD_ROOT%{_decoder_plugins}/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS NEWS README THANKS TODO *.example
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/moc
%dir %{_libdir}/moc/decoder_plugins
%{_datadir}/%{name}
%{_mandir}/man1/mocp*

%files musepack
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libmusepack_decoder.so*

%files flac
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libflac_decoder.so*

%files ffmpeg
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libffmpeg_decoder.so

%files mp3
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libmp3_decoder.so*

%files ogg
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libvorbis_decoder.so*

%files sndfile
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libsndfile_formats_decoder.so*

%files speex
%defattr(644,root,root,755)
%attr(755,root,root) %{_decoder_plugins}/libspeex_decoder.so*
