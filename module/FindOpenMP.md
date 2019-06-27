  

# FindOpenMP  
Finds Open Multi-Processing (OpenMP) support.  

This module can be used to detect OpenMP support in a compiler.  If
the compiler supports OpenMP, the flags required to compile with
OpenMP support are returned in variables for the different languages.
The variables may be empty if the compiler does not need a special
flag to support OpenMP.  


Variables
The module exposes the components C, CXX, and Fortran.
Each of these controls the various languages to search OpenMP support for.
Depending on the enabled components the following variables will be set:

OpenMP_FOUND
Variable indicating that OpenMP flags for all requested languages have been found.
If no components are specified, this is true if OpenMP settings for all enabled languages
were detected.
OpenMP_VERSION
Minimal version of the OpenMP standard detected among the requested languages,
or all enabled languages if no components were specified.

This module will set the following variables per language in your
project, where ```<lang>``` is one of C, CXX, or Fortran:

OpenMP_```<lang>```_FOUND
Variable indicating if OpenMP support for ```<lang>``` was detected.
OpenMP_```<lang>```_FLAGS
OpenMP compiler flags for ```<lang>```, separated by spaces.

For linking with OpenMP code written in ```<lang>```, the following
variables are provided:

OpenMP_```<lang>```_LIB_NAMES
;-list of libraries for OpenMP programs for ```<lang>```.
OpenMP_```<libname>```_LIBRARY
Location of the individual libraries needed for OpenMP support in ```<lang>```.
OpenMP_```<lang>```_LIBRARIES
A list of libraries needed to link with OpenMP code written in ```<lang>```.

Additionally, the module provides IMPORTED targets:

OpenMP::OpenMP_```<lang>```
Target for using OpenMP from ```<lang>```.

Specifically for Fortran, the module sets the following variables:

OpenMP_Fortran_HAVE_OMPLIB_HEADER
Boolean indicating if OpenMP is accessible through omp_lib.h.
OpenMP_Fortran_HAVE_OMPLIB_MODULE
Boolean indicating if OpenMP is accessible through the omp_lib Fortran module.

The module will also try to provide the OpenMP version variables:

OpenMP_```<lang>```_SPEC_DATE
Date of the OpenMP specification implemented by the ```<lang>``` compiler.
OpenMP_```<lang>```_VERSION_MAJOR
Major version of OpenMP implemented by the ```<lang>``` compiler.
OpenMP_```<lang>```_VERSION_MINOR
Minor version of OpenMP implemented by the ```<lang>``` compiler.
OpenMP_```<lang>```_VERSION
OpenMP version implemented by the ```<lang>``` compiler.

The specification date is formatted as given in the OpenMP standard:
yyyymm where yyyy and mm represents the year and month of
the OpenMP specification implemented by the ```<lang>``` compiler.
  

