  

# CXX  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling CXX language files. Will only be used by
CMake on the first configuration to determine CXX compiler, after which the
value for CXX is stored in the cache as
CMAKE_CXX_COMPILER. For any configuration
run (including the first), the environment variable will be ignored if the
CMAKE_CXX_COMPILER variable is defined.  

