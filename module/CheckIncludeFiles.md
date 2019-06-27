  

# CheckIncludeFiles  
Provides a macro to check if a list of one or more header files can
be included together.  



CHECK_INCLUDE_FILES
CHECK_INCLUDE_FILES("```<includes>```" ```<variable>``` [LANGUAGE ```<language>```])


Check if the given ```<includes>``` list may be included together
in a source file and store the result in an internal cache
entry named ```<variable>```.  Specify the ```<includes>``` argument
as a ;-list of header file names.
If LANGUAGE is set, the specified compiler will be used to perform the
check. Acceptable values are C and CXX. If not set, the C compiler
will be used if enabled. If the C compiler is not enabled, the C++
compiler will be used if enabled.
  

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
  

See modules CheckIncludeFile and CheckIncludeFileCXX
to check for a single header file in C or CXX languages.  

