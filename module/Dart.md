  

# Dart  
Configure a project for testing with CTest or old Dart Tcl Client  

This file is the backwards-compatibility version of the CTest module.
It supports using the old Dart 1 Tcl client for driving dashboard
submissions as well as testing with CTest.  This module should be
included in the CMakeLists.txt file at the top of a project.  Typical
usage:  

include(Dart)
if(BUILD_TESTING)
  # ... testing related CMake code ...
endif()

  

The BUILD_TESTING option is created by the Dart module to determine
whether testing support should be enabled.  The default is ON.  

