  

# CMAKE_SHARED_LINKER_FLAGS_INIT  
Value used to initialize the CMAKE_SHARED_LINKER_FLAGS
cache entry the first time a build tree is configured.
This variable is meant to be set by a toolchain file.  CMake may prepend or append content to
the value based on the environment and target platform.  

See also the configuration-specific variable
CMAKE_SHARED_LINKER_FLAGS_```<CONFIG>```_INIT.  

