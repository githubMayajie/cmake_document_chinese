  

# CMAKE_C_KNOWN_FEATURES  
List of C features known to this version of CMake.  

The features listed in this global property may be known to be available to the
C compiler.  If the feature is available with the C compiler, it will
be listed in the CMAKE_C_COMPILE_FEATURES variable.  

The features listed here may be used with the target_compile_features()
command.  See the cmake-compile-features(7) manual for information on
compile features and a list of supported compilers.  

The features known to this version of CMake are:  


c_std_90
Compiler mode is aware of C 90.
c_std_99
Compiler mode is aware of C 99.
c_std_11
Compiler mode is aware of C 11.
c_function_prototypes
Function prototypes, as defined in ISO/IEC 9899:1990.
c_restrict
restrict keyword, as defined in ISO/IEC 9899:1999.
c_static_assert
Static assert, as defined in ISO/IEC 9899:2011.
c_variadic_macros
Variadic macros, as defined in ISO/IEC 9899:1999.
  
