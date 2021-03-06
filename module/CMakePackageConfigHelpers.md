  

# CMakePackageConfigHelpers  
Helpers functions for creating config files that can be included by other
projects to find and use a package.  

Adds the configure_package_config_file() and
write_basic_package_version_file() commands.  


Generating a Package Configuration File


configure_package_config_file
Create a config file for a project:
configure_package_config_file(```<input>``` ```<output>```
  INSTALL_DESTINATION ```<path>```
  [PATH_VARS ```<var1>``` ```<var2>``` ... ```<varN>```]
  [NO_SET_AND_CHECK_MACRO]
  [NO_CHECK_REQUIRED_COMPONENTS_MACRO]
  [INSTALL_PREFIX ```<path>```]
  )



configure_package_config_file() should be used instead of the plain
configure_file() command when creating the ```<PackageName>```Config.cmake
or ```<PackageName>```-config.cmake file for installing a project or library.
It helps making the resulting package relocatable by avoiding hardcoded paths
in the installed Config.cmake file.
In a FooConfig.cmake file there may be code like this to make the install
destinations know to the using project:
set(FOO_INCLUDE_DIR   "@CMAKE_INSTALL_FULL_INCLUDEDIR@" )
set(FOO_DATA_DIR   "@CMAKE_INSTALL_PREFIX@/@RELATIVE_DATA_INSTALL_DIR@" )
set(FOO_ICONS_DIR   "@CMAKE_INSTALL_PREFIX@/share/icons" )
#...logic to determine installedPrefix from the own location...
set(FOO_CONFIG_DIR  "${installedPrefix}/@CONFIG_INSTALL_DIR@" )


All 4 options shown above are not sufficient, since the first 3 hardcode the
absolute directory locations, and the 4th case works only if the logic to
determine the installedPrefix is correct, and if CONFIG_INSTALL_DIR
contains a relative path, which in general cannot be guaranteed.  This has the
effect that the resulting FooConfig.cmake file would work poorly under
Windows and OSX, where users are used to choose the install location of a
binary package at install time, independent from how
CMAKE_INSTALL_PREFIX was set at build/cmake time.
Using configure_package_config_file helps.  If used correctly, it makes
the resulting FooConfig.cmake file relocatable.  Usage:

write a FooConfig.cmake.in file as you are used to
insert a line containing only the string @PACKAGE_INIT@
instead of set(FOO_DIR "@SOME_INSTALL_DIR@"), use
set(FOO_DIR "@PACKAGE_SOME_INSTALL_DIR@") (this must be after the
@PACKAGE_INIT@ line)
instead of using the normal configure_file(), use
configure_package_config_file()

The ```<input>``` and ```<output>``` arguments are the input and output file, the
same way as in configure_file().
The ```<path>``` given to INSTALL_DESTINATION must be the destination where
the FooConfig.cmake file will be installed to.  This path can either be
absolute, or relative to the INSTALL_PREFIX path.
The variables ```<var1>``` to ```<varN>``` given as PATH_VARS are the
variables which contain install destinations.  For each of them the macro will
create a helper variable PACKAGE_```<var...>```.  These helper variables must be
used in the FooConfig.cmake.in file for setting the installed location.
They are calculated by configure_package_config_file so that they are
always relative to the installed location of the package.  This works both for
relative and also for absolute locations.  For absolute locations it works
only if the absolute location is a subdirectory of INSTALL_PREFIX.
If the INSTALL_PREFIX argument is passed, this is used as base path to
calculate all the relative paths.  The ```<path>``` argument must be an absolute
path.  If this argument is not passed, the CMAKE_INSTALL_PREFIX
variable will be used instead.  The default value is good when generating a
FooConfig.cmake file to use your package from the install tree.  When
generating a FooConfig.cmake file to use your package from the build tree this
option should be used.
By default configure_package_config_file also generates two helper macros,
set_and_check() and check_required_components() into the
FooConfig.cmake file.
set_and_check() should be used instead of the normal set() command for
setting directories and file locations.  Additionally to setting the variable
it also checks that the referenced file or directory actually exists and fails
with a FATAL_ERROR otherwise.  This makes sure that the created
FooConfig.cmake file does not contain wrong references.
When using the NO_SET_AND_CHECK_MACRO, this macro is not generated
into the FooConfig.cmake file.
check_required_components(```<PackageName>```) should be called at the end of
the FooConfig.cmake file. This macro checks whether all requested,
non-optional components have been found, and if this is not the case, sets
the Foo_FOUND variable to FALSE, so that the package is considered to
be not found.  It does that by testing the Foo_```<Component>```_FOUND
variables for all requested required components.  This macro should be
called even if the package doesn��t provide any components to make sure
users are not specifying components erroneously.  When using the
NO_CHECK_REQUIRED_COMPONENTS_MACRO option, this macro is not generated
into the FooConfig.cmake file.
For an example see below the documentation for
write_basic_package_version_file().
  


