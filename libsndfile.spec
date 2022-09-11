# TODO:
#	- who needs sndfile-regtest?
#
# Conditional build:
%bcond_with	regtest		# build sndfile-regtest program
%bcond_without	octave		# don't build octave binding
%bcond_without	static_libs	# don't build static library
%bcond_without	tests		# don't build tests
#
Summary:	C library for reading and writing files containing sampled sound
Summary(pl.UTF-8):	Biblioteka obsługi plików dźwiękowych
Name:		libsndfile
Version:	1.0.28
Release:	2
License:	LGPL v2.1+
Group:		Libraries
Source0:	http://www.mega-nerd.com/libsndfile/files/%{name}-%{version}.tar.gz
# Source0-md5:	646b5f98ce89ac60cdb060fcd398247c
Patch0:		octave32.patch
URL:		http://www.mega-nerd.com/libsndfile/
BuildRequires:	alsa-lib-devel
BuildRequires:	autoconf >= 2.57
BuildRequires:	automake
BuildRequires:	flac-devel >= 1.3.1
BuildRequires:	gcc-fortran
BuildRequires:	libogg-devel >= 2:1.1.3
%{?with_tests:BuildRequires:	libstdc++-devel}
BuildRequires:	libtool >= 2:2
BuildRequires:	libvorbis-devel >= 1:1.2.3
%{?with_octave:BuildRequires:	octave-devel >= 2:3}
BuildRequires:	pkgconfig
BuildRequires:	sed >= 4.0
%{?with_regtest:BuildRequires:	sqlite3-devel >= 3.2}
Requires:	flac >= 1.3.1
Requires:	libogg >= 2:1.1.3
Requires:	libvorbis >= 1:1.2.3
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
Requires:	flac-devel >= 1.3.1
Requires:	libogg-devel >= 2:1.1.3
Requires:	libvorbis-devel >= 1:1.2.3
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

%package progs
Summary:	libsndfile utility programs
Summary(pl.UTF-8):	Narzędzia korzystające z biblioteki libsndfile
Group:		Applications/Sound
Requires:	%{name} = %{version}-%{release}

%description progs
libsndfile utility programs:
- sndfile-convert - convert a sound files from one format to another
- sndfile-info - display information about a sound file
- sndfile-play - play a sound file

%description progs -l pl.UTF-8
Narzędzia z biblioteki libsndfile:
- sndfile-convert - kowertertuje pliki dźwiękowe
- sndfile-info - wyświetla informacje o pliku dźwiękowym
- sndfile-play - odtwarza pliki dźwiękowe

%package -n octave-sndfile
Summary:	sndfile module for Octave
Summary(pl.UTF-8):	Moduł sndfile dla Octave
Group:		Applications/Math
Requires:	%{name} = %{version}-%{release}
Requires:	octave >= 2:3
Obsoletes:	libsndfile-octave

%description -n octave-sndfile
A couple of script files for loading, saving, and playing sound files
from within Octave.

%description -n octave-sndfile -l pl.UTF-8
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
%{__aclocal} -I M4
%{__autoconf}
%{__automake}
%configure \
	%{!?with_octave:--disable-octave} \
	--disable-silent-rules \
	%{!?with_regtest:--disable-sqlite} \
	%{!?with_static_libs:--disable-static}

%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

# packaged as %doc
%{__rm} -r $RPM_BUILD_ROOT%{_docdir}/libsndfile

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/libsndfile.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libsndfile.so.1

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

%files progs
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/sndfile-*
%{_mandir}/man1/sndfile-*.1*

%if %{with octave}
%files -n octave-sndfile
%defattr(644,root,root,755)
%{_datadir}/octave/site/m/sndfile_*.m
%dir %{_libdir}/octave/*/site/oct/*/sndfile
%{_libdir}/octave/*/site/oct/*/sndfile/PKG_ADD
%attr(755,root,root) %{_libdir}/octave/*/site/oct/*/sndfile/sndfile.oct
%endif
