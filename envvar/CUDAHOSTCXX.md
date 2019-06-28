  

# CUDAHOSTCXX  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling host code when compiling CUDA
language files. Will only be used by CMake on the first configuration to
determine CUDA host compiler, after which the value for CUDAHOSTCXX is
stored in the cache as CMAKE_CUDA_HOST_COMPILER. For any
configuration run (including the first), the environment variable will be
ignored if the CMAKE_CUDA_HOST_COMPILER variable is defined.  

This environment variable is primarily meant for use with projects that
enable CUDA as a first-class language.  The FindCUDA
module will also use it to initialize its CUDA_HOST_COMPILER setting.  

