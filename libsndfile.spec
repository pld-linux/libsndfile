Summary:	C library for reading and writing files containing sampled sound
Summary:	Biblioteka obs³ugi plików d¼wiêkowych
Name:		libsndfile
Version:	1.0.1
Release:	2
License:	GPL
Vendor:		Erik de Castro Lopo <erikd@zip.com.au>
Group:		Development/Libraries
Source0:	http://www.zip.com.au/~erikd/libsndfile/%{name}-%{version}.tar.gz
Patch0:		%{name}-amfix.patch
URL:		http://www.zip.com.au/~erikd/libsndfile/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
Obsoletes:	libsndfile1

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
Requires:	%{name} = %{version}
Obsoletes:	libsndfile1-devel

%description devel
Header files and development documentation for libsndfile.

%description devel -l pl
Pliki nag³ówkowe oraz dokumentacja do biblioteki libsndfile.

%package static
Summary:	libsndfile static libraries
Summary(pl):	Biblioteki statyczne libsndfile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
libsndfile static libraries.

%description static -l pl
Biblioteki statyczne libsndfile.

%package octave
Summary:	libsndfile modules for octave
Summary(pl):	modu³y libsndfile dla octave
Group:		Applications/Math
Requires:	%{name}
Requires:	octave

%description octave
A couple of script files for loading, saving, and playing sound
files from within Octave.

%description octave -l pl
Kilka skryptów Octave do ³adowania, zapisywania i odtwarzania plików
d¼wiêkowych.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc NEWS TODO
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%attr(744,root,root) %{_bindir}/*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%{_includedir}/*
%{_pkgconfigdir}/*.pc

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a

%files octave
%defattr(644,root,root,755)
%{_datadir}/octave/site/m/*
