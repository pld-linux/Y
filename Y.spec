Summary:	Y Windows
Summary(pl):	Y Windows
Name:		Y
Version:	0.2
Release:	0.1
License:	GPL
Group:		X
Group(pl):	X
Source0:	http://www.efaref.net/arch/2004/Y/Y--devel/Y--devel--0.2/patch-1/Y--devel--0.2--patch-1.tar.gz
# Source0-md5:	30bce6027bcb36b39fc89d8cff98e2b0
BuildRequires:	freetype-devel
BuildRequires:	SDL-devel
BuildRequires:	libsigc++1-devel
#Requires:
URL:		http://www.y-windows.org/	
Buildroot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
- -- empty --

%description -l pl
- -- pusty --

%package devel
Summary:	devel
Group:		X
Requires:	%{name} = %{version}
%description devel
- -- empty --

%description devel -l pl
- -- pusty --

%package static
Summary:	static
Group:		X
Requires:	%{name}-devel = %{version}
%description static
- -- empty --

%description static -l pl
- -- pusty --

%package utils
Summary:	utils
Group:		X
Requires:	%{name} = %{version}
%description utils
- -- empty --

%description utils -l pl
- -- pusty --

%prep
%setup -q -n Y--devel--0.2--patch-1

#%patch

%build
./autogen.sh
%configure \
	--disable-yiterm
%{__make} RPM_OPT_FLAGS="$RPM_OPT_FLAGS"

%install
rm -rf $RPM_BUILD_ROOT
%{__make} DESTDIR=$RPM_BUILD_ROOT install

%post
/sbin/ldconfig

%postun
/sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc
%{_sysconfdir}/Y
%{_bindir}/Y
%{_bindir}/startY
%{_libdir}/*.la
%{_libdir}/Y
%{_libdir}/*.so.0.0.0

%files devel
%defattr(644,root,root,755)
%doc
%{_includedir}/Y

%files static
%defattr(644,root,root,755)
%doc
%{_libdir}/*.a

%files utils
%defattr(644,root,root,755)
%doc
%{_bindir}/y*
