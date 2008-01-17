%define name perl-Parse-RecDescent
%define real_name Parse-RecDescent

Summary:	A recursive descent parser generator for Perl
Name:		%{name}
Version:	1.94
Release:	%mkrel 8
License:	GPL or Artistic
Group:		Development/Perl
Source0:	ftp://ftp.pasteur.fr/pub/computing/CPAN/modules/by-module/Parse/%{real_name}-%{version}.tar.bz2
Url:		http://search.cpan.org/dist/%{real_name}/
BuildRequires:	perl-devel
BuildArch:	noarch
Requires:	perl
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot

%description
The Parse::RecDescent perl module is used to generate recursive descent
parsers from powerful grammar specifications.

%prep

%setup -q -n %{real_name}-%{version}
%{__perl} -p -i -e 's|#!.*/usr/local/bin/perl|#!/usr/bin/perl|' `find . -name '*.pl'`
find -type f | xargs chmod 644

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

# now in perl
rm -f $RPM_BUILD_ROOT%{_mandir}/*/Text*

%clean 
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%doc README Changes tutorial/*
%{perl_vendorlib}/Parse
%{_mandir}/*/*
