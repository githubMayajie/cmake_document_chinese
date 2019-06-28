  

# LDFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Will only be used by CMake on the first configuration to determine the default
linker flags, after which the value for LDFLAGS is stored in the cache
as CMAKE_EXE_LINKER_FLAGS_INIT,
CMAKE_SHARED_LINKER_FLAGS_INIT, and
CMAKE_MODULE_LINKER_FLAGS_INIT. For any configuration run
(including the first), the environment variable will be ignored if the
equivalent  CMAKE_```<TYPE>```_LINKER_FLAGS_INIT variable is defined.  

