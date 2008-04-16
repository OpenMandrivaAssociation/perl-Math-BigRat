%define module  Math-BigRat
%define name    perl-%{module}
%define version 0.22
%define release %mkrel 1

Name:           %{name}
Version:        %{version}
Release:        %{release}
Summary:        Arbitrary big rational numbers
License:        GPL or Artistic
Group:          Development/Perl
Url:            http://search.cpan.org/dist/%{module}
Source:         http://www.cpan.org/modules/by-module/Math/%{module}-%{version}.tar.gz
# automatic dependency doesn't work here, because perl package
# provides an unversioned one
BuildRequires:	perl-Math-BigInt >= 1.87
BuildRoot:      %{_tmppath}/%{name}-%{version}

%description
Math::BigRat complements Math::BigInt and Math::BigFloat by providing support
for arbitrary big rational numbers.

%prep
%setup -q -n %{module}-%{version}

%build
export PERL5LIB=%{perl_vendorlib}
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
export PERL5LIB=%{perl_vendorlib}/
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Math
%{_mandir}/*/*

