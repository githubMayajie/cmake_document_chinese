  

# FindZLIB  
Find the native ZLIB includes and library.  


IMPORTED Targets
This module defines IMPORTED target ZLIB::ZLIB, if
ZLIB has been found.
  


Result Variables
This module defines the following variables:
ZLIB_INCLUDE_DIRS   - where to find zlib.h, etc.
ZLIB_LIBRARIES      - List of libraries when using zlib.
ZLIB_FOUND          - True if zlib found.


ZLIB_VERSION_STRING - The version of zlib found (x.y.z)
ZLIB_VERSION_MAJOR  - The major version of zlib
ZLIB_VERSION_MINOR  - The minor version of zlib
ZLIB_VERSION_PATCH  - The patch version of zlib
ZLIB_VERSION_TWEAK  - The tweak version of zlib


  


Backward Compatibility
The following variable are provided for backward compatibility
ZLIB_MAJOR_VERSION  - The major version of zlib
ZLIB_MINOR_VERSION  - The minor version of zlib
ZLIB_PATCH_VERSION  - The patch version of zlib


  


Hints
A user may set ZLIB_ROOT to a zlib installation root to tell this
module where to look.
  

