  

# add_compile_definitions  
Add preprocessor definitions to the compilation of source files.  

add_compile_definitions(```<definition>``` ...)

  

Adds preprocessor definitions to the compiler command line for targets in the
current directory and below (whether added before or after this command is
invoked). See documentation of the directory
and target COMPILE_DEFINITIONS properties.  

Definitions are specified using the syntax VAR or VAR=value.
Function-style definitions are not supported. CMake will automatically
escape the value correctly for the native build system (note that CMake
language syntax may require escapes to specify some values).  

Arguments to add_compile_definitions may use ˇ°generator expressionsˇ± with
the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  