Generating a Package Version File


write_basic_package_version_file
Create a version file for a project:
write_basic_package_version_file(```<filename>```
  [VERSION ```<major.minor.patch>```]
  COMPATIBILITY ```<AnyNewerVersion|SameMajorVersion|SameMinorVersion|ExactVersion>```
  [ARCH_INDEPENDENT] )



Writes a file for use as ```<PackageName>```ConfigVersion.cmake file to
```<filename>```.  See the documentation of find_package() for
details on this.
```<filename>``` is the output filename, it should be in the build tree.
```<major.minor.patch>``` is the version number of the project to be installed.
If no VERSION is given, the PROJECT_VERSION variable is used.
If this hasn��t been set, it errors out.
The COMPATIBILITY mode AnyNewerVersion means that the installed
package version will be considered compatible if it is newer or exactly the
same as the requested version.  This mode should be used for packages which
are fully backward compatible, also across major versions.
If SameMajorVersion is used instead, then the behaviour differs from
AnyNewerVersion in that the major version number must be the same as
requested, e.g.  version 2.0 will not be considered compatible if 1.0 is
requested.  This mode should be used for packages which guarantee backward
compatibility within the same major version.
If SameMinorVersion is used, the behaviour is the same as
SameMajorVersion, but both major and minor version must be the same as
requested, e.g version 0.2 will not be compatible if 0.1 is requested.
If ExactVersion is used, then the package is only considered compatible if
the requested version matches exactly its own version number (not considering
the tweak version).  For example, version 1.2.3 of a package is only
considered compatible to requested version 1.2.3.  This mode is for packages
without compatibility guarantees.
If your project has more elaborated version matching rules, you will need to
write your own custom ConfigVersion.cmake file instead of using this
macro.
If ARCH_INDEPENDENT is given, the installed package version will be
considered compatible even if it was built for a different architecture than
the requested architecture.  Otherwise, an architecture check will be performed,
and the package will be considered compatible only if the architecture matches
exactly.  For example, if the package is built for a 32-bit architecture, the
package is only considered compatible if it is used on a 32-bit architecture,
unless ARCH_INDEPENDENT is given, in which case the package is considered
compatible on any architecture.

Note
ARCH_INDEPENDENT is intended for header-only libraries or similar
packages with no binaries.

Internally, this macro executes configure_file() to create the
resulting version file.  Depending on the COMPATIBILITY, the corresponding
BasicConfigVersion-```<COMPATIBILITY>```.cmake.in file is used.
Please note that these files are internal to CMake and you should not call
configure_file() on them yourself, but they can be used as starting
point to create more sophisticted custom ConfigVersion.cmake files.
  


Example Generating Package Files
Example using both configure_package_config_file() and
write_basic_package_version_file():
CMakeLists.txt:
set(INCLUDE_INSTALL_DIR include/ ... CACHE )
set(LIB_INSTALL_DIR lib/ ... CACHE )
set(SYSCONFIG_INSTALL_DIR etc/foo/ ... CACHE )
#...
include(CMakePackageConfigHelpers)
configure_package_config_file(FooConfig.cmake.in
  ${CMAKE_CURRENT_BINARY_DIR}/FooConfig.cmake
  INSTALL_DESTINATION ${LIB_INSTALL_DIR}/Foo/cmake
  PATH_VARS INCLUDE_INSTALL_DIR SYSCONFIG_INSTALL_DIR)
write_basic_package_version_file(
  ${CMAKE_CURRENT_BINARY_DIR}/FooConfigVersion.cmake
  VERSION 1.2.3
  COMPATIBILITY SameMajorVersion )
install(FILES ${CMAKE_CURRENT_BINARY_DIR}/FooConfig.cmake
              ${CMAKE_CURRENT_BINARY_DIR}/FooConfigVersion.cmake
        DESTINATION ${LIB_INSTALL_DIR}/Foo/cmake )


FooConfig.cmake.in:
set(FOO_VERSION x.y.z)
...
@PACKAGE_INIT@
...
set_and_check(FOO_INCLUDE_DIR "@PACKAGE_INCLUDE_INSTALL_DIR@")
set_and_check(FOO_SYSCONFIG_DIR "@PACKAGE_SYSCONFIG_INSTALL_DIR@")

check_required_components(Foo)


  

