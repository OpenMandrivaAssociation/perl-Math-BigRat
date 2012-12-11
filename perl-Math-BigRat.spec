%define upstream_name    Math-BigRat
%define upstream_version 0.2602

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	1

Summary:	Arbitrary big rational numbers
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Math/%{upstream_name}-%{upstream_version}.tar.gz

# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRequires:	perl-devel

%description
Math::BigRat complements Math::BigInt and Math::BigFloat by providing support
for arbitrary big rational numbers.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
export PERL5LIB=%{perl_vendorlib}
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
export PERL5LIB=%{perl_vendorlib}/
make test

%install
%makeinstall_std

%files 
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*


%changelog
* Sat Nov 13 2010 Jérôme Quelin <jquelin@mandriva.org> 0.260.0-1mdv2011.0
+ Revision: 597190
- update to 0.26

* Thu Sep 10 2009 Jérôme Quelin <jquelin@mandriva.org> 0.240.0-1mdv2011.0
+ Revision: 436571
- update to 0.24

* Wed Jul 29 2009 Jérôme Quelin <jquelin@mandriva.org> 0.220.0-1mdv2010.0
+ Revision: 403854
- rebuild using %%perl_convert_version

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 0.22-2mdv2009.0
+ Revision: 268613
- rebuild early 2009.0 package (before pixel changes)

* Wed Apr 16 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.22-1mdv2009.0
+ Revision: 194859
- update to new version 0.22
- update to new version 0.22

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.0
+ Revision: 78233
- import perl-Math-BigRat


* Sun Sep 02 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2008.0
- first mdv release
