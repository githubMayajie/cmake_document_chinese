  

# CPack  
Build binary and source package installers.  


Introduction
The CPack module generates a file CPackConfig.cmake intended for
use in a subsequent run of  the cpack program
where it steers the generation of installers or/and source packages.
Inclusion of the CPack module adds two new build targets, package
and package_source, which build the binary and source installers
respectively.  The generated binary installers contain everything
installed via CMake¡¯s install() command (and the deprecated
commands install_files(), install_programs(), and
install_targets()).
For certain kinds of binary installers (including the graphical
installers on macOS and Windows), CPack generates installers that
allow users to select individual application components to install.
See CPackComponent module for further details.
  


CPack Generators
The CPACK_GENERATOR variable has different meanings in different
contexts.  In a CMakeLists.txt file, CPACK_GENERATOR is a
list of generators: and when cpack is run with no other
arguments, it will iterate over that list and produce one package for each
generator.  In a CPACK_PROJECT_CONFIG_FILE,
CPACK_GENERATOR is a string naming a single generator.  If you
need per-cpack-generator logic to control other cpack settings, then you
need a CPACK_PROJECT_CONFIG_FILE.
The CMake source tree itself contains a CPACK_PROJECT_CONFIG_FILE.
See the top level file CMakeCPackOptions.cmake.in for an example.
If set, the CPACK_PROJECT_CONFIG_FILE is included automatically
on a per-generator basis.  It only need contain overrides.
Here¡¯s how it works:

cpack runs
it includes CPackConfig.cmake
it iterates over the generators given by the -G command line option,
or if no such option was specified, over the list of generators given by
the CPACK_GENERATOR variable set in the CPackConfig.cmake
input file.
foreach generator, it then
sets CPACK_GENERATOR to the one currently being iterated
includes the CPACK_PROJECT_CONFIG_FILE
produces the package for that generator



This is the key: For each generator listed in CPACK_GENERATOR in
CPackConfig.cmake, cpack will reset CPACK_GENERATOR
internally to the one currently being used and then include the
CPACK_PROJECT_CONFIG_FILE.
  


Variables common to all CPack Generators
Before including this CPack module in your CMakeLists.txt file, there
are a variety of variables that can be set to customize the resulting
installers.  The most commonly-used variables are:


CPACK_PACKAGE_NAME
The name of the package (or application).  If not specified, it defaults to
the project name.



CPACK_PACKAGE_VENDOR
The name of the package vendor. (e.g., ¡°Kitware¡±).  The default is ¡°Humanity¡±.



CPACK_PACKAGE_DIRECTORY
The directory in which CPack is doing its packaging.  If it is not set
then this will default (internally) to the build dir.  This variable may
be defined in a CPack config file or from the cpack
command line option -B.  If set, the command line option overrides the
value found in the config file.



CPACK_PACKAGE_VERSION_MAJOR
Package major version.  This variable will always be set, but its default
value depends on whether or not version details were given to the
project() command in the top level CMakeLists.txt file.  If version
details were given, the default value will be
CMAKE_PROJECT_VERSION_MAJOR.  If no version details were given,
a default version of 0.1.1 will be assumed, leading to
CPACK_PACKAGE_VERSION_MAJOR having a default value of 0.



CPACK_PACKAGE_VERSION_MINOR
Package minor version.  The default value is determined based on whether or
not version details were given to the project() command in the top
level CMakeLists.txt file.  If version details were given, the default
value will be CMAKE_PROJECT_VERSION_MINOR, but if no minor
version component was specified then CPACK_PACKAGE_VERSION_MINOR will be
left unset.  If no project version was given at all, a default version of
0.1.1 will be assumed, leading to CPACK_PACKAGE_VERSION_MINOR having a
default value of 1.



CPACK_PACKAGE_VERSION_PATCH
Package patch version.  The default value is determined based on whether or
not version details were given to the project() command in the top
level CMakeLists.txt file.  If version details were given, the default
value will be CMAKE_PROJECT_VERSION_PATCH, but if no patch
version component was specified then CPACK_PACKAGE_VERSION_PATCH will be
left unset.  If no project version was given at all, a default version of
0.1.1 will be assumed, leading to CPACK_PACKAGE_VERSION_PATCH having a
default value of 1.



