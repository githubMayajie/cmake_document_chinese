  

# find_package  

Contents

find_package
Basic Signature and Module Mode
Full Signature and Config Mode
Version Selection
Search Procedure
Package File Interface Variables



  

Find an external project, and load its settings.  


Basic Signature and Module Mode
find_package(```<PackageName>``` [version] [EXACT] [QUIET] [MODULE]
             [REQUIRED] [[COMPONENTS] [components...]]
             [OPTIONAL_COMPONENTS components...]
             [NO_POLICY_SCOPE])


Finds and loads settings from an external project.  ```<PackageName>```_FOUND
will be set to indicate whether the package was found.  When the
package is found package-specific information is provided through
variables and Imported Targets documented by the package itself.  The
QUIET option disables informational messages, including those indicating
that the package cannot be found if it is not REQUIRED.  The REQUIRED
option stops processing with an error message if the package cannot be found.
A package-specific list of required components may be listed after the
COMPONENTS option (or after the REQUIRED option if present).
Additional optional components may be listed after
OPTIONAL_COMPONENTS.  Available components and their influence on
whether a package is considered to be found are defined by the target
package.
The [version] argument requests a version with which the package found
should be compatible (format is major[.minor[.patch[.tweak]]]).  The
EXACT option requests that the version be matched exactly.  If no
[version] and/or component list is given to a recursive invocation
inside a find-module, the corresponding arguments are forwarded
automatically from the outer call (including the EXACT flag for
[version]).  Version support is currently provided only on a
package-by-package basis (see the Version Selection section below).
See the cmake_policy() command documentation for discussion
of the NO_POLICY_SCOPE option.
The command has two modes by which it searches for packages: ��Module��
mode and ��Config�� mode.  The above signature selects Module mode.
If no module is found the command falls back to Config mode, described
below. This fall back is disabled if the MODULE option is given.
In Module mode, CMake searches for a file called Find```<PackageName>```.cmake.
The file is first searched in the CMAKE_MODULE_PATH,
then among the Find Modules provided by the CMake installation.
If the file is found, it is read and processed by CMake.  It is responsible
for finding the package, checking the version, and producing any needed
messages.  Some find-modules provide limited or no support for versioning;
check the module documentation.
If the MODULE option is not specfied in the above signature,
CMake first searches for the package using Module mode. Then, if the
package is not found, it searches again using Config mode. A user
may set the variable CMAKE_FIND_PACKAGE_PREFER_CONFIG to
TRUE to direct CMake first search using Config mode before falling
back to Module mode.
  


Full Signature and Config Mode
User code should generally look for packages using the above basic
signature.  The remainder of this command documentation specifies the
full command signature and details of the search process.  Project
maintainers wishing to provide a package to be found by this command
are encouraged to read on.
The complete Config mode command signature is
find_package(```<PackageName>``` [version] [EXACT] [QUIET]
             [REQUIRED] [[COMPONENTS] [components...]]
             [CONFIG|NO_MODULE]
             [NO_POLICY_SCOPE]
             [NAMES name1 [name2 ...]]
             [CONFIGS config1 [config2 ...]]
             [HINTS path1 [path2 ... ]]
             [PATHS path1 [path2 ... ]]
             [PATH_SUFFIXES suffix1 [suffix2 ...]]
             [NO_DEFAULT_PATH]
             [NO_PACKAGE_ROOT_PATH]
             [NO_CMAKE_PATH]
             [NO_CMAKE_ENVIRONMENT_PATH]
             [NO_SYSTEM_ENVIRONMENT_PATH]
             [NO_CMAKE_PACKAGE_REGISTRY]
             [NO_CMAKE_BUILDS_PATH] # Deprecated; does nothing.
             [NO_CMAKE_SYSTEM_PATH]
             [NO_CMAKE_SYSTEM_PACKAGE_REGISTRY]
             [CMAKE_FIND_ROOT_PATH_BOTH |
              ONLY_CMAKE_FIND_ROOT_PATH |
              NO_CMAKE_FIND_ROOT_PATH])


