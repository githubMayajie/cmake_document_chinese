  

# CFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Default compilation flags to be used when compiling C files. Will only be
used by CMake on the first configuration to determine CC default compilation
flags, after which the value for CFLAGS is stored in the cache
as CMAKE_C_FLAGS. For any configuration run
(including the first), the environment variable will be ignored if the
CMAKE_C_FLAGS variable is defined.  

