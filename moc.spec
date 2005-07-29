
# I know, console<->terminal
Summary:	Console audio player with simple ncurses interface
Summary(pl):	Konsolowy odtwarzacz audio z prostym interfejsem ncurses
Name:		moc
Version:	2.3.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}.tar.bz2
# Source0-md5:	3d5d152c28f6e40162058fc1566c8109
URL:		http://moc.daper.net/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	curl-devel
BuildRequires:	flac-devel
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libltdl-devel
BuildRequires:	libmad-devel
BuildRequires:	libmpcdec-devel >= 1.2
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	pkgconfig
BuildRequires:	taglib-devel >= 1.3.1
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MOC is a console audio player with simple ncurses interface in
playmp3list style. It supports MP3, Ogg, FLAC, Musepack, Speex, WAV
and other less popular formats supported by libsndfile. It has 
all functions one may expect from simple audio player. Now it supports
net streams (shoutcast, icecast, regular HTTP, FTP) also.

%description -l pl
MOC to konsolowy odtwarzacz audio z prostym interfejsem budz±cym
skojarzenia z playmp3list. Obs³uguje formaty MP3, Ogg, FLAC, 
Musepack, Speex, WAV oraz inne mniej popularne formaty wspierane przez
bibliotekê libsndfile. Ma wszystkie funkcje, których mo¿na spodziewaæ
siê w prostym odtwarzaczu audio. Teraz tak¿e obs³uguje strumienie
sieciowe (shoutcast, icecast, HTTP, FTP).

%prep
%setup -q

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

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

rm $RPM_BUILD_ROOT%{_docdir}/%{name}/*
rm -f $RPM_BUILD_ROOT%{_libdir}/moc/decoder_plugins/lib*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO NEWS AUTHORS THANKS *.example
%attr(755,root,root) %{_bindir}/*
%dir %{_libdir}/moc
%dir %{_libdir}/moc/decoder_plugins
%attr(755,root,root) %{_libdir}/moc/decoder_plugins/lib*.so
%{_datadir}/%{name}
%{_mandir}/man8/mocp*
