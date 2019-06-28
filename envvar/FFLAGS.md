  

# FFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Default compilation flags to be used when compiling Fortran files. Will only
be used by CMake on the first configuration to determine Fortran default
compilation flags, after which the value for FFLAGS is stored in the cache
as CMAKE_Fortran_FLAGS. For any configuration
run (including the first), the environment variable will be ignored if
the CMAKE_Fortran_FLAGS variable is defined.  

