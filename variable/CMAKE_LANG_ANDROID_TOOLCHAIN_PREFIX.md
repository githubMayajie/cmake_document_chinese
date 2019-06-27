  

# CMAKE_```<LANG>```_ANDROID_TOOLCHAIN_PREFIX  
When Cross Compiling for Android this variable contains the absolute
path prefixing the toolchain GNU compiler and its binutils.  

See also CMAKE_```<LANG>```_ANDROID_TOOLCHAIN_SUFFIX
and CMAKE_```<LANG>```_ANDROID_TOOLCHAIN_MACHINE.  

For example, the path to the linker is:  

${CMAKE_CXX_ANDROID_TOOLCHAIN_PREFIX}ld${CMAKE_CXX_ANDROID_TOOLCHAIN_SUFFIX}

  

