  

# FindCABLE  
Find CABLE  

This module finds if CABLE is installed and determines where the
include files and libraries are.  This code sets the following
variables:  

CABLE             the path to the cable executable
CABLE_TCL_LIBRARY the path to the Tcl wrapper library
CABLE_INCLUDE_DIR the path to the include directory

  

To build Tcl wrappers, you should add shared library and link it to
${CABLE_TCL_LIBRARY}.  You should also add ${CABLE_INCLUDE_DIR} as an
include directory.  

