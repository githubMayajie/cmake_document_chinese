  

# CheckCXXSymbolExists  
Check if a symbol exists as a function, variable, or macro in C++  



CHECK_CXX_SYMBOL_EXISTS
CHECK_CXX_SYMBOL_EXISTS(```<symbol>``` ```<files>``` ```<variable>```)


Check that the ```<symbol>``` is available after including given header
```<files>``` and store the result in a ```<variable>```.  Specify the list of
files in one argument as a semicolon-separated list.
CHECK_CXX_SYMBOL_EXISTS() can be used to check in C++ files, as
opposed to CHECK_SYMBOL_EXISTS(), which works only for C.
If the header files define the symbol as a macro it is considered
available and assumed to work.  If the header files declare the symbol
as a function or variable then the symbol must also be available for
linking.  If the symbol is a type or enum value it will not be
recognized (consider using CheckTypeSize
or CheckCXXSourceCompiles).
  

The following variables may be set before calling this macro to modify
the way the check is run:  


CMAKE_REQUIRED_FLAGS
string of compile command line flags.
CMAKE_REQUIRED_DEFINITIONS
a ;-list of macros to define (-DFOO=bar).
CMAKE_REQUIRED_INCLUDES
a ;-list of header search paths to pass to
the compiler.
CMAKE_REQUIRED_LINK_OPTIONS
a ;-list of options to add to the link command.
CMAKE_REQUIRED_LIBRARIES
a ;-list of libraries to add to the link
command. See policy CMP0075.
CMAKE_REQUIRED_QUIET
execute quietly without messages.
  

