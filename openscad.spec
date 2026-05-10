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
%define	hash	1e5d8ca
Version:	2026.03.08
Release:	2
# COPYING contains a linking exception for CGAL
# Appdata file is CC0
# Examples are CC0
License:	GPL v2 with exceptions, CC0
Group:		Applications/Engineering
#Source0:	http://files.openscad.org/%{name}-%{version}.src.tar.gz
Source0:	https://github.com/openscad/openscad/archive/%{hash}/%{name}-%{version}.tar.gz
# Source0-md5:	475d58035886bf5dd745837b42e3e024
# see libraries/MCAD on github for submodule reference
%define	mcad_gitref	1ea402208c3127ffb443931e9bb1681c191dacca
Source1:	https://github.com/openscad/MCAD/archive/%{mcad_gitref}/MCAD-%{mcad_gitref}.tar.gz
# Source1-md5:	a86572e744abff686ee146274eda87f4
Patch1:		localedir.patch
Patch2:		lib3mf2.patch
URL:		https://openscad.org/
BuildRequires:	CGAL-devel >= 6.1.1
BuildRequires:	Clipper2-devel
BuildRequires:	EGL-devel
%{?with_tests:BuildRequires:	ImageMagick}
%{?with_tests:BuildRequires:	ImageMagick-coder-png}
%{?with_tests:BuildRequires:	Mesa-dri-driver-swrast}
BuildRequires:	OpenGL-GLX-devel
BuildRequires:	OpenGL-devel
BuildRequires:	Qt6Concurrent-devel
BuildRequires:	Qt6Core-devel
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Multimedia-devel
BuildRequires:	Qt6Network-devel
BuildRequires:	Qt6OpenGL-devel
BuildRequires:	Qt6PrintSupport-devel
BuildRequires:	Qt6Qt5Compat-devel
BuildRequires:	Qt6Svg-devel
BuildRequires:	Qt6Wayland-devel
BuildRequires:	Qt6Widgets-devel
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
BuildRequires:	manifold-devel >= 3.4.0
BuildRequires:	mimalloc-devel
BuildRequires:	mpfr-devel >= 3.0.0
BuildRequires:	opencsg-devel >= 1.3.2
BuildRequires:	pkgconfig
BuildRequires:	procps
BuildRequires:	python3 >= 1:3.4
BuildRequires:	qscintilla2-qt6-devel
BuildRequires:	qt6-build
BuildRequires:	rpm-build >= 4.6
BuildRequires:	rpmbuild(macros) >= 2.016
BuildRequires:	sanitizers-cmake
BuildRequires:	tbb-devel
BuildRequires:	xorg-lib-libX11-devel
%{?with_tests:BuildRequires:	xorg-xserver-Xvfb}
# Library may have new symbols without soname change
%requires_eq	tbb
Requires:	Qt6Concurrent
Requires:	Qt6Core
Requires:	Qt6DBus
Requires:	Qt6Multimedia
Requires:	Qt6Network
Requires:	Qt6OpenGL
Requires:	Qt6PrintSupport
Requires:	Qt6Qt5Compat
Requires:	Qt6Svg
Requires:	Qt6Wayland
Requires:	Qt6Widgets
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
Requires:	qscintilla2-qt6
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
%setup -q -n openscad-1e5d8ca4bb937582781a99b65cc0b3b5bd047ec8
%patch -P1 -p1
%patch -P2 -p1

%{__tar} xf %{SOURCE1} -C libraries/MCAD --strip-components=1

%build
%cmake -B build \
	-DUSE_BUILTIN_MANIFOLD=OFF \
	-DUSE_BUILTIN_CLIPPER2=OFF \
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
