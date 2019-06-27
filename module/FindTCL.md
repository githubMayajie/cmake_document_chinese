  

# FindTCL  
TK_INTERNAL_PATH was removed.  

This module finds if Tcl is installed and determines where the include
files and libraries are.  It also determines what the name of the
library is.  This code sets the following variables:  

TCL_FOUND              = Tcl was found
TK_FOUND               = Tk was found
TCLTK_FOUND            = Tcl and Tk were found
TCL_LIBRARY            = path to Tcl library (tcl tcl80)
TCL_INCLUDE_PATH       = path to where tcl.h can be found
TCL_TCLSH              = path to tclsh binary (tcl tcl80)
TK_LIBRARY             = path to Tk library (tk tk80 etc)
TK_INCLUDE_PATH        = path to where tk.h can be found
TK_WISH                = full path to the wish executable

  

In an effort to remove some clutter and clear up some issues for
people who are not necessarily Tcl/Tk gurus/developers, some
variables were moved or removed.  Changes compared to CMake 2.4 are:  

=>``` they were only useful for people writing Tcl/Tk extensions.
=>``` these libs are not packaged by default with Tcl/Tk distributions.
   Even when Tcl/Tk is built from source, several flavors of debug libs
   are created and there is no real reason to pick a single one
   specifically (say, amongst tcl84g, tcl84gs, or tcl84sgx).
   Let's leave that choice to the user by allowing him to assign
   TCL_LIBRARY to any Tcl library, debug or not.
=>``` this ended up being only a Win32 variable, and there is a lot of
   confusion regarding the location of this file in an installed Tcl/Tk
   tree anyway (see 8.5 for example). If you need the internal path at
   this point it is safer you ask directly where the *source* tree is
   and dig from there.

  

