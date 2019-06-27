  

# WriteCompilerDetectionHeader  
This module provides the function write_compiler_detection_header().  

This function can be used to generate a file suitable for preprocessor
inclusion which contains macros to be used in source code:  

write_compiler_detection_header(
          FILE ```<file>```
          PREFIX ```<prefix>```
          [OUTPUT_FILES_VAR ```<output_files_var>``` OUTPUT_DIR ```<output_dir>```]
          COMPILERS ```<compiler>``` [...]
          FEATURES ```<feature>``` [...]
          [BARE_FEATURES ```<feature>``` [...]]
          [VERSION ```<version>```]
          [PROLOG ```<prolog>```]
          [EPILOG ```<epilog>```]
          [ALLOW_UNKNOWN_COMPILERS]
          [ALLOW_UNKNOWN_COMPILER_VERSIONS]
)

  

This generates the file ```<file>``` with macros which all have the prefix
```<prefix>```.  

By default, all content is written directly to the ```<file>```.  The
OUTPUT_FILES_VAR may be specified to cause the compiler-specific
content to be written to separate files.  The separate files are then
available in the ```<output_files_var>``` and may be consumed by the caller
for installation for example.  The OUTPUT_DIR specifies a relative
path from the main ```<file>``` to the compiler-specific files. For example:  

write_compiler_detection_header(
  FILE climbingstats_compiler_detection.h
  PREFIX ClimbingStats
  OUTPUT_FILES_VAR support_files
  OUTPUT_DIR compilers
  COMPILERS GNU Clang MSVC Intel
  FEATURES cxx_variadic_templates
)
install(FILES
  ${CMAKE_CURRENT_BINARY_DIR}/climbingstats_compiler_detection.h
  DESTINATION include
)
install(FILES
  ${support_files}
  DESTINATION include/compilers
)

  

VERSION may be used to specify the API version to be generated.
Future versions of CMake may introduce alternative APIs.  A given
API is selected by any ```<version>``` value greater than or equal
to the version of CMake that introduced the given API and less
than the version of CMake that introduced its succeeding API.
The value of the CMAKE_MINIMUM_REQUIRED_VERSION
variable is used if no explicit version is specified.
(As of CMake version 3.15.0-rc2 there is only one API version.)  

PROLOG may be specified as text content to write at the start of the
header. EPILOG may be specified as text content to write at the end
of the header  

At least one ```<compiler>``` and one ```<feature>``` must be listed.  Compilers
which are known to CMake, but not specified are detected and a preprocessor
#error is generated for them.  A preprocessor macro matching
```<PREFIX>```_COMPILER_IS_```<compiler>``` is generated for each compiler
known to CMake to contain the value 0 or 1.  

Possible compiler identifiers are documented with the
CMAKE_```<LANG>```_COMPILER_ID variable.
Available features in this version of CMake are listed in the
CMAKE_C_KNOWN_FEATURES and
CMAKE_CXX_KNOWN_FEATURES global properties.
The {c,cxx}_std_* meta-features are ignored if requested.  

See the cmake-compile-features(7) manual for information on
compile features.  

BARE_FEATURES will define the compatibility macros with the name used in
newer versions of the language standard, so the code can use the new feature
name unconditionally.  

ALLOW_UNKNOWN_COMPILERS and ALLOW_UNKNOWN_COMPILER_VERSIONS cause
the module to generate conditions that treat unknown compilers as simply
lacking all features.  Without these options the default behavior is to
generate a #error for unknown compilers and versions.  


Feature Test Macros
For each compiler, a preprocessor macro is generated matching
```<PREFIX>```_COMPILER_IS_```<compiler>``` which has the content either 0
or 1, depending on the compiler in use. Preprocessor macros for
compiler version components are generated matching
```<PREFIX>```_COMPILER_VERSION_MAJOR ```<PREFIX>```_COMPILER_VERSION_MINOR
and ```<PREFIX>```_COMPILER_VERSION_PATCH containing decimal values
for the corresponding compiler version components, if defined.
A preprocessor test is generated based on the compiler version
denoting whether each feature is enabled.  A preprocessor macro
matching ```<PREFIX>```_COMPILER_```<FEATURE>```, where ```<FEATURE>``` is the
upper-case ```<feature>``` name, is generated to contain the value
0 or 1 depending on whether the compiler in use supports the
feature:
write_compiler_detection_header(
  FILE climbingstats_compiler_detection.h
  PREFIX ClimbingStats
  COMPILERS GNU Clang AppleClang MSVC Intel
  FEATURES cxx_variadic_templates
)


