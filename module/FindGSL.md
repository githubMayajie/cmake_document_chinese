  

# FindGSL  
Find the native GNU Scientific Library (GSL) includes and libraries.  

The GNU Scientific Library (GSL) is a numerical library for C and C++
programmers. It is free software under the GNU General Public
License.  


Imported Targets
If GSL is found, this module defines the following IMPORTED
targets:
GSL::gsl      - The main GSL library.
GSL::gslcblas - The CBLAS support library used by GSL.


  


Result Variables
This module will set the following variables in your project:
GSL_FOUND          - True if GSL found on the local system
GSL_INCLUDE_DIRS   - Location of GSL header files.
GSL_LIBRARIES      - The GSL libraries.
GSL_VERSION        - The version of the discovered GSL install.


  


Hints
Set GSL_ROOT_DIR to a directory that contains a GSL installation.
This script expects to find libraries at $GSL_ROOT_DIR/lib and the GSL
headers at $GSL_ROOT_DIR/include/gsl.  The library directory may
optionally provide Release and Debug folders. If available, the libraries
named gsld, gslblasd or cblasd are recognized as debug libraries.
For Unix-like systems, this script will use $GSL_ROOT_DIR/bin/gsl-config
(if found) to aid in the discovery of GSL.
  


Cache Variables
This module may set the following variables depending on platform and type
of GSL installation discovered.  These variables may optionally be set to
help this module find the correct files:
GSL_CBLAS_LIBRARY       - Location of the GSL CBLAS library.
GSL_CBLAS_LIBRARY_DEBUG - Location of the debug GSL CBLAS library (if any).
GSL_CONFIG_EXECUTABLE   - Location of the ``gsl-config`` script (if any).
GSL_LIBRARY             - Location of the GSL library.
GSL_LIBRARY_DEBUG       - Location of the debug GSL library (if any).


  

