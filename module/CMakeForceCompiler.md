  

# CMakeForceCompiler  

Deprecated since version 3.6: Do not use.
  

The macros provided by this module were once intended for use by
cross-compiling toolchain files when CMake was not able to automatically
detect the compiler identification.  Since the introduction of this module,
CMake¡¯s compiler identification capabilities have improved and can now be
taught to recognize any compiler.  Furthermore, the suite of information
CMake detects from a compiler is now too extensive to be provided by
toolchain files using these macros.  

One common use case for this module was to skip CMake¡¯s checks for a
working compiler when using a cross-compiler that cannot link binaries
without special flags or custom linker scripts.  This case is now supported
by setting the CMAKE_TRY_COMPILE_TARGET_TYPE variable in the
toolchain file instead.  

  

Macro CMAKE_FORCE_C_COMPILER has the following signature:  

CMAKE_FORCE_C_COMPILER(```<compiler>``` ```<compiler-id>```)

  

It sets CMAKE_C_COMPILER to
the given compiler and the cmake internal variable
CMAKE_C_COMPILER_ID to the given
compiler-id.  It also bypasses the check for working compiler and basic
compiler information tests.  

Macro CMAKE_FORCE_CXX_COMPILER has the following signature:  

CMAKE_FORCE_CXX_COMPILER(```<compiler>``` ```<compiler-id>```)

  

It sets CMAKE_CXX_COMPILER to
the given compiler and the cmake internal variable
CMAKE_CXX_COMPILER_ID to the given
compiler-id.  It also bypasses the check for working compiler and basic
compiler information tests.  

Macro CMAKE_FORCE_Fortran_COMPILER has the following signature:  

CMAKE_FORCE_Fortran_COMPILER(```<compiler>``` ```<compiler-id>```)

  

It sets CMAKE_Fortran_COMPILER to
the given compiler and the cmake internal variable
CMAKE_Fortran_COMPILER_ID to the given
compiler-id.  It also bypasses the check for working compiler and basic
compiler information tests.  

So a simple toolchain file could look like this:  

include (CMakeForceCompiler)
set(CMAKE_SYSTEM_NAME Generic)
CMAKE_FORCE_C_COMPILER   (chc12 MetrowerksHicross)
CMAKE_FORCE_CXX_COMPILER (chc12 MetrowerksHicross)

  

