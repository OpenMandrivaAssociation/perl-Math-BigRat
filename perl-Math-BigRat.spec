%define debug_package %{nil}

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

