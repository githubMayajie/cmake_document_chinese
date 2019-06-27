  

# CMakeExpandImportedTargets  

Deprecated since version 3.4: Do not use.
  

This module was once needed to expand imported targets to the underlying
libraries they reference on disk for use with the try_compile()
and try_run() commands.  These commands now support imported
libraries in their LINK_LIBRARIES options (since CMake 2.8.11
for try_compile() and since CMake 3.2 for try_run()).  

This module does not support the policy CMP0022 NEW
behavior or use of the INTERFACE_LINK_LIBRARIES property
because generator expressions
cannot be evaluated during configuration.  

CMAKE_EXPAND_IMPORTED_TARGETS(```<var>``` LIBRARIES lib1 lib2...libN
                              [CONFIGURATION ```<config>```])

  

CMAKE_EXPAND_IMPORTED_TARGETS() takes a list of libraries and replaces
all imported targets contained in this list with their actual file
paths of the referenced libraries on disk, including the libraries
from their link interfaces.  If a CONFIGURATION is given, it uses the
respective configuration of the imported targets if it exists.  If no
CONFIGURATION is given, it uses the first configuration from
${CMAKE_CONFIGURATION_TYPES} if set, otherwise ${CMAKE_BUILD_TYPE}.  

cmake_expand_imported_targets(expandedLibs
  LIBRARIES ${CMAKE_REQUIRED_LIBRARIES}
  CONFIGURATION "${CMAKE_TRY_COMPILE_CONFIGURATION}" )

  

