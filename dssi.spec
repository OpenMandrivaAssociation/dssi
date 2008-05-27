Summary:	Disposable Soft Synth Interface examples and utilities
Name:		dssi
Version:	0.9.1
Release:	%mkrel 11
License:	LGPLv2+
Group:		Sound
URL:		http://dssi.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/dssi/%{name}-%{version}.tar.bz2
Source1:	dssi.sh.bz2
Source2:	dssi.csh.bz2
BuildRequires:	ladspa-devel
BuildRequires:	liblo-devel
BuildRequires:	libalsa-devel
BuildRequires:	jackit-devel
BuildRequires:	libsamplerate-devel
BuildRequires:	libsndfile-devel
BuildRequires:	qt3-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

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
alias libtoolize=true
export QTDIR=/usr/lib/qt3
export PATH=/usr/lib/qt3/bin:$PATH
perl -pi -e 's/\$QTDIR\/lib/\$QTDIR\/%{_lib}/g' configure
perl -pi -e 's/\${QTDIR}\/lib/\${QTDIR}\/%{_lib}/g' configure
%configure2_5x
%make

%install
rm -rf %{buildroot}
%makeinstall_std

install -d -m 755 %{buildroot}%{_sysconfdir}/profile.d
bzcat %{SOURCE1} > %{buildroot}%{_sysconfdir}/profile.d/dssi.sh
bzcat %{SOURCE2} > %{buildroot}%{_sysconfdir}/profile.d/dssi.csh
perl -pi -e "s!__LIBDIR__!%{_libdir}!" %{buildroot}%{_sysconfdir}/profile.d/dssi*sh

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc ChangeLog README
%{_bindir}/jack-dssi-host
%{_bindir}/dssi_osc_send
%{_bindir}/dssi_osc_update
%{_bindir}/less_trivial_synth
%{_bindir}/trivial_sampler
%{_bindir}/trivial_synth
%{_libdir}/dssi/*.so
%{_libdir}/dssi/*.la
%{_libdir}/dssi/less_trivial_synth/LTS_*
%{_libdir}/dssi/trivial_sampler/trivial_sampler_*
%config(noreplace) %attr(755,root,root) %{_sysconfdir}/profile.d/dssi*sh

%files devel
%defattr(-,root,root)
%doc doc/TODO doc/*.txt doc/*.html
%{_includedir}/dssi.h
%{_libdir}/pkgconfig/dssi.pc