#if ClimbingStats_COMPILER_CXX_VARIADIC_TEMPLATES
template```<typename... T>```
void someInterface(T t...) { /* ... */ }
#else
// Compatibility versions
template```<typename T1>```
void someInterface(T1 t1) { /* ... */ }
template```<typename T1, typename T2>```
void someInterface(T1 t1, T2 t2) { /* ... */ }
template```<typename T1, typename T2, typename T3>```
void someInterface(T1 t1, T2 t2, T3 t3) { /* ... */ }
#endif


  


Symbol Macros
Some additional symbol-defines are created for particular features for
use as symbols which may be conditionally defined empty:
class MyClass ClimbingStats_FINAL
{
    ClimbingStats_CONSTEXPR int someInterface() { return 42; }
};


The ClimbingStats_FINAL macro will expand to final if the
compiler (and its flags) support the cxx_final feature, and the
ClimbingStats_CONSTEXPR macro will expand to constexpr
if cxx_constexpr is supported.
If BARE_FEATURES cxx_final was given as argument the final keyword
will be defined for old compilers, too.
The following features generate corresponding symbol defines and if they
are available as BARE_FEATURES:








Feature
Define
Symbol
bare



c_restrict
```<PREFIX>```_RESTRICT
restrict
yes

cxx_constexpr
```<PREFIX>```_CONSTEXPR
constexpr
yes

cxx_deleted_functions
```<PREFIX>```_DELETED_FUNCTION
= delete


cxx_extern_templates
```<PREFIX>```_EXTERN_TEMPLATE
extern


cxx_final
```<PREFIX>```_FINAL
final
yes

cxx_noexcept
```<PREFIX>```_NOEXCEPT
noexcept
yes

cxx_noexcept
```<PREFIX>```_NOEXCEPT_EXPR(X)
noexcept(X)


cxx_override
```<PREFIX>```_OVERRIDE
override
yes



  


Compatibility Implementation Macros
Some features are suitable for wrapping in a macro with a backward
compatibility implementation if the compiler does not support the feature.
When the cxx_static_assert feature is not provided by the compiler,
a compatibility implementation is available via the
```<PREFIX>```_STATIC_ASSERT(COND) and
```<PREFIX>```_STATIC_ASSERT_MSG(COND, MSG) function-like macros. The macros
expand to static_assert where that compiler feature is available, and
to a compatibility implementation otherwise. In the first form, the
condition is stringified in the message field of static_assert.  In
the second form, the message MSG is passed to the message field of
static_assert, or ignored if using the backward compatibility
implementation.
The cxx_attribute_deprecated feature provides a macro definition
```<PREFIX>```_DEPRECATED, which expands to either the standard
[[deprecated]] attribute or a compiler-specific decorator such
as __attribute__((__deprecated__)) used by GNU compilers.
The cxx_alignas feature provides a macro definition
```<PREFIX>```_ALIGNAS which expands to either the standard alignas
decorator or a compiler-specific decorator such as
__attribute__ ((__aligned__)) used by GNU compilers.
The cxx_alignof feature provides a macro definition
```<PREFIX>```_ALIGNOF which expands to either the standard alignof
decorator or a compiler-specific decorator such as __alignof__
used by GNU compilers.








Feature
Define
Symbol
bare



cxx_alignas
```<PREFIX>```_ALIGNAS
alignas


cxx_alignof
```<PREFIX>```_ALIGNOF
alignof


cxx_nullptr
```<PREFIX>```_NULLPTR
nullptr
yes

cxx_static_assert
```<PREFIX>```_STATIC_ASSERT
static_assert


cxx_static_assert
```<PREFIX>```_STATIC_ASSERT_MSG
static_assert


cxx_attribute_deprecated
```<PREFIX>```_DEPRECATED
[[deprecated]]


cxx_attribute_deprecated
```<PREFIX>```_DEPRECATED_MSG
[[deprecated]]


cxx_thread_local
```<PREFIX>```_THREAD_LOCAL
thread_local




A use-case which arises with such deprecation macros is the deprecation
of an entire library.  In that case, all public API in the library may
be decorated with the ```<PREFIX>```_DEPRECATED macro.  This results in
very noisy build output when building the library itself, so the macro
may be may be defined to empty in that case when building the deprecated
library:
add_library(compat_support ${srcs})
target_compile_definitions(compat_support
  PRIVATE
    CompatSupport_DEPRECATED=
)


  

