
# I know, console<->terminal
Summary:	Console audio player with simple ncurses interface
Summary(pl):	Konsolowy odtwarzacz audio z prostym interfejsem ncurses
Name:		moc
Version:	2.2.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.daper.net/pub/soft/moc/stable/%{name}-%{version}.tar.gz
# Source0-md5:	992f64aee3a2bba83ee15b834bd796fb
Patch0:		%{name}-ncurses.patch
URL:		http://moc.daper.net/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	flac-devel
BuildRequires:	libao-devel
BuildRequires:	libid3tag-devel
BuildRequires:	libmad-devel
BuildRequires:	libsndfile-devel
BuildRequires:	libvorbis-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MOC is a console audio player with simple ncurses interface in
playmp3list style. It supports MP3, Ogg and WAV formats. It has all
functions one may expect from simple audio player

%description -l pl
MOC to konsolowy odtwarzacz audio z prostym interfejsem budz±cym
skojarzenia z playmp3list. Obs³uguje formaty MP3, Ogg oraz WAV. Ma
wszystkie funkcje, których spodziewa³by¶ siê w prostym odtwarzaczu
audio.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%{__aclocal} -I m4
%{__autoconf}
%{__automake}
%configure \
 	--disable-version-checker \
	--disable-debug

%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO NEWS AUTHORS THANKS *.example
%attr(755,root,root) %{_bindir}/*
%{_datadir}/%{name}
%{_mandir}/man8/mocp*
