%define modname	Parse-RecDescent

Summary:	A recursive descent parser generator for Perl
Name:		perl-%{modname}
Version:	1.967015
Release:	2
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	http://www.cpan.org/modules/by-module/Parse/Parse-RecDescent-%{version}.tar.gz
BuildArch:	noarch
BuildRequires:	perl(Text::Balanced)
BuildRequires:	perl(Test::More)
BuildRequires:	perl-devel

%description
The Parse::RecDescent perl module is used to generate recursive descent
parsers from powerful grammar specifications.

%prep
%autosetup -p1 -n %{modname}-%{version}
perl -p -i -e 's|#!.*/usr/local/bin/perl|#!/usr/bin/perl|' `find . -name '*.pl'`
find -type f | xargs chmod 644
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

# now in perl
rm -f %{buildroot}%{_mandir}/*/Text*

%files
%doc README Changes tutorial/*
%{perl_vendorlib}/Parse
%{_mandir}/man3/*
