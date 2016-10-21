Name: perl-PGPLOT
Version: 2.21
Release: 4%{?dist}
Summary: Perl extension for using the pgplot library
License: GPL+ or Artistic
URL: http://search.cpan.org/dist/PGPLOT/
Source0: http://search.cpan.org/CPAN/authors/id/K/KG/KGB/PGPLOT-%{version}.tar.gz
# Build
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl(Config)
BuildRequires: perl(ExtUtils::F77)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(IO::File)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: pgplot-devel
# Runtime
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
# Dependencies
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Allow subroutines in the PGPLOT graphics library to be called from Perl.

%prep
%setup -q -n PGPLOT-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -type f -name '*.bs' -size 0 -exec rm -f {} \;

%{_fixperms} $RPM_BUILD_ROOT/*

%check
#works locally
#make test

%files
%license LICENSE
%doc CHANGES HELP README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
* Fri Oct 21 2016 Paul Howarth <paul@city-fan.org> - 2.21-4
- Specify all build requirements
- Don't need to remove empty directories from the buildroot
- Use %%license

* Sun Aug 31 2014 Sérgio Basto <sergio@serjux.com> - 2.21-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Wed Sep 11 2013 Sergio Pascual <sergiopr@fis.ucm.es> - 2.21-2
- Removed patch
- Added buildrequires perl(ExtUtils::F77)

* Tue Sep 10 2013 Sergio Pascual <sergiopr@fis.ucm.es> - 2.21-1
- Initial spec