The CONFIG option, the synonymous NO_MODULE option, or the use
of options not specified in the basic signature all enforce pure Config
mode.  In pure Config mode, the command skips Module mode search and
proceeds at once with Config mode search.
Config mode search attempts to locate a configuration file provided by the
package to be found.  A cache entry called ```<PackageName>```_DIR is created to
hold the directory containing the file.  By default the command
searches for a package with the name ```<PackageName>```.  If the NAMES option
is given the names following it are used instead of ```<PackageName>```.
The command searches for a file called ```<PackageName>```Config.cmake or
```<lower-case-package-name>```-config.cmake for each name specified.
A replacement set of possible configuration file names may be given
using the CONFIGS option.  The search procedure is specified below.
Once found, the configuration file is read and processed by CMake.
Since the file is provided by the package it already knows the
location of package contents.  The full path to the configuration file
is stored in the cmake variable ```<PackageName>```_CONFIG.
All configuration files which have been considered by CMake while
searching for an installation of the package with an appropriate
version are stored in the cmake variable ```<PackageName>```_CONSIDERED_CONFIGS,
the associated versions in ```<PackageName>```_CONSIDERED_VERSIONS.
If the package configuration file cannot be found CMake will generate
an error describing the problem unless the QUIET argument is
specified.  If REQUIRED is specified and the package is not found a
fatal error is generated and the configure step stops executing.  If
```<PackageName>```_DIR has been set to a directory not containing a
configuration file CMake will ignore it and search from scratch.
Package maintainers providing CMake package configuration files are
encouraged to name and install them such that the Search Procedure
outlined below will find them without requiring use of additional options.
  


Version Selection
When the [version] argument is given Config mode will only find a
version of the package that claims compatibility with the requested
version (format is major[.minor[.patch[.tweak]]]).  If the EXACT
option is given only a version of the package claiming an exact match
of the requested version may be found.  CMake does not establish any
convention for the meaning of version numbers.  Package version
numbers are checked by ��version�� files provided by the packages
themselves.  For a candidate package configuration file
```<config-file>```.cmake the corresponding version file is located next
to it and named either ```<config-file>```-version.cmake or
```<config-file>```Version.cmake.  If no such version file is available
then the configuration file is assumed to not be compatible with any
requested version.  A basic version file containing generic version
matching code can be created using the
CMakePackageConfigHelpers module.  When a version file
is found it is loaded to check the requested version number.  The
version file is loaded in a nested scope in which the following
variables have been defined:

PACKAGE_FIND_NAME
the ```<PackageName>```
PACKAGE_FIND_VERSION
full requested version string
PACKAGE_FIND_VERSION_MAJOR
major version if requested, else 0
PACKAGE_FIND_VERSION_MINOR
minor version if requested, else 0
PACKAGE_FIND_VERSION_PATCH
patch version if requested, else 0
PACKAGE_FIND_VERSION_TWEAK
tweak version if requested, else 0
PACKAGE_FIND_VERSION_COUNT
number of version components, 0 to 4

The version file checks whether it satisfies the requested version and
sets these variables:

PACKAGE_VERSION
full provided version string
PACKAGE_VERSION_EXACT
true if version is exact match
PACKAGE_VERSION_COMPATIBLE
true if version is compatible
PACKAGE_VERSION_UNSUITABLE
true if unsuitable as any version

These variables are checked by the find_package command to determine
whether the configuration file provides an acceptable version.  They
are not available after the find_package call returns.  If the version
is acceptable the following variables are set:

```<PackageName>```_VERSION
full provided version string
```<PackageName>```_VERSION_MAJOR
major version if provided, else 0
```<PackageName>```_VERSION_MINOR
minor version if provided, else 0
```<PackageName>```_VERSION_PATCH
patch version if provided, else 0
```<PackageName>```_VERSION_TWEAK
tweak version if provided, else 0
```<PackageName>```_VERSION_COUNT
number of version components, 0 to 4

and the corresponding package configuration file is loaded.
When multiple package configuration files are available whose version files
claim compatibility with the version requested it is unspecified which
one is chosen: unless the variable CMAKE_FIND_PACKAGE_SORT_ORDER
is set no attempt is made to choose a highest or closest version number.
To control the order in which find_package checks for compatibility use
the two variables CMAKE_FIND_PACKAGE_SORT_ORDER and
CMAKE_FIND_PACKAGE_SORT_DIRECTION.
For instance in order to select the highest version one can set
SET(CMAKE_FIND_PACKAGE_SORT_ORDER NATURAL)
SET(CMAKE_FIND_PACKAGE_SORT_DIRECTION DEC)


before calling find_package.
  


