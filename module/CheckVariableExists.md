  

# CheckVariableExists  
Check if the variable exists.  



CHECK_VARIABLE_EXISTS
CHECK_VARIABLE_EXISTS(VAR VARIABLE)


VAR      - the name of the variable
VARIABLE - variable to store the result
           Will be created as an internal cache variable.


This macro is only for C variables.
  

The following variables may be set before calling this macro to modify
the way the check is run:  

CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_LINK_OPTIONS = list of options to pass to link command
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages

  

