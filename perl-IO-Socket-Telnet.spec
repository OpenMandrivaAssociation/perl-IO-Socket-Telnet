%define upstream_name    IO-Socket-Telnet
%define upstream_version 0.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Transparent telnet negotiation for IO::Socket::INET
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/IO/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

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
%{__perl} Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes META.yml README
%{_mandir}/man3/*
%perl_vendorlib/*


