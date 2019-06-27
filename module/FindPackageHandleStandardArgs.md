  

# FindPackageHandleStandardArgs  
This module provides a function intended to be used in Find Modules
implementing find_package(```<PackageName>```) calls.  It handles the
REQUIRED, QUIET and version-related arguments of find_package.
It also sets the ```<PackageName>```_FOUND variable.  The package is
considered found if all variables listed contain valid results, e.g.
valid filepaths.  



find_package_handle_standard_args
There are two signatures:
find_package_handle_standard_args(```<PackageName>```
  (DEFAULT_MSG|```<custom-failure-message>```)
  ```<required-var>```...
  )

find_package_handle_standard_args(```<PackageName>```
  [FOUND_VAR ```<result-var>```]
  [REQUIRED_VARS ```<required-var>```...]
  [VERSION_VAR ```<version-var>```]
  [HANDLE_COMPONENTS]
  [CONFIG_MODE]
  [FAIL_MESSAGE ```<custom-failure-message>```]
  )


The ```<PackageName>```_FOUND variable will be set to TRUE if all
the variables ```<required-var>```... are valid and any optional
constraints are satisfied, and FALSE otherwise.  A success or
failure message may be displayed based on the results and on
whether the REQUIRED and/or QUIET option was given to
the find_package() call.
The options are:

(DEFAULT_MSG|```<custom-failure-message>```)
In the simple signature this specifies the failure message.
Use DEFAULT_MSG to ask for a default message to be computed
(recommended).  Not valid in the full signature.
FOUND_VAR ```<result-var>```
Obsolete.  Specifies either ```<PackageName>```_FOUND or
```<PACKAGENAME>```_FOUND as the result variable.  This exists only
for compatibility with older versions of CMake and is now ignored.
Result variables of both names are always set for compatibility.
REQUIRED_VARS ```<required-var>```...
Specify the variables which are required for this package.
These may be named in the generated failure message asking the
user to set the missing variable values.  Therefore these should
typically be cache entries such as FOO_LIBRARY and not output
variables like FOO_LIBRARIES.
VERSION_VAR ```<version-var>```
Specify the name of a variable that holds the version of the package
that has been found.  This version will be checked against the
(potentially) specified required version given to the
find_package() call, including its EXACT option.
The default messages include information about the required
version and the version which has been actually found, both
if the version is ok or not.
HANDLE_COMPONENTS
Enable handling of package components.  In this case, the command
will report which components have been found and which are missing,
and the ```<PackageName>```_FOUND variable will be set to FALSE
if any of the required components (i.e. not the ones listed after
the OPTIONAL_COMPONENTS option of find_package()) are
missing.
CONFIG_MODE
Specify that the calling find module is a wrapper around a
call to find_package(```<PackageName>``` NO_MODULE).  This implies
a VERSION_VAR value of ```<PackageName>```_VERSION.  The command
will automatically check whether the package configuration file
was found.
FAIL_MESSAGE ```<custom-failure-message>```
Specify a custom failure message instead of using the default
generated message.  Not recommended.

  

Example for the simple signature:  

find_package_handle_standard_args(LibXml2 DEFAULT_MSG
  LIBXML2_LIBRARY LIBXML2_INCLUDE_DIR)

  

The LibXml2 package is considered to be found if both
LIBXML2_LIBRARY and LIBXML2_INCLUDE_DIR are valid.
Then also LibXml2_FOUND is set to TRUE.  If it is not found
and REQUIRED was used, it fails with a
message(FATAL_ERROR), independent whether QUIET was
used or not.  If it is found, success will be reported, including
the content of the first ```<required-var>```.  On repeated CMake runs,
the same message will not be printed again.  

Example for the full signature:  

find_package_handle_standard_args(LibArchive
  REQUIRED_VARS LibArchive_LIBRARY LibArchive_INCLUDE_DIR
  VERSION_VAR LibArchive_VERSION)

  

In this case, the LibArchive package is considered to be found if
both LibArchive_LIBRARY and LibArchive_INCLUDE_DIR are valid.
Also the version of LibArchive will be checked by using the version
contained in LibArchive_VERSION.  Since no FAIL_MESSAGE is given,
the default messages will be printed.  

Another example for the full signature:  

find_package(Automoc4 QUIET NO_MODULE HINTS /opt/automoc4)
find_package_handle_standard_args(Automoc4  CONFIG_MODE)

  

In this case, a FindAutmoc4.cmake module wraps a call to
find_package(Automoc4 NO_MODULE) and adds an additional search
directory for automoc4.  Then the call to
find_package_handle_standard_args produces a proper success/failure
message.  

