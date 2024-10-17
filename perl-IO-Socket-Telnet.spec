%define upstream_name    IO-Socket-Telnet
%define upstream_version 0.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	5

Summary:	Transparent telnet negotiation for IO::Socket::INET
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildArch:	noarch

%description
Telnet is a simple protocol that sits on top of TCP/IP. It handles the
negotiation of various options, both about the connection itself (ECHO) and
the setup of both sides of the party (NAWS, TTYPE).

This is a wrapper around the IO::Socket::INET manpage that both strips out
the telnet escape sequences and lets you handle the negotiation in a
high-level manner.

There is currently no interface for defining callbacks. This will be
rectified very soon. The module as it stands is still useful for stripping
out telnet escape sequences.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.40.0-2mdv2011.0
+ Revision: 657782
- rebuild for updated spec-helper

* Sun Oct 03 2010 Shlomi Fish <shlomif@mandriva.org> 0.40.0-1mdv2011.0
+ Revision: 582694
- import perl-IO-Socket-Telnet

