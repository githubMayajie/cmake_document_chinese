  

# CheckLibraryExists  
Check if the function exists.  



CHECK_LIBRARY_EXISTS
CHECK_LIBRARY_EXISTS(LIBRARY FUNCTION LOCATION VARIABLE)


LIBRARY  - the name of the library you are looking for
FUNCTION - the name of the function
LOCATION - location where the library should be found
VARIABLE - variable to store the result
           Will be created as an internal cache variable.


  

The following variables may be set before calling this macro to modify
the way the check is run:  

CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_LINK_OPTIONS = list of options to pass to link command
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages

  

