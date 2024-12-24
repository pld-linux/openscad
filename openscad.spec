# TODO: ENABLE_PYTHON, BR: python3-devel, cryptopp-devel
#
# Conditional build:
%bcond_with	tests		# test suite (needs external MCAD)

%ifarch x32
%undefine	with_tests
%endif
Summary:	The Programmers Solid 3D CAD Modeller
Summary(pl.UTF-8):	Program CAD do modelowania brył 3D
Name:		openscad
%define	hash	fd3a9aa
Version:	2024.11.03
Release:	4
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:	GPL v2 with exceptions, CC0
Group:		Applications/Engineering
#Source0:	http://files.openscad.org/%{name}-%{version}.src.tar.gz
Source0:	https://github.com/openscad/openscad/archive/%{hash}/%{name}-%{version}.tar.gz
# Source0-md5:	0eebc48f5fc493d3f57896dec43e5ba1
# see libraries/MCAD on github for submodule reference
%define	mcad_gitref	1ea402208c3127ffb443931e9bb1681c191dacca
Source1:	https://github.com/openscad/MCAD/archive/%{mcad_gitref}/MCAD-%{mcad_gitref}.tar.gz
# Source1-md5:	a86572e744abff686ee146274eda87f4
Patch0:		%{name}-polyclipping.patch
Patch1:		localedir.patch
Patch2:		tests.patch
URL:		https://openscad.org/
BuildRequires:	CGAL-devel >= 5.0
BuildRequires:	EGL-devel
%{?with_tests:BuildRequires:	ImageMagick}
%{?with_tests:BuildRequires:	ImageMagick-coder-png}
%{?with_tests:BuildRequires:	Mesa-dri-driver-swrast}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt5Concurrent-devel >= 5.12
BuildRequires:	Qt5Core-devel >= 5.12
BuildRequires:	Qt5DBus-devel >= 5
BuildRequires:	Qt5Gamepad-devel >= 5
BuildRequires:	Qt5Multimedia-devel >= 5.12
BuildRequires:	Qt5Network-devel >= 5.12
BuildRequires:	Qt5OpenGL-devel >= 5.12
BuildRequires:	Qt5Svg-devel >= 5.12
BuildRequires:	Qt5Widgets-devel >= 5.12
# or Qt6{Concurrent,Core,Core5Compat,DBus,Multimedia,Network,OpenGL,OpenGLWidgets,Svg,Widgets} >= 6 + Qt6QScintilla >= 2.8.0
BuildRequires:	bison >= 2.4
BuildRequires:	boost-devel >= 1.56
BuildRequires:	cairo-devel >= 1.14
BuildRequires:	cmake >= 3.13
BuildRequires:	desktop-file-utils
BuildRequires:	double-conversion-devel
BuildRequires:	eigen3 >= 3
BuildRequires:	flex >= 2.5.35
BuildRequires:	fontconfig-devel >= 2.10
BuildRequires:	freetype-devel >= 1:2.4.9
BuildRequires:	gettext-tools
# or glad-devel with opencsg >= 1.6.0
BuildRequires:	glew-devel >= 1.6
BuildRequires:	glib2-devel >= 1:2.26
BuildRequires:	gmp-devel >= 5.0.0
BuildRequires:	harfbuzz-devel >= 0.9.19
BuildRequires:	hidapi-devel >= 0.10
BuildRequires:	lib3mf-devel >= 1.8.1
BuildRequires:	libspnav-devel
# C++17
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	libxml2-devel >= 1:2.9
BuildRequires:	libzip-devel
BuildRequires:	manifold-devel
BuildRequires:	mimalloc-devel
BuildRequires:	mpfr-devel >= 3.0.0
BuildRequires:	opencsg-devel >= 1.3.2
BuildRequires:	pkgconfig
BuildRequires:	polyclipping-devel >= 6.1.3
BuildRequires:	procps
BuildRequires:	python3 >= 1:3.4
BuildRequires:	qscintilla2-qt5-devel >= 2.11.2
BuildRequires:	qt5-build >= 5.12
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	sanitizers-cmake
BuildRequires:	tbb-devel
BuildRequires:	xorg-lib-libX11-devel
%{?with_tests:BuildRequires:	xorg-xserver-Xvfb}
# Library may have new symbols without soname change
%requires_eq	tbb
Requires:	Qt5Concurrent >= 5.12
Requires:	Qt5Core >= 5.12
Requires:	Qt5DBus >= 5
Requires:	Qt5Gamepad >= 5
Requires:	Qt5Multimedia >= 5.12
Requires:	Qt5Network >= 5.12
Requires:	Qt5OpenGL >= 5.12
Requires:	Qt5Svg >= 5.12
Requires:	Qt5Widgets >= 5.12
Requires:	cairo >= 1.14
Requires:	font(liberationmono)
Requires:	font(liberationsans)
Requires:	font(liberationserif)
Requires:	fontconfig-libs >= 2.10
Requires:	freetype >= 1:2.4.9
Requires:	glew >= 1.6
Requires:	glib2 >= 1:2.26
Requires:	gmp >= 5.0.0
Requires:	harfbuzz >= 0.9.19
Requires:	hidapi >= 0.10
Requires:	lib3mf >= 1.8.1
Requires:	libxml2 >= 1:2.9
Requires:	mpfr >= 3.0.0
Requires:	opencsg >= 1.3.2
Requires:	polyclipping >= 6.1.3
Requires:	qscintilla2-qt5 >= 2.11.2
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

