  

# FindSWIG  
Find Simplified Wrapper and Interface Generator (SWIG)  

This module finds an installed SWIG.  It sets the following variables:  

SWIG_FOUND - set to "True" if SWIG is found
SWIG_DIR - the directory where swig is installed
SWIG_EXECUTABLE - the path to the swig executable
SWIG_VERSION   - the version number of the swig executable

  

The minimum required version of SWIG can be specified using the
standard syntax, e.g.   find_package(SWIG 1.1)  

All information is collected from the SWIG_EXECUTABLE, so the version
to be found can be changed from the command line by means of setting
SWIG_EXECUTABLE  

