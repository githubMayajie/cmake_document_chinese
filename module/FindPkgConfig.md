  

# FindPkgConfig  
A pkg-config module for CMake.  

Finds the pkg-config executable and adds the pkg_get_variable(),
pkg_check_modules() and pkg_search_module() commands. The
following variables will also be set:  


PKG_CONFIG_FOUND
if pkg-config executable was found
PKG_CONFIG_EXECUTABLE
pathname of the pkg-config program
PKG_CONFIG_VERSION_STRING
version of pkg-config (since CMake 2.8.8)
  



pkg_check_modules
Checks for all the given modules, setting a variety of result variables in
the calling scope.
pkg_check_modules(```<prefix>```
                  [REQUIRED] [QUIET]
                  [NO_CMAKE_PATH]
                  [NO_CMAKE_ENVIRONMENT_PATH]
                  [IMPORTED_TARGET [GLOBAL]]
                  ```<moduleSpec>``` [```<moduleSpec>```...])


When the REQUIRED argument is given, the command will fail with an error
if module(s) could not be found.
When the QUIET argument is given, no status messages will be printed.
By default, if CMAKE_MINIMUM_REQUIRED_VERSION is 3.1 or
later, or if PKG_CONFIG_USE_CMAKE_PREFIX_PATH is set to a
boolean True value, then the CMAKE_PREFIX_PATH,
CMAKE_FRAMEWORK_PATH, and CMAKE_APPBUNDLE_PATH cache
and environment variables will be added to the pkg-config search path.
The NO_CMAKE_PATH and NO_CMAKE_ENVIRONMENT_PATH arguments
disable this behavior for the cache variables and environment variables
respectively.
The IMPORTED_TARGET argument will create an imported target named
PkgConfig::```<prefix>``` that can be passed directly as an argument to
target_link_libraries(). The GLOBAL argument will make the
imported target available in global scope.
Each ```<moduleSpec>``` can be either a bare module name or it can be a
module name with a version constraint (operators =, ```<, >```,
```<= and >```= are supported).  The following are examples for a module
named foo with various constraints:

foo matches any version.
foo```<2 only matches versions before 2.
foo>```=3.1 matches any version from 3.1 or later.
foo=1.2.3 requires that foo must be exactly version 1.2.3.

The following variables may be set upon return.  Two sets of values exist:
One for the common case (```<XXX>``` = ```<prefix>```) and another for the
information pkg-config provides when called with the --static
option (```<XXX>``` = ```<prefix>```_STATIC).

```<XXX>```_FOUND
set to 1 if module(s) exist
```<XXX>```_LIBRARIES
only the libraries (without the ¡®-l¡¯)
```<XXX>```_LINK_LIBRARIES
the libraries and their absolute paths
```<XXX>```_LIBRARY_DIRS
the paths of the libraries (without the ¡®-L¡¯)
```<XXX>```_LDFLAGS
all required linker flags
```<XXX>```_LDFLAGS_OTHER
all other linker flags
```<XXX>```_INCLUDE_DIRS
the ¡®-I¡¯ preprocessor flags (without the ¡®-I¡¯)
```<XXX>```_CFLAGS
all required cflags
```<XXX>```_CFLAGS_OTHER
the other compiler flags

All but ```<XXX>```_FOUND may be a ;-list if the
associated variable returned from pkg-config has multiple values.
There are some special variables whose prefix depends on the number of
```<moduleSpec>``` given.  When there is only one ```<moduleSpec>```,
```<YYY>``` will simply be ```<prefix>```, but if two or more ```<moduleSpec>```
items are given, ```<YYY>``` will be ```<prefix>```_```<moduleName>```.

```<YYY>```_VERSION
version of the module
```<YYY>```_PREFIX
prefix directory of the module
```<YYY>```_INCLUDEDIR
include directory of the module
```<YYY>```_LIBDIR
lib directory of the module

Examples:
pkg_check_modules (GLIB2 glib-2.0)


Looks for any version of glib2.  If found, the output variable
GLIB2_VERSION will hold the actual version found.
pkg_check_modules (GLIB2 glib-2.0>```=2.10)


Looks for at least version 2.10 of glib2.  If found, the output variable
GLIB2_VERSION will hold the actual version found.
pkg_check_modules (FOO glib-2.0>```=2.10 gtk+-2.0)


Looks for both glib2-2.0 (at least version 2.10) and any version of
gtk2+-2.0.  Only if both are found will FOO be considered found.
The FOO_glib-2.0_VERSION and FOO_gtk+-2.0_VERSION variables will be
set to their respective found module versions.
pkg_check_modules (XRENDER REQUIRED xrender)


Requires any version of xrender.  Example output variables set by a
successful call:
XRENDER_LIBRARIES=Xrender;X11
XRENDER_STATIC_LIBRARIES=Xrender;X11;pthread;Xau;Xdmcp


  



pkg_search_module
The behavior of this command is the same as pkg_check_modules(),
except that rather than checking for all the specified modules, it searches
for just the first successful match.
pkg_search_module(```<prefix>```
                  [REQUIRED] [QUIET]
                  [NO_CMAKE_PATH]
                  [NO_CMAKE_ENVIRONMENT_PATH]
                  [IMPORTED_TARGET [GLOBAL]]
                  ```<moduleSpec>``` [```<moduleSpec>```...])


Example:
pkg_search_module (BAR libxml-2.0 libxml2 libxml>```=2)


  



pkg_get_variable
Retrieves the value of a pkg-config variable varName and stores it in the
result variable resultVar in the calling scope.
pkg_get_variable(```<resultVar>``` ```<moduleName>``` ```<varName>```)


If pkg-config returns multiple values for the specified variable,
resultVar will contain a ;-list.
For example:
pkg_get_variable(GI_GIRDIR gobject-introspection-1.0 girdir)


  


Variables Affecting Behavior


PKG_CONFIG_EXECUTABLE
This can be set to the path of the pkg-config executable.  If not provided,
it will be set by the module as a result of calling find_program()
internally.  The PKG_CONFIG environment variable can be used as a hint.



PKG_CONFIG_USE_CMAKE_PREFIX_PATH
Specifies whether pkg_check_modules() and
pkg_search_module() should add the paths in the
CMAKE_PREFIX_PATH, CMAKE_FRAMEWORK_PATH and
CMAKE_APPBUNDLE_PATH cache and environment variables to the
pkg-config search path.
If this variable is not set, this behavior is enabled by default if
CMAKE_MINIMUM_REQUIRED_VERSION is 3.1 or later, disabled
otherwise.

  

