  

# target_include_directories  
Add include directories to a target.  

target_include_directories(```<target>``` [SYSTEM] [BEFORE]
  ```<INTERFACE|PUBLIC|PRIVATE>``` [items1...]
  [```<INTERFACE|PUBLIC|PRIVATE>``` [items2...] ...])

  

Specifies include directories to use when compiling a given target.
The named ```<target>``` must have been created by a command such
as add_executable() or add_library() and must not be an
ALIAS target.  

If BEFORE is specified, the content will be prepended to the property
instead of being appended.  

The INTERFACE, PUBLIC and PRIVATE keywords are required to specify
the scope of the following arguments.  PRIVATE and PUBLIC items will
populate the INCLUDE_DIRECTORIES property of ```<target>```.
PUBLIC and INTERFACE items will populate the
INTERFACE_INCLUDE_DIRECTORIES property of ```<target>```.
(IMPORTED targets only support INTERFACE items.)
The following arguments specify include directories.  

Specified include directories may be absolute paths or relative paths.
Repeated calls for the same ```<target>``` append items in the order called.  If
SYSTEM is specified, the compiler will be told the
directories are meant as system include directories on some platforms
(signalling this setting might achieve effects such as the compiler
skipping warnings, or these fixed-install system files not being
considered in dependency calculations - see compiler docs).  If SYSTEM
is used together with PUBLIC or INTERFACE, the
INTERFACE_SYSTEM_INCLUDE_DIRECTORIES target property will be
populated with the specified directories.  

Arguments to target_include_directories may use ˇ°generator expressionsˇ±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  

Include directories usage requirements commonly differ between the build-tree
and the install-tree.  The BUILD_INTERFACE and INSTALL_INTERFACE
generator expressions can be used to describe separate usage requirements
based on the usage location.  Relative paths are allowed within the
INSTALL_INTERFACE expression and are interpreted relative to the
installation prefix.  For example:  

target_include_directories(mylib PUBLIC
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
  

