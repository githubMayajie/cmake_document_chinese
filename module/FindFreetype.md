  

# FindFreetype  
Find the FreeType font renderer includes and library.  


Imported Targets
This module defines the following IMPORTED target:

Freetype::Freetype
The Freetype freetype library, if found

  


Result Variables
This module will set the following variables in your project:

FREETYPE_FOUND
true if the Freetype headers and libraries were found
FREETYPE_INCLUDE_DIRS
directories containing the Freetype headers. This is the
concatenation of the variables:

FREETYPE_INCLUDE_DIR_ft2build
directory holding the main Freetype API configuration header
FREETYPE_INCLUDE_DIR_freetype2
directory holding Freetype public headers


FREETYPE_LIBRARIES
the library to link against
FREETYPE_VERSION_STRING
the version of freetype found (since CMake 2.8.8)

  


Hints
The user may set the environment variable FREETYPE_DIR to the root
directory of a Freetype installation.
  

