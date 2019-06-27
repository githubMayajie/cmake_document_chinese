  

# FindCups  
Find the Common UNIX Printing System (CUPS).  

Set CUPS_REQUIRE_IPP_DELETE_ATTRIBUTE to TRUE if you need a version which
features this function (i.e. at least 1.1.19)  


Imported targets
This module defines IMPORTED target Cups::Cups, if Cups has
been found.
  


Result variables
This module will set the following variables in your project:

CUPS_FOUND
true if CUPS headers and libraries were found
CUPS_INCLUDE_DIRS
the directory containing the Cups headers
CUPS_LIBRARIES
the libraries to link against to use CUPS.
CUPS_VERSION_STRING
the version of CUPS found (since CMake 2.8.8)

  


Cache variables
The following cache variables may also be set:

CUPS_INCLUDE_DIR
the directory containing the Cups headers

  