CPACK_PACKAGE_DESCRIPTION
A description of the project, used in places such as the introduction
screen of CPack-generated Windows installers.  If not set, the value of
this variable is populated from the file named by
CPACK_PACKAGE_DESCRIPTION_FILE.



CPACK_PACKAGE_DESCRIPTION_FILE
A text file used to describe the project when
CPACK_PACKAGE_DESCRIPTION is not explicitly set.  The default
value for CPACK_PACKAGE_DESCRIPTION_FILE points to a built-in template
file Templates/CPack.GenericDescription.txt.



CPACK_PACKAGE_DESCRIPTION_SUMMARY
Short description of the project (only a few words).  If the
CMAKE_PROJECT_DESCRIPTION variable is set, it is used as the
default value, otherwise the default will be a string generated by CMake
based on CMAKE_PROJECT_NAME.



CPACK_PACKAGE_HOMEPAGE_URL
Project homepage URL.  The default value is taken from the
CMAKE_PROJECT_HOMEPAGE_URL variable, which is set by the top
level project() command, or else the default will be empty if no
URL was provided to project().



CPACK_PACKAGE_FILE_NAME
The name of the package file to generate, not including the
extension.  For example, cmake-2.6.1-Linux-i686.  The default value
is:
${CPACK_PACKAGE_NAME}-${CPACK_PACKAGE_VERSION}-${CPACK_SYSTEM_NAME}





CPACK_PACKAGE_INSTALL_DIRECTORY
Installation directory on the target system. This may be used by some
CPack generators like NSIS to create an installation directory e.g.,
¡°CMake 2.5¡± below the installation prefix.  All installed elements will be
put inside this directory.



CPACK_PACKAGE_ICON
A branding image that will be displayed inside the installer (used by GUI
installers).



CPACK_PACKAGE_CHECKSUM
An algorithm that will be used to generate an additional file with the
checksum of the package.  The output file name will be:
${CPACK_PACKAGE_FILE_NAME}.${CPACK_PACKAGE_CHECKSUM}


Supported algorithms are those listed by the
string(```<HASH>```) command.



CPACK_PROJECT_CONFIG_FILE
CPack-time project CPack configuration file.  This file is included at cpack
time, once per generator after CPack has set CPACK_GENERATOR
to the actual generator being used.  It allows per-generator setting of
CPACK_* variables at cpack time.



CPACK_RESOURCE_FILE_LICENSE
License to be embedded in the installer.  It will typically be displayed
to the user by the produced installer (often with an explicit ¡°Accept¡±
button, for graphical installers) prior to installation.  This license
file is NOT added to the installed files but is used by some CPack generators
like NSIS.  If you want to install a license file (may be the same as this
one) along with your project, you must add an appropriate CMake
install() command in your CMakeLists.txt.



CPACK_RESOURCE_FILE_README
ReadMe file to be embedded in the installer.  It typically describes in
some detail the purpose of the project during the installation.  Not all
CPack generators use this file.



CPACK_RESOURCE_FILE_WELCOME
Welcome file to be embedded in the installer.  It welcomes users to this
installer.  Typically used in the graphical installers on Windows and Mac
OS X.



CPACK_MONOLITHIC_INSTALL
Disables the component-based installation mechanism.  When set, the
component specification is ignored and all installed items are put in a
single ¡°MONOLITHIC¡± package.  Some CPack generators do monolithic
packaging by default and may be asked to do component packaging by
setting CPACK_```<GENNAME>```_COMPONENT_INSTALL to TRUE.



CPACK_GENERATOR
List of CPack generators to use.  If not specified, CPack will create a
set of options following the naming pattern
CPACK_BINARY_```<GENNAME>``` (e.g. CPACK_BINARY_NSIS) allowing
the user to enable/disable individual generators.  If the -G option is
given on the cpack command line, it will override this
variable and any CPACK_BINARY_```<GENNAME>``` options.



