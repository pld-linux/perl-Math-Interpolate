#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Interpolate
Summary:	Math::Interpolate Perl module - interpolating data sets
Summary(pl):	Modu³ Perla Math::Interpolate - interpolacja zbiorów danych
Name:		perl-Math-Interpolate
Version:	1.05
Release:	2
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	1826c6c24b75a2a27964c3dac198adac
BuildRequires:	perl-devel >= 5.6
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Math::Interpolate package. This module contains several
useful routines for interpolating data sets and finding where a given
value lies in a sorted list.

%description -l pl
Modu³ Math::Interpolate zawiera funkcje przydatne do interpolacji
zbiorów danych i znajdywania, gdzie dana warto¶æ le¿y na posortowanej
li¶cie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{!?_without_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README
%{perl_vendorlib}/Math/*.pm
%{_mandir}/man3/*