%description -l pl.UTF-8
OpenSCAD to oprogramowanie do tworzenia obiektów CAD w postaci brył
trójwymiarowych. W przeciwieństwie do większości wolnodostępnych
programów do tworzenia modeli 3D (takich, jak słynny Blender), nie
skupia się na aspektach artystycznych modelowania 3D, ale na aspektach
CAD (projektowania wspomaganego komputerowo). Może więc przydzać się
do tworzenia modeli 3D części maszyn, ale nie do tworzenia filmów
animowanych.

%package MCAD
Summary:	OpenSCAD Parametric CAD Library
Summary(pl.UTF-8):	Biblioteka parametryczna CAD dla programu OpenSCAD
License:	LGPL v2/v2+/v3+, GPL v3/v3+, CC-BY-SA, CC-BY, BSD, MIT, Public Domain
URL:		https://www.github.com/openscad/MCAD
Requires:	%{name} = %{version}-%{release}
BuildArch:	noarch

%description MCAD
This library contains components commonly used in designing and
moching up mechanical designs. It is currently unfinished and you can
expect some API changes, however many things are already working.

%description MCAD -l pl.UTF-8
Ta biblioteka zawiera komponenty często używane przy projektach
mechanicznych. Obecnie nie jest skończona i można spodziewać się
zmian API, ale wiele rzeczy już działa.

%prep
%setup -q -n openscad-fd3a9aad2bcd913ac1830e11670f0a422231e43f
%patch0 -p1
%patch1 -p1

%{__tar} xf %{SOURCE1} -C libraries/MCAD --strip-components=1

# use system package
%{__rm} -r src/ext/polyclipping

%build
%cmake -B build \
	-DUSE_BUILTIN_MANIFOLD=OFF \
	-DUSE_CCACHE=OFF \
	%{cmake_on_off tests ENABLE_TESTS}

%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} -r $RPM_BUILD_ROOT%{_datadir}/%{name}/fonts
%{__rm} $RPM_BUILD_ROOT%{_datadir}/%{name}/libraries/MCAD/{README.markdown,TODO,lgpl-2.1.txt}
%{__mv} $RPM_BUILD_ROOT%{_datadir}/{%{name},}/locale

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README.md RELEASE_NOTES.md
%attr(755,root,root) %{_bindir}/openscad
%dir %{_datadir}/%{name}
%{_datadir}/%{name}/examples
%{_datadir}/%{name}/color-schemes
%dir %{_datadir}/%{name}/libraries
%{_datadir}/%{name}/shaders
%{_datadir}/%{name}/templates
%{_datadir}/metainfo/org.openscad.OpenSCAD.appdata.xml
%{_datadir}/mime/packages/openscad.xml
%{_desktopdir}/openscad.desktop
%{_iconsdir}/hicolor/*x*/apps/openscad.png
%{_mandir}/man1/openscad.1*

%files MCAD
%defattr(644,root,root,755)
%doc libraries/MCAD/{README.markdown,TODO}
%{_datadir}/%{name}/libraries/MCAD
