Summary:	SKK like Japanese-input application
Summary(pl):	Aplikacja do wprowadzania znaków japoñskich w stylu SKK
Name:		skkinput
Version:	2.03
Release:	5
License:	GPL
Group:		X11/Applications
Source0:	http://member.nifty.ne.jp/Tatari_SAKAMOTO/%{name}-%{version}.tar.gz
Source1:	%{name}.1x
Patch0:		%{name}-fontset.patch
URL:		http://member.nifty.ne.jp/Tatari_SAKAMOTO/
BuildRequires:	XFree86-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
skkinput is a kana to kanji converter with kinput protocol, kinput2
protocol, Ximp Protocol, X Input Method (X11R6 standard) under X
Window System.

%description -l pl
skkinput jest konwerterem kana do kanji z protoko³ami kinput, kinput2,
Ximp oraz standardow± metod± wprowadzania pod X11R6.

%prep
%setup -q
%patch -p1

%build
xmkmf -a
%{__make} CDEBUGFLAGS="%{rpmcflags}"

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install install.man \
	DESTDIR=$RPM_BUILD_ROOT \
	MANDIR=%{_mandir}/ja/man1

install -d $RPM_BUILD_ROOT%{_mandir}/man1
install %{SOURCE1} $RPM_BUILD_ROOT%{_mandir}/man1

%clean
rm -fr ${RPM_BUILD_ROOT}

%files
%defattr(644,root,root,755)
%lang(ja) %doc BUGS.jis CHANGES.jis FAQ.jis PROGRAM.jis README.jis TODO.jis skkinput.doc
%doc dot.skkinput
%attr(755,root,root) %{_bindir}/*
%{_libdir}/X11/app-defaults/Skkinput
%{_mandir}/man1/*
%lang(ja) %{_mandir}/ja/man1/*
