#
# Conditional build:
%bcond_without	tests		# build with tests

%ifnarch %{x8664}
%undefine	with_tests
%endif
Summary:	The Programmers Solid 3D CAD Modeller
Name:		openscad
Version:	2021.01
Release:	1
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:	GPLv2 with exceptions and CC0
Group:		Applications/Engineering
Source0:	http://files.openscad.org/%{name}-%{version}.src.tar.gz
# Source0-md5:	79f8e3a42bcfeeb3ddde9e5bc2311f76
Patch0:		%{name}-polyclipping.patch
Patch1:		localedir.patch
URL:		http://www.openscad.org/
BuildRequires:	CGAL-devel >= 4.9
BuildRequires:	ImageMagick
BuildRequires:	Mesa-dri-driver-swrast
BuildRequires:	Qt5Concurrent-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel
BuildRequires:	Qt5PrintSupport-devel
BuildRequires:	bison >= 2.4
BuildRequires:	boost-devel >= 1.35
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
BuildRequires:	mpfr-devel >= 3.0.0
BuildRequires:	opencsg-devel >= 1.3.2
BuildRequires:	pkgconfig
BuildRequires:	polyclipping-devel >= 6.1.3
BuildRequires:	procps
BuildRequires:	python
BuildRequires:	qscintilla2-qt5-devel >= 2.11.2
BuildRequires:	qt5-build
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
BuildArch:	noarch

%description    MCAD
This library contains components commonly used in designing and
moching up mechanical designs. It is currently unfinished and you can
expect some API changes, however many things are already working.

%prep
%setup -q
%patch0 -p1
%patch1 -p1

# use system package
%{__rm} -r src/ext/polyclipping

%build
qmake-qt5 \
	PREFIX=%{_prefix}
%{__make}

%if %{with tests}
cd tests
%cmake .
%{__make}
%{__make} -j1 test
%endif

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install \
	INSTALL_ROOT=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/lgpl-2.1.txt
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/README.markdown
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/TODO
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
%{_datadir}/%{name}/templates
%{_mandir}/man1/*

%files MCAD
%defattr(644,root,root,755)
%doc libraries/MCAD/README.markdown libraries/MCAD/TODO
%{_datadir}/%{name}/libraries/MCAD
