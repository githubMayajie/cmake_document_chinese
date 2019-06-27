  

# FindTclStub  
TCL_STUB_LIBRARY_DEBUG and TK_STUB_LIBRARY_DEBUG were removed.  

This module finds Tcl stub libraries.  It first finds Tcl include
files and libraries by calling FindTCL.cmake.  How to Use the Tcl
Stubs Library:  

http://tcl.activestate.com/doc/howto/stubs.html

  

Using Stub Libraries:  

http://safari.oreilly.com/0130385603/ch48lev1sec3

  

This code sets the following variables:  

TCL_STUB_LIBRARY       = path to Tcl stub library
TK_STUB_LIBRARY        = path to Tk stub library
TTK_STUB_LIBRARY       = path to ttk stub library

  

In an effort to remove some clutter and clear up some issues for
people who are not necessarily Tcl/Tk gurus/developers, some
variables were moved or removed.  Changes compared to CMake 2.4 are:  

=>``` these libs are not packaged by default with Tcl/Tk distributions.
   Even when Tcl/Tk is built from source, several flavors of debug libs
   are created and there is no real reason to pick a single one
   specifically (say, amongst tclstub84g, tclstub84gs, or tclstub84sgx).
   Let's leave that choice to the user by allowing him to assign
   TCL_STUB_LIBRARY to any Tcl library, debug or not.

  

