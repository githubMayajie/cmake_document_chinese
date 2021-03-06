  

# add_definitions  
Add -D define flags to the compilation of source files.  

add_definitions(-DFOO -DBAR ...)

  

Adds definitions to the compiler command line for targets in the current
directory and below (whether added before or after this command is invoked).
This command can be used to add any flags, but it is intended to add
preprocessor definitions.  


Note
This command has been superseded by alternatives:

Use add_compile_definitions() to add preprocessor definitions.
Use include_directories() to add include directories.
Use add_compile_options() to add other options.

  

Flags beginning in -D or /D that look like preprocessor definitions are
automatically added to the COMPILE_DEFINITIONS directory
property for the current directory.  Definitions with non-trivial values
may be left in the set of flags instead of being converted for reasons of
backwards compatibility.  See documentation of the
directory,
target,
source file COMPILE_DEFINITIONS
properties for details on adding preprocessor definitions to specific
scopes and configurations.  

See the cmake-buildsystem(7) manual for more on defining
buildsystem properties.  

