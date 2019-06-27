  

# CheckIncludeFile  
Provides a macro to check if a header file can be included in C.  



CHECK_INCLUDE_FILE
CHECK_INCLUDE_FILE(```<include>``` ```<variable>``` [```<flags>```])


Check if the given ```<include>``` file may be included in a C
source file and store the result in an internal cache entry named
```<variable>```.  The optional third argument may be used to add
compilation flags to the check (or use CMAKE_REQUIRED_FLAGS below).
  

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
  

See the CheckIncludeFiles module to check for multiple headers
at once.  See the CheckIncludeFileCXX module to check for headers
using the CXX language.  

