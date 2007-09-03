#
# Conditional build:
%bcond_without	sqlite		# disable use of sqlite
%bcond_without	static_libs	# don't build static library
%bcond_without	tests		# don't build tests
#
Summary:	C library for reading and writing files containing sampled sound
Summary(pl.UTF-8):	Biblioteka obsługi plików dźwiękowych
Name:		libsndfile
Version:	1.0.17
Release:	3
License:	LGPL v2.1+
Vendor:		Erik de Castro Lopo <erikd@zip.com.au>
Group:		Development/Libraries
Source0:	http://www.mega-nerd.com/libsndfile/%{name}-%{version}.tar.gz
# Source0-md5:	2d126c35448503f6dbe33934d9581f6b
Patch0:		%{name}-flac.patch
URL:		http://www.mega-nerd.com/libsndfile/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.54
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.1.3
%{?with_tests:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
%{?with_sqlite:BuildRequires:	sqlite3-devel}
Obsoletes:	libsndfile1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Libsndfile is a C library for reading and writing files containing
sampled sound (such as MS Windows WAV and the Apple/SGI AIFF format)
through one standard library interface.

%description -l pl.UTF-8
Libsndfile to biblioteką napisaną w C, służąca do czytania i
zapisywania plików zawierających zsamplowany dźwięk (np. w formacie MS
Windows WAV czy Apple/SGI AIFF) poprzez jednolity, standardowy
interfejs.

%package devel
Summary:	libsndfile header files and development documentation
Summary(pl.UTF-8):	Pliki nagłówkowe oraz dokumentacja do libsndfile
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	flac-devel >= 1.1.1
Obsoletes:	libsndfile1-devel

%description devel
Header files and development documentation for libsndfile.

%description devel -l pl.UTF-8
Pliki nagłówkowe oraz dokumentacja do biblioteki libsndfile.

%package static
Summary:	libsndfile static libraries
Summary(pl.UTF-8):	Biblioteki statyczne libsndfile
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
libsndfile static libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libsndfile.

%package octave
Summary:	libsndfile modules for octave
Summary(pl.UTF-8):	Moduły libsndfile dla octave
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave

%description octave
A couple of script files for loading, saving, and playing sound files
from within Octave.

%description octave -l pl.UTF-8
Kilka skryptów Octave do ładowania, zapisywania i odtwarzania plików
dźwiękowych.

%prep
%setup -q
%patch0 -p1

%if %{without tests}
%{__sed} -i 's, tests$,,' Makefile.am
%endif

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure \
	%{!?with_static_libs:--disable-static} \
	%{!?with_sqlite:--disable-sqlite}

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
%attr(755,root,root) %{_bindir}/sndfile-*
%attr(755,root,root) %{_libdir}/libsndfile.so.*.*
%{_mandir}/man1/sndfile-*.1*

%files devel
%defattr(644,root,root,755)
%doc doc/*.html doc/*.jpg doc/new_file_type.HOWTO
%attr(755,root,root) %{_libdir}/libsndfile.so
%{_libdir}/libsndfile.la
%{_includedir}/sndfile.h*
%{_pkgconfigdir}/sndfile.pc

%if %{with static_libs}
%files static
%defattr(644,root,root,755)
%{_libdir}/libsndfile.a
%endif

%files octave
%defattr(644,root,root,755)
%{_datadir}/octave/site/m/*
