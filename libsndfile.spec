Summary:	C library for reading and writing files containing sampled sound
Summary:	Biblioteka obs�ugi plik�w d�wi�kowych
Name:		libsndfile
Version:	0.0.25
Release:	1
License:	GPL
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Vendor:		Erik de Castro Lopo <erikd@zip.com.au>
Source0:	http://www.zip.com.au/~erikd/libsndfile/%{name}-%{version}.tar.gz
Patch0:		%{name}-autoconf.patch
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
URL:		http://www.zip.com.au/~erikd/libsndfile/
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
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Header files and development documentation for libsndfile.

%description devel -l pl
Pliki nag��wkowe oraz dokumentacja do biblioteki libsndfile.

%package static
Summary:	libsndfile static libraries
Summary(pl):	Biblioteki statyczne libsndfile
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(fr):	Development/Librairies
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
libtoolize --copy --force
aclocal
autoconf
rm -f missing
automake -a -c
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf NEWS TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc *.gz doc/*.html doc/*.jpg
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
