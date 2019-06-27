  

# FindwxWindows  

Deprecated since version 3.0: Replaced by FindwxWidgets.
  

Find wxWindows (wxWidgets) installation  

This module finds if wxWindows/wxWidgets is installed and determines
where the include files and libraries are.  It also determines what
the name of the library is.  This code sets the following variables:  

WXWINDOWS_FOUND     = system has WxWindows
WXWINDOWS_LIBRARIES = path to the wxWindows libraries
                      on Unix/Linux with additional
                      linker flags from
                      "wx-config --libs"
CMAKE_WXWINDOWS_CXX_FLAGS  = Compiler flags for wxWindows,
                             essentially "`wx-config --cxxflags`"
                             on Linux
WXWINDOWS_INCLUDE_DIR      = where to find "wx/wx.h" and "wx/setup.h"
WXWINDOWS_LINK_DIRECTORIES = link directories, useful for rpath on
                              Unix
WXWINDOWS_DEFINITIONS      = extra defines

  

OPTIONS If you need OpenGL support please  

set(WXWINDOWS_USE_GL 1)

  

in your CMakeLists.txt before you include this file.  

HAVE_ISYSTEM      - true required to replace -I by -isystem on g++

  

For convenience include Use_wxWindows.cmake in your project¡¯s
CMakeLists.txt using
include(${CMAKE_CURRENT_LIST_DIR}/Use_wxWindows.cmake).  

USAGE  

set(WXWINDOWS_USE_GL 1)
find_package(wxWindows)

  

NOTES wxWidgets 2.6.x is supported for monolithic builds e.g.
compiled in wx/build/msw dir as:  

nmake -f makefile.vc BUILD=debug SHARED=0 USE_OPENGL=1 MONOLITHIC=1

  

DEPRECATED  

CMAKE_WX_CAN_COMPILE
WXWINDOWS_LIBRARY
CMAKE_WX_CXX_FLAGS
WXWINDOWS_INCLUDE_PATH

  

AUTHOR Jan Woetzel ```<http://www.mip.informatik.uni-kiel.de/~jw>```
(07/2003-01/2006)  

