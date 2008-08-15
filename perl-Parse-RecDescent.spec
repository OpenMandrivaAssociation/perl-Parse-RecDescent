%define module Parse-RecDescent
%define name perl-%{module}

Name:		%{name}
Version:	1.95.1
Release:	%mkrel 1
Summary:	A recursive descent parser generator for Perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:     http://www.cpan.org/modules/by-module/Parse/%{module}-v%{version}.tar.gz
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}

%description
The Parse::RecDescent perl module is used to generate recursive descent
parsers from powerful grammar specifications.

%prep
%setup -q -n %{module}-v%{version}
%{__perl} -p -i -e 's|#!.*/usr/local/bin/perl|#!/usr/bin/perl|' `find . -name '*.pl'`
find -type f | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %{buildroot}
%makeinstall_std

# now in perl
rm -f %{buildroot}%{_mandir}/*/Text*

%clean 
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README Changes tutorial/*
%{perl_vendorlib}/Parse
%{_mandir}/*/*
