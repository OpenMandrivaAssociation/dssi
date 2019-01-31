Summary:	Disposable Soft Synth Interface examples and utilities
Name:		dssi
Version:	1.1.1
Release:	16
License:	LGPLv2+
Group:		Sound
Url:		http://dssi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.gz
Source1:	dssi.sh.bz2
Source2:	dssi.csh.bz2
BuildRequires:	ladspa-devel
#BuildRequires:	qt4-devel
BuildRequires:	pkgconfig(alsa)
BuildRequires:	pkgconfig(jack)
BuildRequires:	pkgconfig(liblo)
BuildRequires:	pkgconfig(samplerate)
BuildRequires:  pkgconfig(sndfile)

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
%configure
%make_build

%install
%make_install

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/profile.d/dssi.sh
bzcat %{SOURCE2} > %{buildroot}%{_sysconfdir}/profile.d/dssi.csh
perl -pi -e "s!__LIBDIR__!%{_libdir}!" %{buildroot}%{_sysconfdir}/profile.d/dssi*sh

%files
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
#{_libdir}/dssi/less_trivial_synth/LTS_*
#{_libdir}/dssi/trivial_sampler/trivial_sampler_*
%{_mandir}/man1/dssi_osc_send.1*
%{_mandir}/man1/dssi_osc_update.1*
%{_mandir}/man1/jack-dssi-host.1*
%{_mandir}/man1/dssi_analyse_plugin.1*
%{_mandir}/man1/dssi_list_plugins.1*
%config(noreplace) %attr(644,root,root) %{_sysconfdir}/profile.d/dssi*sh

%files devel
%doc doc/TODO doc/*.txt
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/dssi.pc
