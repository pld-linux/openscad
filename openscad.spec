#
# Conditional build:
%bcond_with	tests		# build with tests (need external MCAD)

%ifarch x32
%undefine	with_tests
%endif
Summary:	The Programmers Solid 3D CAD Modeller
Name:		openscad
%define	hash	fd3a9aa
Version:	2024.11.03
Release:	1
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:	GPLv2 with exceptions and CC0
Group:		Applications/Engineering
#Source0:	http://files.openscad.org/%{name}-%{version}.src.tar.gz
Source0:	https://github.com/openscad/openscad/archive/%{hash}/%{name}-%{version}.tar.gz
# Source0-md5:	0eebc48f5fc493d3f57896dec43e5ba1
Patch0:		%{name}-polyclipping.patch
Patch1:		localedir.patch
Patch2:		tests.patch
URL:		http://www.openscad.org/
BuildRequires:	CGAL-devel >= 5.0
%{?with_tests:BuildRequires:	ImageMagick}
%{?with_tests:BuildRequires:	ImageMagick-coder-png}
%{?with_tests:BuildRequires:	Mesa-dri-driver-swrast}
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	bison >= 2.4
BuildRequires:	boost-devel >= 1.35
BuildRequires:	cmake >= 3.3
BuildRequires:	desktop-file-utils
BuildRequires:	double-conversion-devel
BuildRequires:	eigen3
BuildRequires:	flex >= 2.5.35
BuildRequires:	fontconfig-devel >= 2.10
BuildRequires:	freetype-devel >= 2.4
BuildRequires:	gettext
BuildRequires:	glew-devel >= 1.6
BuildRequires:	glib2-devel
BuildRequires:	gmp-devel >= 5.0.0
BuildRequires:	harfbuzz-devel >= 0.9.19
BuildRequires:	lib3mf-devel >= 1.8.1
BuildRequires:	libxml2-devel
BuildRequires:	libzip-devel
BuildRequires:	manifold-devel
BuildRequires:	mimalloc-devel
BuildRequires:	mpfr-devel >= 3.0.0
BuildRequires:	opencsg-devel >= 1.3.2
BuildRequires:	pkgconfig
BuildRequires:	polyclipping-devel >= 6.1.3
BuildRequires:	procps
BuildRequires:	python3
BuildRequires:	qscintilla2-qt5-devel >= 2.11.2
BuildRequires:	qt5-build
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	sanitizers-cmake
BuildRequires:	tbb-devel
%{?with_tests:BuildRequires:	xorg-xserver-Xvfb}
# Library may have new symbols without soname change
%requires_eq	tbb
Requires:	font(liberationmono)
Requires:	font(liberationsans)
Requires:	font(liberationserif)
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

### LICENSES:

##  LGPLv2+:
#   2Dshapes.scad
#   3d_triangle.scad
#   fonts.scad
#   gridbeam.scad
#   hardware.scad
#   libtriangles.scad
#   multiply.scad
#   shapes.scad
#   screw.scad

##  LGPLv2:
#   gears.scad
#   involute_gears.scad
#   servos.scad
#   transformations.scad
#   triangles.scad
#   unregular_shapes.scad
#   bitmap/letter_necklace.scad

##  LGPLv3+:
#   teardrop.scad

##  GPLv3 or LGPLv2:
#   motors.scad
#   nuts_and_bolts.scad


##  GPLv3+ or LGPLv2:
#   metric_fastners.scad
#   regular_shapes.scad

##  CC-BY-SA or LGPLv2+:
#   bearing.scad
#   materials.scad
#   stepper.scad
#   utilities.scad

##  CC-BY-SA or LGPLv2:
#   units.scad

##  CC-BY:
#   polyholes.scad
#   bitmap/alphabet_block.scad
#   bitmap/bitmap.scad
#   bitmap/height_map.scad
#   bitmap/name_tag.scad

## BSD
#   boxes.scad

## MIT
#   constants.scad
#   curves.scad
#   math.scad

## Public Domain
#   lego_compatibility.scad
#   trochoids.scad

###############################################

%description
OpenSCAD is a software for creating solid 3D CAD objects. Unlike most
free software for creating 3D models (such as the famous application
Blender) it does not focus on the artistic aspects of 3D modeling but
instead on the CAD aspects. Thus it might be the application you are
looking for when you are planning to create 3D models of machine parts
but pretty sure is not what you are looking for when you are more
interested in creating computer-animated movies.

%package MCAD
Summary:	OpenSCAD Parametric CAD Library
License:	LGPLv2+ and LGPLv2 and LGPLv3+ and (GPLv3 or LGPLv2) and (GPLv3+ or LGPLv2) and (CC-BY-SA or LGPLv2+) and (CC-BY-SA or LGPLv2) and CC-BY and BSD and MIT and Public Domain
URL:		https://www.github.com/openscad/MCAD
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description    MCAD
This library contains components commonly used in designing and
moching up mechanical designs. It is currently unfinished and you can
expect some API changes, however many things are already working.

%prep
%setup -q -n openscad-fd3a9aad2bcd913ac1830e11670f0a422231e43f
%patch0 -p1
%patch1 -p1

# use system package
%{__rm} -r src/ext/polyclipping

%build
mkdir -p build
cd build
%cmake ../ \
	-DUSE_BUILTIN_MANIFOLD=OFF \
	%{cmake_on_off tests ENABLE_TESTS}

%{__make}

%if %{with tests}
export OPENSCAD_BINARY=$(pwd)/openscad
cd tests
%cmake .
%{__make}
%{__make} -j1 test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts

%{__mv} $RPM_BUILD_ROOT%{_datadir}/{%{name},}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md RELEASE_NOTES.md
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/metainfo/*.xml
%{_desktopdir}/%{name}.desktop
%{_iconsdir}/hicolor/*x*/apps/openscad.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/color-schemes
%dir %{_datadir}/%{name}/libraries
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/templates
%{_mandir}/man1/*
