#
# Conditional build:
# _without_tests - do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Math
%define		pnam	Interpolate
Summary:	Math::Interpolate Perl module - interpolating data sets
Summary(pl):	Modu� Perla Math::Interpolate - interpolacja zbior�w danych
Name:		perl-Math-Interpolate
Version:	1.05
Release:	1
License:	unknown
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is the Math::Interpolate package. This module contains several
useful routines for interpolating data sets and finding where a given
value lies in a sorted list.

%description -l pl
Modu� Math::Interpolate zawiera funkcje przydatne do interpolacji
zbior�w danych i znajdywania, gdzie dana warto�� le�y na posortowanej
li�cie.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
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
%{perl_sitelib}/Math/*.pm
%{_mandir}/man3/*
