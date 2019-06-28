  

# CUDAFLAGS  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Default compilation flags to be used when compiling CUDA files. Will only be
used by CMake on the first configuration to determine CUDA default
compilation flags, after which the value for CUDAFLAGS is stored in the
cache as CMAKE_CUDA_FLAGS. For any configuration
run (including the first), the environment variable will be ignored if
the CMAKE_CUDA_FLAGS variable is defined.  

