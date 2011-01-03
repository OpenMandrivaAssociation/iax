%define	major 0
%define libname	%mklibname iax %{major}
%define develname %mklibname -d iax

Summary:	IAX (Inter Asterisk eXchange) Library
Name:		iax
Version:	0.2.3
Release:	%mkrel 14
License:	LGPL
Group:		System/Libraries
URL:		http://www.asterisk.org/
Source0:	libiax2-0.2.3-20060212.tar.bz2
Patch0:		libiax2.diff
Patch1:		libiax2-fix-str-fmt.patch
Patch2:		libiax2-install.patch
%if %mdkversion >= 1020
BuildRequires:	multiarch-utils >= 1.0.3
%endif
BuildRoot:	%{_tmppath}/%{name}-%{version}-root

%description
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks),
is the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a
high performance, feature rich protocol unrelated to SIP or H.323.

Its single-socket design allows it to interoperate with NAT and
PAT masquerade firewalls.  It supports internationalization,
remote dialplans, and voice, HTML, image, DTMF, and video content.

For more information see http://www.gnophone.com

%package -n	%{libname}
Summary:	IAX (Inter Asterisk eXchange) Library
Group:          System/Libraries

%description -n	%{libname}
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks),
is the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a
high performance, feature rich protocol unrelated to SIP or H.323.

Its single-socket design allows it to interoperate with NAT and
PAT masquerade firewalls.  It supports internationalization,
remote dialplans, and voice, HTML, image, DTMF, and video content.

For more information see http://www.gnophone.com

%package -n	%{develname}
Summary:	IAX (Inter Asterisk eXchange) Development Package
Group:		Development/C
Provides:	%{name}-devel = %{version}
Provides:	lib%{name}-devel = %{version}
Requires:	%{libname} = %{version}
Obsoletes:	%{_lib}iax0-devel

%description -n	%{develname}
Inter Asterisk eXchange, lovingly called IAX (pronounced: eeks),
is the protocol used by the Asterisk PBX system for
inter-asterisk-communication. Other applications may use libiax to
communicate with each other and other asterisk servers. IAX is a
high performance, feature rich protocol unrelated to SIP or H.323.

Its single-socket design allows it to interoperate with NAT and
PAT masquerade firewalls.  It supports internationalization,
remote dialplans, and voice, HTML, image, DTMF, and video content.

For more information see http://www.gnophone.com

This package contains all of the development files that you will
need in order to compile IAX applications.

%prep

%setup -q -n libiax2
%patch0 -p1
%patch1 -p0
%patch2 -p0

# no debug...
find -type f -name "Makefile.am" | xargs perl -pi -e "s|-DDEBUG_SUPPORT||g"

%build
autoreconf -fi
%configure2_5x \
    --disable-extreme-debug
%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

# install _all_ headers...
install -m0644 src/*.h %{buildroot}%{_includedir}/iax/

%if %mdkversion >= 1020
%multiarch_binaries %{buildroot}%{_bindir}/iax-config
%endif

%if %mdkversion < 200900
%post -n %{libname} -p /sbin/ldconfig
%endif

%if %mdkversion < 200900
%postun -n %{libname} -p /sbin/ldconfig
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%if %mdkversion >= 1020
%multiarch %{multiarch_bindir}/iax-config
%endif
%{_bindir}/iax-config
%{_includedir}/iax
%{_libdir}/*.so
%{_libdir}/*.a
%{_libdir}/*.la
