Summary:	SKK like Japanese-input application
Summary(pl):	Aplikacja do wprowadzania znak�w japo�skich w stylu SKK
Name:		skkinput
Version:	3.0.6
Release:	1
License:	GPL
Group:		X11/Applications
#Source0Download: http://www.tatari-sakamoto.jp/~tatari/skkinput3.jis.html
Source0:	http://member.nifty.ne.jp/Tatari_SAKAMOTO/arc/%{name}-%{version}.tar.gz
# Source0-md5:	96b4a37e71bb415b6fced59bbc02372e
Source1:	%{name}.1x
Patch0:		%{name}-fontset.patch
URL:		http://www.tatari-sakamoto.jp/~tatari/skkinput3.jis.html
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_appdefsdir	/usr/X11R6/lib/X11/app-defaults

%description
skkinput is a kana to kanji converter with kinput protocol, kinput2
protocol, Ximp Protocol, X Input Method (X11R6 standard) under X
Window System.

%description -l pl
skkinput jest konwerterem kana do kanji z protoko�ami kinput, kinput2,
Ximp oraz standardow� metod� wprowadzania pod X11R6.

%prep
%setup -q
%patch0 -p1

%build
xmkmf -a
%{__make} \
	CC="%{__cc}" \
	CDEBUGFLAGS="%{rpmcflags}" \
	ELISP_DIR=%{_datadir}/skkinput

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	BINDIR=%{_bindir} \
	MANDIR=%{_mandir}/ja/man1 \
	ELISP_DIR=%{_datadir}/skkinput

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -fr $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc dot.skkinput
%lang(ja) %doc ChangeLog README-lisp.jis README.jis 
%attr(755,root,root) %{_bindir}/*
%{_datadir}/skkinput
%{_appdefsdir}/Skkinput
%{_mandir}/man1/*
# empty
#%lang(ja) %{_mandir}/ja/man1/*
