
# I know, console<->terminal
Summary:	Console audio player with simple ncurses interface
Summary(pl):	Konsolowy odtwarzacz audio z prostym interfejsem ncurses
Name:		moc
Version:	1.1.0
Release:	1
License:	GPL
Group:		Applications/Sound
Source0:	ftp://ftp.daper.net/pub/soft/moc/%{name}-%{version}.tar.gz
Patch0:		%{name}-ncurses.patch
URL:		http://moc.daper.net
BuildRequires:	libao-devel
BuildRequires:	libvorbis-devel
BuildRequires:	mad-devel
BuildRequires:	ncurses-devel
BuildRequires:	zlib-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MOC is a console audio player with simple ncurses interface in
playmp3list style. It supports MP3, OGG and WAV formats. It has all
functions one may expect from simple audio player

%description -l pl
MOC to konsolowy odtwarzacz audio z prostym interfejsem budz±cym
skojarzenia z playmp3list. Obs³uguje formaty MP3, OGG oraz WAV. Ma
wszystkie funkcje, których spodziewa³by¶ siê w prostym odtwarzaczu
audio.

%prep
%setup -q
%patch0 -p1

%build
CFLAGS="-I/usr/include/ncurses %{rpmcflags}"

%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	--disable-version-checker
%{__make}
	
%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc ChangeLog README TODO NEWS AUTHORS
%attr(755,root,root) %{_bindir}/*
