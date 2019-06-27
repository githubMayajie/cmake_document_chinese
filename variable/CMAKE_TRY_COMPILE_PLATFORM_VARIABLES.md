  

# CMAKE_TRY_COMPILE_PLATFORM_VARIABLES  
List of variables that the try_compile() command source file signature
must propagate into the test project in order to target the same platform as
the host project.  

This variable should not be set by project code.  It is meant to be set by
CMake��s platform information modules for the current toolchain, or by a
toolchain file when used with CMAKE_TOOLCHAIN_FILE.  

Variables meaningful to CMake, such as CMAKE_```<LANG>```_FLAGS, are
propagated automatically.  The CMAKE_TRY_COMPILE_PLATFORM_VARIABLES
variable may be set to pass custom variables meaningful to a toolchain file.
For example, a toolchain file may contain:  

set(CMAKE_SYSTEM_NAME ...)
set(CMAKE_TRY_COMPILE_PLATFORM_VARIABLES MY_CUSTOM_VARIABLE)
# ... use MY_CUSTOM_VARIABLE ...

  

If a user passes -DMY_CUSTOM_VARIABLE=SomeValue to CMake then this
setting will be made visible to the toolchain file both for the main
project and for test projects generated by the try_compile()
command source file signature.  
