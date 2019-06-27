  

# FindTclsh  
Find tclsh  

This module finds if TCL is installed and determines where the include
files and libraries are.  It also determines what the name of the
library is.  This code sets the following variables:  

TCLSH_FOUND = TRUE if tclsh has been found
TCL_TCLSH = the path to the tclsh executable

  

In cygwin, look for the cygwin version first.  Don¡¯t look for it later
to avoid finding the cygwin version on a Win32 build.  

