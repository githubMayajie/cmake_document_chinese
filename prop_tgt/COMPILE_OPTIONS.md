  

# COMPILE_OPTIONS  
List of options to pass to the compiler.  

This property holds a semicolon-separated list of options
given so far to the add_compile_options() command.  

This property is used to initialize the COMPILE_OPTIONS target
property when a target is created, which is used by the generators to set
the options for the compiler.  

Contents of COMPILE_OPTIONS may use ¡°generator expressions¡± with the
syntax $```<...>```.  See the cmake-generator-expressions(7) manual
for available expressions.  See the cmake-buildsystem(7) manual
for more on defining buildsystem properties.  

