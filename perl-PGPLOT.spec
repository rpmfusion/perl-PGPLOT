Name: perl-PGPLOT
Version: 2.21
Release: 2%{?dist}.1
Summary: Perl extension for using the pgplot library
Group: Development/Libraries
License: GPL+ or Artistic
URL: http://search.cpan.org/dist/PGPLOT/
Source0: http://search.cpan.org/CPAN/authors/id/K/KG/KGB/PGPLOT-%{version}.tar.gz
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::F77)
BuildRequires: pgplot-devel 
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))
Buildroot: %(mktemp -ud %{_tmppath}/%{name}-%{version}-%{release}-XXXXXX)

%{?perl_default_filter}

%description
Allow subroutines in the PGPLOT graphics library to be called from Perl.

%prep
%setup -q -n PGPLOT-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make pure_install PERL_INSTALL_ROOT=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null \;

%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)
%doc CHANGES HELP LICENSE README
%{perl_vendorarch}/*
%exclude %dir %{perl_vendorarch}/auto/
%{_mandir}/man3/*

%changelog
* Wed Oct 16 2013 Sergio Pascual <sergiopr@fis.ucm.es> - 2.21-2.1
- Add buildroot and defattr (old rpm)

* Wed Sep 11 2013 Sergio Pascual <sergiopr@fis.ucm.es> - 2.21-2
- Removed patch
- Added buildrequires perl(ExtUtils::F77)

* Tue Sep 10 2013 Sergio Pascual <sergiopr@fis.ucm.es> - 2.21-1
- Initial spec

