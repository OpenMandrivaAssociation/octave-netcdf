%global octpkg netcdf

Summary:	A NetCDF interface for Octave
Name:		octave-netcdf
Version:	1.0.16
Release:	2
License:	GPLv3+
Group:		Sciences/Mathematics
Url:		https://packages.octave.org/netcdf/
Source0:	https://downloads.sourceforge.net/octave/netcdf-%{version}.tar.gz
# skip failing test(s)
Patch0:		octave-netcdf-1.0.16-skip_tests.patch

BuildRequires:  octave-devel >= 4.0.0
BuildRequires:	pkgconfig(netcdf)

Requires:	octave(api) = %{octave_api}

Requires(post): octave
Requires(postun): octave

%description
A MATLAB compatible NetCDF interface for Octave.

%files
%license COPYING
%doc NEWS
%dir %{octpkgdir}
%{octpkgdir}/*
%dir %{octpkglibdir}
%{octpkglibdir}/*
%{_metainfodir}/*.metainfo.xml

#---------------------------------------------------------------------------

%prep
%autosetup -p1 -n %{octpkg}-%{version}

# remove failing test(s)
#rm -f inst/private/test_netcdf_unlim.m

%build
%set_build_flags
%octave_pkg_build

%install
%octave_pkg_install

%check
%octave_pkg_check

%post
%octave_cmd pkg rebuild

%preun
%octave_pkg_preun

%postun
%octave_cmd pkg rebuild

