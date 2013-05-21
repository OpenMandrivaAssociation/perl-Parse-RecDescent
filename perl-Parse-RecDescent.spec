%define upstream_name    Parse-RecDescent
%define upstream_version 1.965001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6

Summary:	A recursive descent parser generator for Perl
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch:	noarch

%description
The Parse::RecDescent perl module is used to generate recursive descent
parsers from powerful grammar specifications.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
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
%{_mandir}/*/*


%changelog
* Sun Jan 22 2012 Oden Eriksson <oeriksson@mandriva.com> 1.965.1-4mdv2012.0
+ Revision: 765587
- rebuilt for perl-5.14.2

* Sat Jan 21 2012 Oden Eriksson <oeriksson@mandriva.com> 1.965.1-3
+ Revision: 764097
- rebuilt for perl-5.14.x

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.965.1-2
+ Revision: 667288
- mass rebuild

* Tue Apr 06 2010 Jérôme Quelin <jquelin@mandriva.org> 1.965.1-1mdv2011.0
+ Revision: 532155
- update to 1.965001

* Wed Feb 17 2010 Jérôme Quelin <jquelin@mandriva.org> 1.964.0-1mdv2010.1
+ Revision: 506943
- update to 1.964

* Thu Jan 21 2010 Jérôme Quelin <jquelin@mandriva.org> 1.963.0-1mdv2010.1
+ Revision: 494444
- update to 1.963

* Sat Aug 29 2009 Jérôme Quelin <jquelin@mandriva.org> 1.962.2-1mdv2010.0
+ Revision: 422082
- update to 1.962.2

* Fri Aug 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.962.1-1mdv2010.0
+ Revision: 421829
- update to 1.962.1

* Wed Aug 26 2009 Jérôme Quelin <jquelin@mandriva.org> 1.962.0-1mdv2010.0
+ Revision: 421386
- update to 1.962.0
- using %%perl_convert_version
- fixed license field

* Mon Feb 09 2009 Guillaume Rousse <guillomovitch@mandriva.org> 1.96.0-1mdv2009.1
+ Revision: 338703
- new version

* Fri Aug 15 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.95.1-1mdv2009.0
+ Revision: 272297
- new version

* Wed Jun 18 2008 Thierry Vignaud <tv@mandriva.org> 1.94-9mdv2009.0
+ Revision: 223951
- rebuild

* Thu Jan 17 2008 Oden Eriksson <oeriksson@mandriva.com> 1.94-8mdv2008.1
+ Revision: 154208
- rebuild

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 1.94-7mdv2008.0
+ Revision: 67515
- rebuild


* Sun Jan 14 2007 Olivier Thauvin <nanardon@mandriva.org> 1.94-6mdv2007.0
+ Revision: 108468
- rebuild

  + Guillaume Rousse <guillomovitch@mandriva.org>
    - Import perl-Parse-RecDescent

* Tue Oct 11 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.94-5mdk
- Rebuild, fix permissions, change summary

* Tue Aug 10 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.94-4mdk
- Rebuild for new perl
- Fix description
- Include tutorial

