  

# RCFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Default compilation flags to be used when compiling resource files. Will
only be used by CMake on the first configuration to determine resource
default compilation flags, after which the value for RCFLAGS is stored in
the cache as CMAKE_RC_FLAGS. For any
configuration run (including the first), the environment variable will be ignored
if the CMAKE_RC_FLAGS variable is defined.  

