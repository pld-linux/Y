Summary:	Y Windows - modern windowing system
Summary(pl.UTF-8):   Y Windows - nowoczesny system okienkowy
Name:		Y
Version:	0.2
Release:	0.1
License:	LGPL (communication libraries), CPL (yiterm), GPL (the rest)
Group:		Libraries
Source0:	http://www.efaref.net/arch/2004/Y/Y--devel/Y--devel--0.2/patch-1/Y--devel--0.2--patch-1.tar.gz
# Source0-md5:	30bce6027bcb36b39fc89d8cff98e2b0
Patch0:		%{name}-make.patch
Patch1:		%{name}-clients.patch
URL:		http://www.y-windows.org/
BuildRequires:	SDL-devel >= 1.2.0
BuildRequires:	autoconf >= 2.53
BuildRequires:	automake >= 1:1.7
BuildRequires:	freetype-devel >= 2.1.3
BuildRequires:	libiterm-devel >= 0.5
BuildRequires:	libsigc++1-devel >= 1.0.0
BuildRequires:	libtool >= 2:1.5
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Y is an implementation of a modern windowing system. The Y design has
the following features:
- network transparency
- modularity
- in-server implementation of widgets
- consistency and themeability
- support for hardware acceleration
- better internationalization, localization and accessibility.

%description -l pl.UTF-8
Y to implementacja nowoczesnego systemu okienkowe. Projekt Y ma
następujące cechy:
- przezroczystość względem sieci
- modularność
- implementacja widgetów w serwerze
- spójność i możliwość używania motywów
- obsługa akceleracji sprzętowej
- lepsze umiędzynarodowienie, lokalizacja i ułatwienia dostępu.

%package devel
Summary:	Header files for Y Windows libraries
Summary(pl.UTF-8):   Pliki nagłówkowe bibliotek Y Windows
License:	LGPL
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
# for libY++: libsigc++1-devel

%description devel
Header files for Y Windows libraries.

%description devel -l pl.UTF-8
Pliki nagłówkowe bibliotek Y Windows.

%package static
Summary:	Static Y Windows libraries
Summary(pl.UTF-8):   Statyczne biblioteki Y Windows
License:	LGPL
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static Y Windows libraries.

%description static -l pl.UTF-8
Statyczne biblioteki Y Windows.

%package utils
Summary:	Y Windows utilities
Summary(pl.UTF-8):   Programy użytkowe Y Windows
License:	CPL (yiterm), GPL (the rest)
Group:		Applications
Requires:	%{name} = %{version}-%{release}

%description utils
Y Windows utilities.

%description utils -l pl.UTF-8
Programy użytkowe Y Windows.

%prep
%setup -q -n Y--devel--0.2--patch-1
%patch0 -p1
%patch1 -p1

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -f $RPM_BUILD_ROOT%{_libdir}/Y/{*,*/*}/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
# COPYING contains only notes which part is on which license
%doc AUTHORS COPYING ChangeLog TODO
# communication libs
%attr(755,root,root) %{_libdir}/lib*.so.*.*.*

# Y server
%attr(755,root,root) %{_bindir}/Y
%attr(755,root,root) %{_bindir}/startY
%dir %{_libdir}/Y
%dir %{_libdir}/Y/driver
%dir %{_libdir}/Y/driver/input
%attr(755,root,root) %{_libdir}/Y/driver/input/*.so
%dir %{_libdir}/Y/driver/ipc
%attr(755,root,root) %{_libdir}/Y/driver/ipc/*.so
%dir %{_libdir}/Y/driver/video
%attr(755,root,root) %{_libdir}/Y/driver/video/fbdev.so
%dir %{_libdir}/Y/theme
%attr(755,root,root) %{_libdir}/Y/theme/*.so
%dir %{_libdir}/Y/wm
%attr(755,root,root) %{_libdir}/Y/wm/*.so
%{_sysconfdir}/Y

# driver-sdl
%attr(755,root,root) %{_libdir}/Y/driver/video/sdl.so

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/*.la
%{_includedir}/Y

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%files utils
%defattr(644,root,root,755)
%doc COPYING.CPL
%attr(755,root,root) %{_bindir}/y*
