  

# GenerateExportHeader  
Function for generation of export macros for libraries  

This module provides the function GENERATE_EXPORT_HEADER().  

The GENERATE_EXPORT_HEADER function can be used to generate a file
suitable for preprocessor inclusion which contains EXPORT macros to be
used in library classes:  

GENERATE_EXPORT_HEADER( LIBRARY_TARGET
          [BASE_NAME ```<base_name>```]
          [EXPORT_MACRO_NAME ```<export_macro_name>```]
          [EXPORT_FILE_NAME ```<export_file_name>```]
          [DEPRECATED_MACRO_NAME ```<deprecated_macro_name>```]
          [NO_EXPORT_MACRO_NAME ```<no_export_macro_name>```]
          [INCLUDE_GUARD_NAME ```<include_guard_name>```]
          [STATIC_DEFINE ```<static_define>```]
          [NO_DEPRECATED_MACRO_NAME ```<no_deprecated_macro_name>```]
          [DEFINE_NO_DEPRECATED]
          [PREFIX_NAME ```<prefix_name>```]
          [CUSTOM_CONTENT_FROM_VARIABLE ```<variable>```]
)

  

The target properties CXX_VISIBILITY_PRESET
and VISIBILITY_INLINES_HIDDEN can be used to add the appropriate
compile flags for targets.  See the documentation of those target properties,
and the convenience variables
CMAKE_CXX_VISIBILITY_PRESET and
CMAKE_VISIBILITY_INLINES_HIDDEN.  

By default GENERATE_EXPORT_HEADER() generates macro names in a file
name determined by the name of the library.  This means that in the
simplest case, users of GenerateExportHeader will be equivalent to:  

set(CMAKE_CXX_VISIBILITY_PRESET hidden)
set(CMAKE_VISIBILITY_INLINES_HIDDEN 1)
add_library(somelib someclass.cpp)
generate_export_header(somelib)
install(TARGETS somelib DESTINATION ${LIBRARY_INSTALL_DIR})
install(FILES
 someclass.h
 ${PROJECT_BINARY_DIR}/somelib_export.h DESTINATION ${INCLUDE_INSTALL_DIR}
)

  

And in the ABI header files:  

#include "somelib_export.h"
class SOMELIB_EXPORT SomeClass {
  ...
};

  

The CMake fragment will generate a file in the
${CMAKE_CURRENT_BINARY_DIR} called somelib_export.h containing the
macros SOMELIB_EXPORT, SOMELIB_NO_EXPORT, SOMELIB_DEPRECATED,
SOMELIB_DEPRECATED_EXPORT and SOMELIB_DEPRECATED_NO_EXPORT.
They will be followed by content taken from the variable specified by
the CUSTOM_CONTENT_FROM_VARIABLE option, if any.
The resulting file should be installed with other headers in the library.  

The BASE_NAME argument can be used to override the file name and the
names used for the macros:  

add_library(somelib someclass.cpp)
generate_export_header(somelib
  BASE_NAME other_name
)

  

Generates a file called other_name_export.h containing the macros
OTHER_NAME_EXPORT, OTHER_NAME_NO_EXPORT and OTHER_NAME_DEPRECATED
etc.  

The BASE_NAME may be overridden by specifying other options in the
function.  For example:  

add_library(somelib someclass.cpp)
generate_export_header(somelib
  EXPORT_MACRO_NAME OTHER_NAME_EXPORT
)

  

creates the macro OTHER_NAME_EXPORT instead of SOMELIB_EXPORT, but
other macros and the generated file name is as default:  

add_library(somelib someclass.cpp)
generate_export_header(somelib
  DEPRECATED_MACRO_NAME KDE_DEPRECATED
)

  

creates the macro KDE_DEPRECATED instead of SOMELIB_DEPRECATED.  

If LIBRARY_TARGET is a static library, macros are defined without
values.  

If the same sources are used to create both a shared and a static
library, the uppercased symbol ${BASE_NAME}_STATIC_DEFINE should be
used when building the static library:  

add_library(shared_variant SHARED ${lib_SRCS})
add_library(static_variant ${lib_SRCS})
generate_export_header(shared_variant BASE_NAME libshared_and_static)
set_target_properties(static_variant PROPERTIES
  COMPILE_FLAGS -DLIBSHARED_AND_STATIC_STATIC_DEFINE)

  

This will cause the export macros to expand to nothing when building
the static library.  

If DEFINE_NO_DEPRECATED is specified, then a macro
${BASE_NAME}_NO_DEPRECATED will be defined This macro can be used to
remove deprecated code from preprocessor output:  

option(EXCLUDE_DEPRECATED "Exclude deprecated parts of the library" FALSE)
if (EXCLUDE_DEPRECATED)
  set(NO_BUILD_DEPRECATED DEFINE_NO_DEPRECATED)
endif()
generate_export_header(somelib ${NO_BUILD_DEPRECATED})

  

And then in somelib:  

class SOMELIB_EXPORT SomeClass
{
public:
#ifndef SOMELIB_NO_DEPRECATED
  SOMELIB_DEPRECATED void oldMethod();
#endif
};

  

#ifndef SOMELIB_NO_DEPRECATED
void SomeClass::oldMethod() {  }
#endif

  

If PREFIX_NAME is specified, the argument will be used as a prefix to
all generated macros.  

For example:  

generate_export_header(somelib PREFIX_NAME VTK_)

  

Generates the macros VTK_SOMELIB_EXPORT etc.  

ADD_COMPILER_EXPORT_FLAGS( [```<output_variable>```] )

  

The ADD_COMPILER_EXPORT_FLAGS function adds -fvisibility=hidden to
CMAKE_CXX_FLAGS if supported, and is a no-op
on Windows which does not need extra compiler flags for exporting support.
You may optionally pass a single argument to ADD_COMPILER_EXPORT_FLAGS
that will be populated with the CXX_FLAGS required to enable visibility
support for the compiler/architecture in use.  

This function is deprecated.  Set the target properties
CXX_VISIBILITY_PRESET and
VISIBILITY_INLINES_HIDDEN instead.  

