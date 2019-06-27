  

# INTERFACE_SYSTEM_INCLUDE_DIRECTORIES  
List of public system include directories for a library.  

Targets may populate this property to publish the include directories
which contain system headers, and therefore should not result in
compiler warnings.  The target_include_directories(SYSTEM)
command signature populates this property with values given to the
PUBLIC and INTERFACE keywords.  

Projects may also get and set the property directly, but must be aware that
adding directories to this property does not make those directories used
during compilation.  Adding directories to this property marks directories
as SYSTEM which otherwise would be used in a non-SYSTEM manner.  This
can appear similar to ¡®duplication¡¯, so prefer the
high-level target_include_directories(SYSTEM) command and avoid
setting the property by low-level means.  

When target dependencies are specified using target_link_libraries(),
CMake will read this property from all target dependencies to mark the
same include directories as containing system headers.  

Contents of INTERFACE_SYSTEM_INCLUDE_DIRECTORIES may use ¡°generator
expressions¡± with the syntax $```<...>```.  See the
cmake-generator-expressions(7) manual for available expressions.
See the cmake-buildsystem(7) manual for more on defining
buildsystem properties.  

