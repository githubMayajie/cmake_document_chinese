  

# CSFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling CSharp language files. Will only be
used by CMake on the first configuration to determine CSharp default
compilation flags, after which the value for CSFLAGS is stored in the cache
as CMAKE_CSharp_FLAGS. For any configuration
run (including the first), the environment variable will be ignored if the
CMAKE_CSharp_FLAGS variable is defined.  

