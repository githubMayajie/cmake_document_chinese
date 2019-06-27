  

# CMAKE_```<LANG>```_FLAGS_INIT  
Value used to initialize the CMAKE_```<LANG>```_FLAGS cache entry
the first time a build tree is configured for language ```<LANG>```.
This variable is meant to be set by a toolchain file.  CMake may prepend or append content to
the value based on the environment and target platform.  

See also the configuration-specific
CMAKE_```<LANG>```_FLAGS_```<CONFIG>```_INIT variable.  

