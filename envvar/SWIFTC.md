  

# SWIFTC  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling Swift language files. Will only be used by
CMake on the first configuration to determine Swift compiler, after which the
value for SWIFTC is stored in the cache as
CMAKE_Swift_COMPILER. For any configuration run
(including the first), the environment variable will be ignored if the
CMAKE_Swift_COMPILER variable is defined.  

