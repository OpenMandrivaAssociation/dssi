Summary:	Disposable Soft Synth Interface examples and utilities
Name:		dssi
Version:	1.1.1
Release:	1
License:	LGPLv2+
Group:		Sound
URL:		http://dssi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
Source1:	dssi.sh.bz2
Source2:	dssi.csh.bz2
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	jackit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:  pkgconfig(sndfile)
BuildRequires:	qt4-devel

%description
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

This package contains examples and utilities.

%package devel
Summary:	Disposable Soft Synth Interface API
Group:		Development/C
Requires:	%{name} = %{version}
Requires:	ladspa-devel
Requires:	libalsa-devel

%description devel
DSSI (pronounced "dizzy") is an API for audio plugins, with particular
application for software synthesis plugins with native user
interfaces. DSSI is an open specification developed for use in Linux
audio applications, although portable to other platforms. It may be
thought of as LADSPA-for-instruments, or something comparable to VSTi.

DSSI consists of a C language API for use by plugins and hosts, based
on the LADSPA API, and an OSC (Open Sound Control) API for use in user
interface to host communications. The DSSI specification consists of
an RFC which describes the background for the proposal and defines the
OSC part of the specification, and a documented header file which
defines the C API.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/profile.d/dssi.sh
bzcat %{SOURCE2} > %{buildroot}%{_sysconfdir}/profile.d/dssi.csh
perl -pi -e "s!__LIBDIR__!%{_libdir}!" %{buildroot}%{_sysconfdir}/profile.d/dssi*sh

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/jack-dssi-host
%{_bindir}/dssi_analyse_plugin
%{_bindir}/dssi_list_plugins
%{_bindir}/dssi_osc_send
%{_bindir}/dssi_osc_update
%{_bindir}/karplong
%{_bindir}/less_trivial_synth
%{_bindir}/trivial_sampler
%{_bindir}/trivial_synth
%{_libdir}/dssi/*.so
%{_libdir}/dssi/less_trivial_synth/LTS_*
%{_libdir}/dssi/trivial_sampler/trivial_sampler_*
%{_mandir}/man1/dssi_osc_send.1*
%{_mandir}/man1/dssi_osc_update.1*
%{_mandir}/man1/jack-dssi-host.1*
%{_mandir}/man1/dssi_analyse_plugin.1*
%{_mandir}/man1/dssi_list_plugins.1*
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/profile.d/dssi*sh

%files devel
%defattr(-,root,root)
%doc doc/TODO doc/*.txt
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/dssi.pc


%changelog
* Tue May 03 2011 Oden Eriksson <oeriksson@mandriva.com> 1.1.0-2
+ Revision: 663887
- mass rebuild

* Sun Sep 19 2010 Frank Kober <emuse@mandriva.org> 1.1.0-1mdv2011.0
+ Revision: 579878
- new version 1.1.0 (finally removing qt3 dependencies)
  o adjust file list
  o respect qt4 port

* Sat Jan 02 2010 Jérôme Brenier <incubusss@mandriva.org> 1.0.0-3mdv2010.1
+ Revision: 485088
- re-enable libtoolize to fix build

* Sun Jun 07 2009 Nicolas Lécureuil <nlecureuil@mandriva.com> 1.0.0-2mdv2010.0
+ Revision: 383460
- Rebuild against latest liblo

* Sun Mar 22 2009 Herton Ronaldo Krzesinski <herton@mandriva.com.br> 1.0.0-1mdv2009.1
+ Revision: 360224
- Updated to version 1.0.0
- Dropped dssi-0.9.1-gcc43.patch (merged)

* Tue Dec 09 2008 Adam Williamson <awilliamson@mandriva.org> 0.9.1-11mdv2009.1
+ Revision: 312082
- rebuild
- add gcc43.patch: fix build with GCC 4.3 (missing #include)
- add qt3test.patch: hack up the qt3 test to work with our moved libs

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Tomasz Pawel Gajc <tpg@mandriva.org>
    - remove re-defines
    - spec file clean

* Sat Jan 12 2008 Thierry Vignaud <tv@mandriva.org> 0.9.1-10mdv2008.1
+ Revision: 149679
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Wed Sep 19 2007 Adam Williamson <awilliamson@mandriva.org> 0.9.1-9mdv2008.0
+ Revision: 90136
- rebuild for 2008
- new license policy

* Sat Sep 08 2007 Emmanuel Andry <eandry@mandriva.org> 0.9.1-8mdv2008.0
+ Revision: 82486
- rebuild for 2008.0


* Sun Feb 18 2007 Christiaan Welvaart <cjw@daneel.dyndns.org>
+ 2007-02-18 18:29:29 (122506)
- rebuild to fix libflac dep for ppc

* Sun Jan 28 2007 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.9.1-6mdv2007.1
+ 2007-01-28 23:31:28 (114716)
- rebuild for new flac
- Import dssi

* Tue Aug 15 2006 Götz Waschk <waschk@mandriva.org> 0.9.1-5mdv2007.0
- fix devel deps

* Fri May 12 2006 Pedro Lopez-Cabanillas <plcl@users.sf.net> 0.9.1-4mdk
- add missing BuildRequires qt3-devel
- add missing Requires ladspa-devel for devel package

* Mon Apr 03 2006 Pedro Lopez-Cabanillas <plcl@users.sf.net> 0.9.1-3mdk
- environment profile scripts

* Sun Apr 02 2006 Austin Acton <austin@mandriva.org> 0.9.1-2mdk
- libtoolize hack easier than autoreconf

* Wed Mar 29 2006 Austin Acton <austin@mandriva.org> 0.9.1-1mdk
- adapt spec from Pedro Lopez-Cabanillas <plcl@users.sourceforge.net>
- initial package

