%define modname	Parse-RecDescent
%define modver 1.967009

Summary:	A recursive descent parser generator for Perl
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	6
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Parse/Parse-RecDescent-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel

%description
The Parse::RecDescent perl module is used to generate recursive descent
parsers from powerful grammar specifications.

%prep
%setup -qn %{modname}-%{modver}
%__perl -p -i -e 's|#!.*/usr/local/bin/perl|#!/usr/bin/perl|' `find . -name '*.pl'`
find -type f | xargs chmod 644

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

# now in perl
rm -f %{buildroot}%{_mandir}/*/Text*

%files
%doc README Changes tutorial/*
%{perl_vendorlib}/Parse
%{_mandir}/man3/*


