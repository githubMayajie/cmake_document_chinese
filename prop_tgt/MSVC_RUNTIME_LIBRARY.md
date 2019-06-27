  

# MSVC_RUNTIME_LIBRARY  
Select the MSVC runtime library for use by compilers targeting the MSVC ABI.  

The allowed values are:  


MultiThreaded
Compile with -MT or equivalent flag(s) to use a multi-threaded
statically-linked runtime library.
MultiThreadedDLL
Compile with -MD or equivalent flag(s) to use a multi-threaded
dynamically-linked runtime library.
MultiThreadedDebug
Compile with -MTd or equivalent flag(s) to use a multi-threaded
statically-linked runtime library.
MultiThreadedDebugDLL
Compile with -MDd or equivalent flag(s) to use a multi-threaded
dynamically-linked runtime library.
  

The value is ignored on non-MSVC compilers but an unsupported value will
be rejected as an error when using a compiler targeting the MSVC ABI.  

The value may also be the empty string ("") in which case no runtime
library selection flag will be added explicitly by CMake.  Note that with
Visual Studio Generators the native build system may choose to
add its own default runtime library selection flag.  

Use generator expressions to
support per-configuration specification.  For example, the code:  

add_executable(foo foo.c)
set_property(TARGET foo PROPERTY
  MSVC_RUNTIME_LIBRARY "MultiThreaded$```<$```<CONFIG:Debug>```:Debug>```")

  

selects for the target foo a multi-threaded statically-linked runtime
library with or without debug information depending on the configuration.  


Note
This property has effect only when policy CMP0091 is set to NEW
prior to the first project() or enable_language() command
that enables a language using a compiler targeting the MSVC ABI.
  

