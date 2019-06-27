  

# CMakeDetermineVSServicePack  

Deprecated since version 3.0: Do not use.
  

The functionality of this module has been superseded by the
CMAKE_```<LANG>```_COMPILER_VERSION variable that contains
the compiler version number.  

Determine the Visual Studio service pack of the ¡®cl¡¯ in use.  

Usage:  

if(MSVC)
  include(CMakeDetermineVSServicePack)
  DetermineVSServicePack( my_service_pack )
  if( my_service_pack )
    message(STATUS "Detected: ${my_service_pack}")
  endif()
endif()

  

Function DetermineVSServicePack sets the given variable to one of the
following values or an empty string if unknown:  

vc80, vc80sp1
vc90, vc90sp1
vc100, vc100sp1
vc110, vc110sp1, vc110sp2, vc110sp3, vc110sp4

  

