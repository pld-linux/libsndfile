Summary:	C library for reading and writing files containing sampled sound
Summary:	Biblioteka obs³ugi plików d¼wiêkowych
Name:		libsndfile
Version:	0.0.20
Release:	1
License:	GPL
Group:		Development/Libraries
Group(fr):	Development/Librairies
Vendor:		Erik de Castro Lopo <erikd@zip.com.au>
Source0:	http://www.zip.com.au/~erikd/libsndfile/%{name}-%{version}.tar.gz
Patch0:		libsndfile-autoconf.patch
URL:		http://www.zip.com.au/~erikd/libsndfile/
BuildRequires:	autoconf
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%description -l pl
Libsndfile to bibliotek± napisan± w C, s³u¿±ca do czytania i
zapisywania plików zawieraj±cych zsamplowany d¼wiêk (np. w formacie MS
Windows WAV czy Apple/SGI AIFF) poprzez jednolity, standardowy
interfejs.

%package devel
Summary:	libsndfile header files and development documentation
Summary(pl):	Pliki nag³ówkowe oraz dokumentacja do libsndfile
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libsndfile.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki libsndfile.

%package static
Summary:	libsndfile static libraries
Summary(pl):	Biblioteki statyczne libsndfile
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
libsndfile static libraries.

%description static -l pl
Biblioteki statyczne libsndfile.

%prep
%setup -q
%patch -p1

%build
aclocal
autoconf
LDFLAGS="-s"; export LDFLAGS
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_applnkdir}/Multimedia,%{_datadir}/pixmaps}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc {NEWS,TODO}.gz doc/*.html doc/*.jpg
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