Search Procedure
CMake constructs a set of possible installation prefixes for the
package.  Under each prefix several directories are searched for a
configuration file.  The tables below show the directories searched.
Each entry is meant for installation trees following Windows (W), UNIX
(U), or Apple (A) conventions:
```<prefix>```/                                                       (W)
```<prefix>```/(cmake|CMake)/                                         (W)
```<prefix>```/```<name>```*/                                               (W)
```<prefix>```/```<name>```*/(cmake|CMake)/                                 (W)
```<prefix>```/(lib/```<arch>```|lib*|share)/cmake/```<name>```*/                 (U)
```<prefix>```/(lib/```<arch>```|lib*|share)/```<name>```*/                       (U)
```<prefix>```/(lib/```<arch>```|lib*|share)/```<name>```*/(cmake|CMake)/         (U)
```<prefix>```/```<name>```*/(lib/```<arch>```|lib*|share)/cmake/```<name>```*/         (W/U)
```<prefix>```/```<name>```*/(lib/```<arch>```|lib*|share)/```<name>```*/               (W/U)
```<prefix>```/```<name>```*/(lib/```<arch>```|lib*|share)/```<name>```*/(cmake|CMake)/ (W/U)


On systems supporting macOS FRAMEWORK and BUNDLE, the
following directories are searched for Frameworks or Application Bundles
containing a configuration file:
```<prefix>```/```<name>```.framework/Resources/                    (A)
```<prefix>```/```<name>```.framework/Resources/CMake/              (A)
```<prefix>```/```<name>```.framework/Versions/*/Resources/         (A)
```<prefix>```/```<name>```.framework/Versions/*/Resources/CMake/   (A)
```<prefix>```/```<name>```.app/Contents/Resources/                 (A)
```<prefix>```/```<name>```.app/Contents/Resources/CMake/           (A)


In all cases the ```<name>``` is treated as case-insensitive and corresponds
to any of the names specified (```<PackageName>``` or names given by NAMES).
Paths with lib/```<arch>``` are enabled if the
CMAKE_LIBRARY_ARCHITECTURE variable is set. lib* includes one
or more of the values lib64, lib32, libx32 or lib (searched in
that order).

Paths with lib64 are searched on 64 bit platforms if the
FIND_LIBRARY_USE_LIB64_PATHS property is set to TRUE.
Paths with lib32 are searched on 32 bit platforms if the
FIND_LIBRARY_USE_LIB32_PATHS property is set to TRUE.
Paths with libx32 are searched on platforms using the x32 ABI
if the FIND_LIBRARY_USE_LIBX32_PATHS property is set to TRUE.
The lib path is always searched.

If PATH_SUFFIXES is specified, the suffixes are appended to each
(W) or (U) directory entry one-by-one.
This set of directories is intended to work in cooperation with
projects that provide configuration files in their installation trees.
Directories above marked with (W) are intended for installations on
Windows where the prefix may point at the top of an application��s
installation directory.  Those marked with (U) are intended for
installations on UNIX platforms where the prefix is shared by multiple
packages.  This is merely a convention, so all (W) and (U) directories
are still searched on all platforms.  Directories marked with (A) are
intended for installations on Apple platforms.  The
CMAKE_FIND_FRAMEWORK and CMAKE_FIND_APPBUNDLE
variables determine the order of preference.
The set of installation prefixes is constructed using the following
steps.  If NO_DEFAULT_PATH is specified all NO_* options are
enabled.

Search paths specified in the ```<PackageName>```_ROOT CMake
variable and the ```<PackageName>```_ROOT environment variable,
where ```<PackageName>``` is the package to be found.
The package root variables are maintained as a stack so if
called from within a find module, root paths from the parent��s find
module will also be searched after paths for the current package.
This can be skipped if NO_PACKAGE_ROOT_PATH is passed.
See policy CMP0074.

Search paths specified in cmake-specific cache variables.  These
are intended to be used on the command line with a -DVAR=value.
The values are interpreted as semicolon-separated lists.
This can be skipped if NO_CMAKE_PATH is passed:
CMAKE_PREFIX_PATH
CMAKE_FRAMEWORK_PATH
CMAKE_APPBUNDLE_PATH



Search paths specified in cmake-specific environment variables.
These are intended to be set in the user��s shell configuration,
and therefore use the host��s native path separator
(; on Windows and : on UNIX).
This can be skipped if NO_CMAKE_ENVIRONMENT_PATH is passed:
```<PackageName>```_DIR
CMAKE_PREFIX_PATH
CMAKE_FRAMEWORK_PATH
CMAKE_APPBUNDLE_PATH



Search paths specified by the HINTS option.  These should be paths
computed by system introspection, such as a hint provided by the
location of another item already found.  Hard-coded guesses should
be specified with the PATHS option.

Search the standard system environment variables.  This can be
skipped if NO_SYSTEM_ENVIRONMENT_PATH is passed.  Path entries
ending in /bin or /sbin are automatically converted to their
parent directories:
PATH



