  

# FindGLEW  
Find the OpenGL Extension Wrangler Library (GLEW)  


Input Variables
The following variables may be set to influence this module¡¯s behavior:

GLEW_USE_STATIC_LIBS
to find and create IMPORTED target for static linkage.
GLEW_VERBOSE
to output a detailed log of this module.

  


Imported Targets
This module defines the following Imported Targets:

GLEW::glew
The GLEW shared library.
GLEW::glew_s
The GLEW static library, if GLEW_USE_STATIC_LIBS is set to TRUE.
GLEW::GLEW
Duplicates either GLEW::glew or GLEW::glew_s based on availability.

  


Result Variables
This module defines the following variables:

GLEW_INCLUDE_DIRS
include directories for GLEW
GLEW_LIBRARIES
libraries to link against GLEW
GLEW_SHARED_LIBRARIES
libraries to link against shared GLEW
GLEW_STATIC_LIBRARIES
libraries to link against static GLEW
GLEW_FOUND
true if GLEW has been found and can be used
GLEW_VERSION
GLEW version
GLEW_VERSION_MAJOR
GLEW major version
GLEW_VERSION_MINOR
GLEW minor version
GLEW_VERSION_MICRO
GLEW micro version

  

