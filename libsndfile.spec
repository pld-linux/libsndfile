Summary:	C library for reading and writing files containing sampled sound
Summary(pl):	Biblioteka obs�ugi plik�w d�wi�kowych
Name:		libsndfile
Version:	1.0.15
Release:	1
License:	LGPL v2.1+
Vendor:		Erik de Castro Lopo <erikd@zip.com.au>
Group:		Development/Libraries
Source0:	http://www.mega-nerd.com/libsndfile/%{name}-%{version}.tar.gz
# Source0-md5:	4171faabfad0ce550cbe9bf1b065e976
URL:		http://www.mega-nerd.com/libsndfile/
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.1
BuildRequires:	libtool
Obsoletes:	libsndfile1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%description -l pl
Libsndfile to bibliotek� napisan� w C, s�u��ca do czytania i
zapisywania plik�w zawieraj�cych zsamplowany d�wi�k (np. w formacie MS
Windows WAV czy Apple/SGI AIFF) poprzez jednolity, standardowy
interfejs.

%package devel
Summary:	libsndfile header files and development documentation
Summary(pl):	Pliki nag��wkowe oraz dokumentacja do libsndfile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	flac-devel >= 1.1.1
Obsoletes:	libsndfile1-devel

%description devel
Header files and development documentation for libsndfile.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki libsndfile.

%package static
Summary:	libsndfile static libraries
Summary(pl):	Biblioteki statyczne libsndfile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsndfile static libraries.

%description static -l pl
Biblioteki statyczne libsndfile.

%package octave
Summary:	libsndfile modules for octave
Summary(pl):	Modu�y libsndfile dla octave
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave

%description octave
A couple of script files for loading, saving, and playing sound files
from within Octave.

%description octave -l pl
Kilka skrypt�w Octave do �adowania, zapisywania i odtwarzania plik�w
d�wi�kowych.

%prep
%setup -q

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

rm -rf $RPM_BUILD_ROOT%{_docdir}/libsndfile1-dev

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README TODO
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so.*.*
%{_mandir}/man1/*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/new_file_type.HOWTO
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
