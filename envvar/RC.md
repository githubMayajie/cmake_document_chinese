  

# RC  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling resource files. Will only be used by CMake
on the first configuration to determine resource compiler, after which the
value for RC is stored in the cache as
CMAKE_RC_COMPILER. For any configuration run
(including the first), the environment variable will be ignored if the
CMAKE_RC_COMPILER variable is defined.  

