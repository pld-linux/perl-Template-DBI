#
# Conditional build:
%bcond_without	autodeps	# don't BR packages needed only for resolving deps
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	Template
%define		pnam	DBI
Summary:	DBI plugin for Template Toolkit - database access
Summary(pl):	Wtyczka DBI dla pakietu Template Toolkit - dostêp do baz danych
Name:		perl-Template-DBI
Version:	2.64
Release:	1
# same as perl
License:	GPL v1+ or or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	424d2f17b8b2b3329e758044210920cb
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	perl(File::Spec) >= 0.6
BuildRequires:	perl-AppConfig >= 1.52
%if %{with autodeps} || %{with tests}
BuildRequires:	perl-DBI >= 1.14
BuildRequires:	perl-Pod-POM >= 0.1
BuildRequires:	perl-Template-Toolkit >= 2.15
BuildRequires:	perl-Text-Autoformat >= 1.03
%endif
BuildRequires:	rpm-perlprov >= 4.1-13
Requires:	perl-Template-Toolkit >= 2.15
Obsoletes:	perl-Template-Toolkit-Plugin-DBI
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
DBI plugin for Template Toolkit - interface to the DBI module. It
provides an interface to the Perl DBI/DBD modules, allowing you to
integrate SQL queries into your template documents. It also provides
an interface via the Tie::DBI module (if installed on your system) so
that you can access database records without having to embed any SQL
in your templates.

%description -l pl
Wtyczka DBI dla pakietu Template Toolkit - bêd±ca interfejsem do
modu³u DBI. Daje dostêp do modu³ów Perla DBI/DBD, pozwalaj±c na
integrowanie zapytañ SQL do dokumentów szablonów. Udostêpnia tak¿e
interfejs poprzez modu³ Tie::DBI (je¶li jest zainstalowany), co
pozwala na dostêp do rekordów bazy danych bez potrzeby osadzania SQL-a
w szablonach.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
echo "n" | %{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{perl_vendorlib}/Template/Plugin/DBI.pm
%{_mandir}/man3/*
