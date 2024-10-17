%define	major 0
%define libname	%mklibname iax %{major}
%define develname %mklibname -d iax

Summary:	IAX (Inter Asterisk eXchange) Library
Name:		iax
Version:	0.2.3
Release:	16
License:	LGPL
Group:		System/Libraries
URL:		https://www.asterisk.org/
Source0:	libiax2-0.2.3-20060212.tar.bz2
Patch0:		libiax2.diff
Patch1:		libiax2-fix-str-fmt.patch
Patch2:		libiax2-install.patch
BuildRequires:	multiarch-utils >= 1.0.3

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
%makeinstall_std

# install _all_ headers...
install -m0644 src/*.h %{buildroot}%{_includedir}/iax/

%multiarch_binaries %{buildroot}%{_bindir}/iax-config

%files -n %{libname}
%defattr(-,root,root)
%doc ChangeLog NEWS README
%{_libdir}/*.so.%{major}
%{_libdir}/*.so.%{major}.*

%files -n %{develname}
%defattr(-,root,root)
%{multiarch_bindir}/iax-config
%{_bindir}/iax-config
%{_includedir}/iax
%{_libdir}/*.so
%{_libdir}/*.a


%changelog
* Mon Jan 03 2011 Funda Wang <fwang@mandriva.org> 0.2.3-14mdv2011.0
+ Revision: 627966
- fix build

  + Oden Eriksson <oeriksson@mandriva.com>
    - don't force the usage of automake1.7

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.2.3-12mdv2009.0
+ Revision: 247139
- rebuild

  + Pixel <pixel@mandriva.com>
    - do not call ldconfig in %%post/%%postun, it is now handled by filetriggers

* Wed Jan 02 2008 Olivier Blin <oblin@mandriva.com> 0.2.3-10mdv2008.1
+ Revision: 140755
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request
    - import iax


* Sun Sep 17 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-10mdv2007.0
- rebuild

* Sun Feb 12 2006 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-9mdk
- use a svn snap (r35)
- new P0

* Thu May 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-8mdk
- use new code from the iaxclient codebase

* Thu May 05 2005 Oden Eriksson <oeriksson@mandriva.com> 0.2.3-7mdk
- rebuilt with gcc4

* Sun Apr 10 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.2.3-6mdk
- use the %%mkrel macro
- added new jitterbuffer code from the iaxclient codebase
- revert latest "lib64 fixes"

* Mon Jan 31 2005 Oden Eriksson <oeriksson@mandrakesoft.com> 0.2.3-5mdk
- fix deps and conditional %%multiarch
- fix requires-on-release

* Tue Dec 28 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.2.3-4mdk
- lib64 fixes

* Fri Sep 10 2004 Oden Eriksson <oeriksson@mandrakesoft.com> 0.2.3-3mdk
- 0.2.3
- drop P0, it's included
- fix deps

* Thu Jul 10 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.2.2-3mdk
- rebuild

* Tue Jul 08 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.2.2-2mdk
- Copyright/License

* Tue Jul 08 2003 Oden Eriksson <oden.eriksson@kvikkjokk.net> 0.2.2-1mdk
- initial cooker contrib
- mandrakified the provided spec file
