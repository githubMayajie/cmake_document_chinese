  

# CC  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling C language files. Will only be used by
CMake on the first configuration to determine C compiler, after which the
value for CC is stored in the cache as
CMAKE_C_COMPILER. For any configuration run
(including the first), the environment variable will be ignored if the
CMAKE_C_COMPILER variable is defined.  