CPACK_OUTPUT_CONFIG_FILE
The name of the CPack binary configuration file.  This file is the CPack
configuration generated by the CPack module for binary installers.
Defaults to CPackConfig.cmake.



CPACK_PACKAGE_EXECUTABLES
Lists each of the executables and associated text label to be used to
create Start Menu shortcuts.  For example, setting this to the list
ccmake;CMake will create a shortcut named ¡°CMake¡± that will execute the
installed executable ccmake.  Not all CPack generators use it (at least
NSIS, WIX and OSXX11 do).



CPACK_STRIP_FILES
List of files to be stripped.  Starting with CMake 2.6.0,
CPACK_STRIP_FILES will be a boolean variable which enables
stripping of all files (a list of files evaluates to TRUE in CMake,
so this change is compatible).



CPACK_VERBATIM_VARIABLES
If set to TRUE, values of variables prefixed with CPACK_ will be
escaped before being written to the configuration files, so that the cpack
program receives them exactly as they were specified.  If not, characters
like quotes and backslashes can cause parsing errors or alter the value
received by the cpack program.  Defaults to FALSE for backwards
compatibility.

  


Variables for Source Package Generators
The following CPack variables are specific to source packages, and
will not affect binary packages:


CPACK_SOURCE_PACKAGE_FILE_NAME
The name of the source package.  For example cmake-2.6.1.



CPACK_SOURCE_STRIP_FILES
List of files in the source tree that will be stripped.  Starting with
CMake 2.6.0, CPACK_SOURCE_STRIP_FILES will be a boolean
variable which enables stripping of all files (a list of files evaluates
to TRUE in CMake, so this change is compatible).



CPACK_SOURCE_GENERATOR
List of generators used for the source packages.  As with
CPACK_GENERATOR, if this is not specified then CPack will
create a set of options (e.g. CPACK_SOURCE_ZIP) allowing
users to select which packages will be generated.



CPACK_SOURCE_OUTPUT_CONFIG_FILE
The name of the CPack source configuration file.  This file is the CPack
configuration generated by the CPack module for source installers.
Defaults to CPackSourceConfig.cmake.



CPACK_SOURCE_IGNORE_FILES
Pattern of files in the source tree that won¡¯t be packaged when building
a source package.  This is a list of regular expression patterns (that
must be properly escaped), e.g.,
/CVS/;/\\.svn/;\\.swp$;\\.#;/#;.*~;cscope.*

  


Variables for Advanced Use
The following variables are for advanced uses of CPack:


CPACK_CMAKE_GENERATOR
What CMake generator should be used if the project is a CMake
project.  Defaults to the value of CMAKE_GENERATOR.  Few users
will want to change this setting.



CPACK_INSTALL_CMAKE_PROJECTS
List of four values that specify what project to install.  The four values
are: Build directory, Project Name, Project Component, Directory.  If
omitted, CPack will build an installer that installs everything.



CPACK_SYSTEM_NAME
System name, defaults to the value of CMAKE_SYSTEM_NAME,
except on Windows where it will be win32 or win64.



CPACK_PACKAGE_VERSION
Package full version, used internally.  By default, this is built from
CPACK_PACKAGE_VERSION_MAJOR,
CPACK_PACKAGE_VERSION_MINOR, and
CPACK_PACKAGE_VERSION_PATCH.



CPACK_TOPLEVEL_TAG
Directory for the installed files.



CPACK_INSTALL_COMMANDS
Extra commands to install components.



CPACK_INSTALLED_DIRECTORIES
Extra directories to install.



CPACK_PACKAGE_INSTALL_REGISTRY_KEY
Registry key used when installing this project.  This is only used by
installers for Windows.  The default value is based on the installation
directory.



CPACK_CREATE_DESKTOP_LINKS
List of desktop links to create.  Each desktop link requires a
corresponding start menu shortcut as created by
CPACK_PACKAGE_EXECUTABLES.



CPACK_BINARY_```<GENNAME>```
CPack generated options for binary generators.  The CPack.cmake module
generates (when CPACK_GENERATOR is not set) a set of CMake
options (see CMake option() command) which may then be used to
select the CPack generator(s) to be used when building the package
target or when running cpack without the -G option.

  

