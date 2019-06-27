  

# CheckFunctionExists  
Check if a C function can be linked  



check_function_exists
check_function_exists(```<function>``` ```<variable>```)


Checks that the ```<function>``` is provided by libraries on the system and store
the result in a ```<variable>```, which will be created as an internal
cache variable.
  

The following variables may be set before calling this macro to modify the
way the check is run:  


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
  


Note
Prefer using CheckSymbolExists instead of this module,
for the following reasons:

check_function_exists() can¡¯t detect functions that are inlined
in headers or specified as a macro.
check_function_exists() can¡¯t detect anything in the 32-bit
versions of the Win32 API, because of a mismatch in calling conventions.
check_function_exists() only verifies linking, it does not verify
that the function is declared in system headers.

  

