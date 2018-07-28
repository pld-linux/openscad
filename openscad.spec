#
# Conditional build:
%bcond_with	tests		# build with tests
%bcond_with	qt5

%define	qtver	%{?with_qt5:5}%{!?with_qt5:4}

%define	upversion 2015.03-1
Summary:	The Programmers Solid 3D CAD Modeller
Name:		openscad
Version:	2015.03.1
Release:	8
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:	GPLv2 with exceptions and CC0
Group:		Applications/Engineering
Source0:	http://files.openscad.org/%{name}-%{upversion}.src.tar.gz
# Source0-md5:	c5994220078f5f5c13984da304e4a2fe
Patch0:		%{name}-polyclipping.patch
URL:		http://www.openscad.org/
BuildRequires:	CGAL-devel >= 3.6
BuildRequires:	ImageMagick
BuildRequires:	Mesa-dri-driver-swrast
BuildRequires:	bison >= 2.4
BuildRequires:	boost-devel >= 1.35
BuildRequires:	desktop-file-utils
BuildRequires:	eigen3
BuildRequires:	flex >= 2.5.35
BuildRequires:	fontconfig-devel >= 2.10
BuildRequires:	freetype-devel >= 2.4
BuildRequires:	gettext
BuildRequires:	glew-devel >= 1.6
BuildRequires:	glib2-devel
BuildRequires:	gmp-devel >= 5.0.0
BuildRequires:	harfbuzz-devel >= 0.9.19
BuildRequires:	mpfr-devel >= 3.0.0
BuildRequires:	opencsg-devel >= 1.3.2
BuildRequires:	polyclipping-devel >= 6.1.3
BuildRequires:	procps
BuildRequires:	python
BuildRequires:	qscintilla2-qt%{qtver}-devel
BuildRequires:	qt%{qtver}-build >= 4.4
BuildRequires:	xorg-xserver-Xvfb
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description    MCAD
This library contains components commonly used in designing and
moching up mechanical designs. It is currently unfinished and you can
expect some API changes, however many things are already working.

%prep
%setup -qn %{name}-%{upversion}
%patch0 -p1

# use system package
rm -r src/polyclipping

%build
qmake-qt%{qtver} \
	PREFIX=%{_prefix}
%{__make}

# tests
cd tests
install -d build
cd build
%cmake ..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -j1 install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

rm -r $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts

:> %{name}.lang
# TODO: fix this to find the files
#%find_lang %{name}

rm $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/lgpl-2.1.txt
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/README.markdown
rm $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/TODO

%if %{with tests}
cd tests
ctest
cd ..
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md RELEASE_NOTES
%attr(755,root,root) %{_bindir}/%{name}
%{_datadir}/appdata/*.xml
%{_desktopdir}/%{name}.desktop
%{_pixmapsdir}/%{name}.png
%{_datadir}/mime/packages/%{name}.xml
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/color-schemes
%dir %{_datadir}/%{name}/locale
# drop when find_lang is fixed
%{_datadir}/%{name}/locale/*
%dir %{_datadir}/%{name}/libraries
%{_mandir}/man1/*

%files MCAD
%defattr(644,root,root,755)
%doc libraries/MCAD/README.markdown libraries/MCAD/TODO
%{_datadir}/%{name}/libraries/MCAD
