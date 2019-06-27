  

# CMAKE_```<LANG>```_STANDARD_INCLUDE_DIRECTORIES  
Include directories to be used for every source file compiled with
the ```<LANG>``` compiler.  This is meant for specification of system
include directories needed by the language for the current platform.
The directories always appear at the end of the include path passed
to the compiler.  

This variable should not be set by project code.  It is meant to be set by
CMake��s platform information modules for the current toolchain, or by a
toolchain file when used with CMAKE_TOOLCHAIN_FILE.  

See also CMAKE_```<LANG>```_STANDARD_LIBRARIES.  
