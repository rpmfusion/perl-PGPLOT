Name:    perl-PGPLOT
Version: 2.30
Release: 2%{?dist}
Summary: Perl extension for using the pgplot library
License: GPL+ or Artistic
URL:     https://metacpan.org/release/PGPLOT
Source0: https://cpan.metacpan.org/authors/id/E/ET/ETJ/PGPLOT-%{version}.tar.gz
# Build
BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: gcc
BuildRequires: libpng12-devel
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-generators
BuildRequires: perl-interpreter
BuildRequires: perl(Config)
BuildRequires: perl(Devel::CheckLib)
BuildRequires: perl(ExtUtils::F77)
BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(ExtUtils::PkgConfig)
BuildRequires: perl(IO::File)
BuildRequires: perl(lib)
BuildRequires: perl(strict)
BuildRequires: perl(Test::More)
BuildRequires: pgplot-devel
BuildRequires: zlib-devel
# Runtime
BuildRequires: perl(DynaLoader)
BuildRequires: perl(Exporter)
BuildRequires: perl(PDL)
# Dependencies
Requires: perl(:MODULE_COMPAT_%(eval "`%{__perl} -V:version`"; echo $version))

%{?perl_default_filter}

%description
Allow subroutines in the PGPLOT graphics library to be called from Perl.

%prep
%autosetup -n PGPLOT-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor OPTIMIZE="%{optflags}"
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
find %{buildroot} -type f -name '*.bs' -empty -delete
%{_fixperms} -c %{buildroot}

%check
make test || :

%files
%license LICENSE
%doc CHANGES HELP README
%{perl_vendorarch}/auto/PGPLOT/
%{perl_vendorarch}/PDL/Demos/PGPLOT*.pm
%{perl_vendorarch}/PDL/Graphics/PGPLOT*.pm
%{perl_vendorarch}/PDL/Graphics/PGPLOT/
%{perl_vendorarch}/PGPLOT.pm
%{_mandir}/man3/PDL::Demos::PGPLOT*
%{_mandir}/man3/PDL::Graphics::*.3pm.*
%{_mandir}/man3/PGPLOT.3*

%changelog
* Wed Jan 29 2025 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.30-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_42_Mass_Rebuild

* Mon Aug 05 2024 Leigh Scott <leigh123linux@gmail.com> - 2.30-1
- Update to 2.30

* Sat Aug 03 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.29-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_41_Mass_Rebuild

* Sun Apr 14 2024 Leigh Scott <leigh123linux@gmail.com> - 2.29-1
- Update to 2.29

* Sun Feb 04 2024 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.28-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_40_Mass_Rebuild

* Thu Aug 03 2023 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.28-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_39_Mass_Rebuild

* Mon Aug 08 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.28-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_37_Mass_Rebuild and ffmpeg
  5.1

* Tue Jun 21 2022 Paul Howarth <paul@city-fan.org> - 2.28-2
- Perl 5.36 rebuild

* Mon Apr 11 2022 Leigh Scott <leigh123linux@gmail.com> - 2.28-1
- Update to 2.28

* Thu Feb 10 2022 RPM Fusion Release Engineering <sergiomb@rpmfusion.org> - 2.24-6
- Rebuilt for https://fedoraproject.org/wiki/Fedora_36_Mass_Rebuild

* Wed Aug 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.24-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_35_Mass_Rebuild

* Thu Jun 17 2021 Leigh Scott <leigh123linux@gmail.com> - 2.24-4
- Rebuild for new perl version

* Thu Feb 04 2021 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.24-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_34_Mass_Rebuild

* Wed Aug 19 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.24-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Wed Jul  1 2020 Paul Howarth <paul@city-fan.org> - 2.24-1
- Update to 2.24

* Wed Feb 05 2020 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.21-14
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Sat Aug 10 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.21-13
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Tue Mar 05 2019 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.21-12
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Sun Aug 19 2018 RPM Fusion Release Engineering <leigh123linux@gmail.com> - 2.21-11
- Rebuilt for Fedora 29 Mass Rebuild binutils issue

* Fri Jul 27 2018 RPM Fusion Release Engineering <sergio@serjux.com> - 2.21-10
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Mar 02 2018 RPM Fusion Release Engineering <leigh123linux@googlemail.com> - 2.21-9
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Sun Feb 04 2018 Sérgio Basto <sergio@serjux.com> - 2.21-8
- Rebuild (gfortran-8.0.1)

* Thu Aug 31 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.21-7
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Sun Jun 18 2017 Paul Howarth <paul@city-fan.org> - 2.21-6
- Perl 5.26 rebuild

* Sun Mar 26 2017 RPM Fusion Release Engineering <kwizart@rpmfusion.org> - 2.21-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

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

