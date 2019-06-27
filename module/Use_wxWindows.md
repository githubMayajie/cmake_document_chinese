  

# Use_wxWindows  

Deprecated since version 2.8.10: Use find_package(wxWidgets) and include(${wxWidgets_USE_FILE}) instead.
  

This convenience include finds if wxWindows is installed and set the
appropriate libs, incdirs, flags etc.  author Jan Woetzel ```<jw -at-
mip.informatik.uni-kiel.de>``` (07/2003)  

USAGE:  

just include Use_wxWindows.cmake
in your projects CMakeLists.txt

  

include( ${CMAKE_MODULE_PATH}/Use_wxWindows.cmake)  

if you are sure you need GL then

  

set(WXWINDOWS_USE_GL 1)  

*before* you include this file.

  

