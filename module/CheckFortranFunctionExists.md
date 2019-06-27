  

# CheckFortranFunctionExists  
Check if a Fortran function exists.  



CHECK_FORTRAN_FUNCTION_EXISTS
CHECK_FORTRAN_FUNCTION_EXISTS(```<function>``` ```<result>```)


where

```<function>```
the name of the Fortran function
```<result>```
variable to store the result; will be created as an internal cache variable.

  

The following variables may be set before calling this macro to modify
the way the check is run:  


CMAKE_REQUIRED_LINK_OPTIONS
A ;-list of options to add to the link
command (see try_compile() for further details).
CMAKE_REQUIRED_LIBRARIES
A ;-list of libraries to add to the link
command. These can be the name of system libraries or they can be
Imported Targets (see try_compile() for
further details).
  

