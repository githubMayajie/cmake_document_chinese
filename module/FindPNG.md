  

# FindPNG  
Find libpng, the official reference library for the PNG image format.  


Imported targets
This module defines the following IMPORTED target:

PNG::PNG
The libpng library, if found.

  


Result variables
This module will set the following variables in your project:

PNG_INCLUDE_DIRS
where to find png.h, etc.
PNG_LIBRARIES
the libraries to link against to use PNG.
PNG_DEFINITIONS
You should add_definitions(${PNG_DEFINITIONS}) before compiling code
that includes png library files.
PNG_FOUND
If false, do not try to use PNG.
PNG_VERSION_STRING
the version of the PNG library found (since CMake 2.8.8)

  


Obsolete variables
The following variables may also be set, for backwards compatibility:

PNG_LIBRARY
where to find the PNG library.
PNG_INCLUDE_DIR
where to find the PNG headers (same as PNG_INCLUDE_DIRS)

Since PNG depends on the ZLib compression library, none of the above
will be defined unless ZLib can be found.
  