Search paths stored in the CMake User Package Registry.
This can be skipped if NO_CMAKE_PACKAGE_REGISTRY is passed or by
setting the CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
to TRUE.
See the cmake-packages(7) manual for details on the user
package registry.

Search cmake variables defined in the Platform files for the
current system.  This can be skipped if NO_CMAKE_SYSTEM_PATH is
passed:
CMAKE_SYSTEM_PREFIX_PATH
CMAKE_SYSTEM_FRAMEWORK_PATH
CMAKE_SYSTEM_APPBUNDLE_PATH



Search paths stored in the CMake System Package Registry.
This can be skipped if NO_CMAKE_SYSTEM_PACKAGE_REGISTRY is passed
or by setting the
CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY to TRUE.
See the cmake-packages(7) manual for details on the system
package registry.

Search paths specified by the PATHS option.  These are typically
hard-coded guesses.


The CMake variable CMAKE_FIND_ROOT_PATH specifies one or more
directories to be prepended to all other search directories.  This
effectively ��re-roots�� the entire search under given locations.
Paths which are descendants of the CMAKE_STAGING_PREFIX are excluded
from this re-rooting, because that variable is always a path on the host system.
By default the CMAKE_FIND_ROOT_PATH is empty.
The CMAKE_SYSROOT variable can also be used to specify exactly one
directory to use as a prefix.  Setting CMAKE_SYSROOT also has other
effects.  See the documentation for that variable for more.
These variables are especially useful when cross-compiling to
point to the root directory of the target environment and CMake will
search there too.  By default at first the directories listed in
CMAKE_FIND_ROOT_PATH are searched, then the CMAKE_SYSROOT
directory is searched, and then the non-rooted directories will be
searched.  The default behavior can be adjusted by setting
CMAKE_FIND_ROOT_PATH_MODE_PACKAGE.  This behavior can be manually
overridden on a per-call basis using options:

CMAKE_FIND_ROOT_PATH_BOTH
Search in the order described above.
NO_CMAKE_FIND_ROOT_PATH
Do not use the CMAKE_FIND_ROOT_PATH variable.
ONLY_CMAKE_FIND_ROOT_PATH
Search only the re-rooted directories and directories below
CMAKE_STAGING_PREFIX.

The default search order is designed to be most-specific to
least-specific for common use cases.
Projects may override the order by simply calling the command
multiple times and using the NO_* options:

find_package (```<PackageName>``` PATHS paths... NO_DEFAULT_PATH)
find_package (```<PackageName>```)

Once one of the calls succeeds the result variable will be set
and stored in the cache so that no call will search again.
By default the value stored in the result variable will be the path at
which the file is found.  The CMAKE_FIND_PACKAGE_RESOLVE_SYMLINKS
variable may be set to TRUE before calling find_package in order
to resolve symbolic links and store the real path to the file.
Every non-REQUIRED find_package call can be disabled by setting the
CMAKE_DISABLE_FIND_PACKAGE_```<PackageName>``` variable to TRUE.
  


Package File Interface Variables
When loading a find module or package configuration file find_package
defines variables to provide information about the call arguments (and
restores their original state before returning):

CMAKE_FIND_PACKAGE_NAME
the ```<PackageName>``` which is searched for
```<PackageName>```_FIND_REQUIRED
true if REQUIRED option was given
```<PackageName>```_FIND_QUIETLY
true if QUIET option was given
```<PackageName>```_FIND_VERSION
full requested version string
```<PackageName>```_FIND_VERSION_MAJOR
major version if requested, else 0
```<PackageName>```_FIND_VERSION_MINOR
minor version if requested, else 0
```<PackageName>```_FIND_VERSION_PATCH
patch version if requested, else 0
```<PackageName>```_FIND_VERSION_TWEAK
tweak version if requested, else 0
```<PackageName>```_FIND_VERSION_COUNT
number of version components, 0 to 4
```<PackageName>```_FIND_VERSION_EXACT
true if EXACT option was given
```<PackageName>```_FIND_COMPONENTS
list of requested components
```<PackageName>```_FIND_REQUIRED_```<c>```
true if component ```<c>``` is required,
false if component ```<c>``` is optional

In Module mode the loaded find module is responsible to honor the
request detailed by these variables; see the find module for details.
In Config mode find_package handles REQUIRED, QUIET, and
[version] options automatically but leaves it to the package
configuration file to handle components in a way that makes sense
for the package.  The package configuration file may set
```<PackageName>```_FOUND to false to tell find_package that component
requirements are not satisfied.
  

