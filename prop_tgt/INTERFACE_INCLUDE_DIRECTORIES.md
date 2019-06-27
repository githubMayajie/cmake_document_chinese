  

# INTERFACE_INCLUDE_DIRECTORIES  
List of public include directories requirements for a library.  

Targets may populate this property to publish the include directories
required to compile against the headers for the target.  The target_include_directories()
command populates this property with values given to the PUBLIC and
INTERFACE keywords.  Projects may also get and set the property directly.  

When target dependencies are specified using target_link_libraries(),
CMake will read this property from all target dependencies to determine the
build properties of the consumer.  

Contents of INTERFACE_INCLUDE_DIRECTORIES may use ¡°generator expressions¡±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
-manual for more on defining buildsystem properties.  

Include directories usage requirements commonly differ between the build-tree
and the install-tree.  The BUILD_INTERFACE and INSTALL_INTERFACE
generator expressions can be used to describe separate usage requirements
based on the usage location.  Relative paths are allowed within the
INSTALL_INTERFACE expression and are interpreted relative to the
installation prefix.  For example:  

target_include_directories(mylib INTERFACE
  $```<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include/mylib>```
  $```<INSTALL_INTERFACE:include/mylib>```  # ```<prefix>```/include/mylib
)

  


Creating Relocatable Packages
Note that it is not advisable to populate the INSTALL_INTERFACE of the
INTERFACE_INCLUDE_DIRECTORIES of a target with absolute paths to the include
directories of dependencies.  That would hard-code into installed packages
the include directory paths for dependencies
as found on the machine the package was made on.
The INSTALL_INTERFACE of the INTERFACE_INCLUDE_DIRECTORIES is only
suitable for specifying the required include directories for headers
provided with the target itself, not those provided by the transitive
dependencies listed in its INTERFACE_LINK_LIBRARIES target
property.  Those dependencies should themselves be targets that specify
their own header locations in INTERFACE_INCLUDE_DIRECTORIES.
See the Creating Relocatable Packages section of the
cmake-packages(7) manual for discussion of additional care
that must be taken when specifying usage requirements while creating
packages for redistribution.
  

