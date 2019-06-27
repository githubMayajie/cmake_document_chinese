  

# FeatureSummary  
Functions for generating a summary of enabled/disabled features.  

These functions can be used to generate a summary of enabled and disabled
packages and/or feature for a build tree such as:  

-- The following OPTIONAL packages have been found:
LibXml2 (required version >```= 2.4), XML processing lib, ```<http://xmlsoft.org>```
   * Enables HTML-import in MyWordProcessor
   * Enables odt-export in MyWordProcessor
PNG, A PNG image library., ```<http://www.libpng.org/pub/png/>```
   * Enables saving screenshots
-- The following OPTIONAL packages have not been found:
Lua51, The Lua scripting language., ```<http://www.lua.org>```
   * Enables macros in MyWordProcessor
Foo, Foo provides cool stuff.

  


Global Properties


FeatureSummary_PKG_TYPES

The global property FeatureSummary_PKG_TYPES defines the type of
packages used by FeatureSummary.
The order in this list is important, the first package type in the list is the
least important, the last is the most important. the of a package can only be
changed to higher types.
The default package types are , RUNTIME, OPTIONAL, RECOMMENDED and
REQUIRED, and their importance is
RUNTIME ```< OPTIONAL ```< RECOMMENDED ```< REQUIRED.


FeatureSummary_REQUIRED_PKG_TYPES

The global property FeatureSummary_REQUIRED_PKG_TYPES defines which
package types are required.
If one or more package in this categories has not been found, CMake will abort
when calling feature_summary() with the
¡®FATAL_ON_MISSING_REQUIRED_PACKAGES¡¯ option enabled.
The default value for this global property is REQUIRED.


FeatureSummary_DEFAULT_PKG_TYPE

The global property FeatureSummary_DEFAULT_PKG_TYPE defines which
package type is the default one.
When calling feature_summary(), if the user did not set the package type
explicitly, the package will be assigned to this category.
This value must be one of the types defined in the
FeatureSummary_PKG_TYPES global property unless the package type
is set for all the packages.
The default value for this global property is OPTIONAL.


FeatureSummary_```<TYPE>```_DESCRIPTION

The global property FeatureSummary_```<TYPE>```_DESCRIPTION can be defined
for each type to replace the type name with the specified string whenever the
package type is used in an output string.
If not set, the string ¡°```<TYPE>``` packages¡± is used.
  


Functions


feature_summary
feature_summary( [FILENAME ```<file>```]
                 [APPEND]
                 [VAR ```<variable_name>```]
                 [INCLUDE_QUIET_PACKAGES]
                 [FATAL_ON_MISSING_REQUIRED_PACKAGES]
                 [DESCRIPTION "```<description>```" | DEFAULT_DESCRIPTION]
                 [QUIET_ON_EMPTY]
                 WHAT (ALL
                      | PACKAGES_FOUND | PACKAGES_NOT_FOUND
                      | ```<TYPE>```_PACKAGES_FOUND | ```<TYPE>```_PACKAGES_NOT_FOUND
                      | ENABLED_FEATURES | DISABLED_FEATURES)
               )


The feature_summary() macro can be used to print information about
enabled or disabled packages or features of a project.  By default,
only the names of the features/packages will be printed and their
required version when one was specified.  Use set_package_properties()
to add more useful information, like e.g.  a download URL for the
respective package or their purpose in the project.
The WHAT option is the only mandatory option.  Here you specify what
information will be printed:

ALL
print everything
ENABLED_FEATURES
the list of all features which are enabled
DISABLED_FEATURES
the list of all features which are disabled
PACKAGES_FOUND
the list of all packages which have been found
PACKAGES_NOT_FOUND
the list of all packages which have not been found

For each package type ```<TYPE>``` defined by the
FeatureSummary_PKG_TYPES global property, the following
information can also be used:

```<TYPE>```_PACKAGES_FOUND
only those packages which have been found which have the type ```<TYPE>```
```<TYPE>```_PACKAGES_NOT_FOUND
only those packages which have not been found which have the type ```<TYPE>```

With the exception of the ALL value, these values can be combined
in order to customize the output. For example:
feature_summary(WHAT ENABLED_FEATURES DISABLED_FEATURES)


If a FILENAME is given, the information is printed into this file.  If
APPEND is used, it is appended to this file, otherwise the file is
overwritten if it already existed.  If the VAR option is used, the
information is ¡°printed¡± into the specified variable.  If FILENAME is
not used, the information is printed to the terminal.  Using the
DESCRIPTION option a description or headline can be set which will be
printed above the actual content.  If only one type of
package was requested, no title is printed, unless it is explicitly set using
either DESCRIPTION to use a custom string, or DEFAULT_DESCRIPTION to
use a default title for the requested type.
If INCLUDE_QUIET_PACKAGES is given, packages which have been searched with
find_package(... QUIET) will also be listed. By default they are skipped.
If FATAL_ON_MISSING_REQUIRED_PACKAGES is given, CMake will abort if a
package which is marked as one of the package types listed in the
FeatureSummary_REQUIRED_PKG_TYPES global property has not been
found.
The default value for the FeatureSummary_REQUIRED_PKG_TYPES global
property is REQUIRED.
The FeatureSummary_DEFAULT_PKG_TYPE global property can be
modified to change the default package type assigned when not explicitly
assigned by the user.
If the QUIET_ON_EMPTY option is used, if only one type of package was
requested, and no packages belonging to that category were found, then no
output (including the DESCRIPTION) is printed or added to the VAR
variable.
Example 1, append everything to a file:
include(FeatureSummary)
feature_summary(WHAT ALL
                FILENAME ${CMAKE_BINARY_DIR}/all.log APPEND)


Example 2, print the enabled features into the variable
enabledFeaturesText, including QUIET packages:
include(FeatureSummary)
feature_summary(WHAT ENABLED_FEATURES
                INCLUDE_QUIET_PACKAGES
                DESCRIPTION "Enabled Features:"
                VAR enabledFeaturesText)
message(STATUS "${enabledFeaturesText}")


Example 3, change default package types and print only the categories that
are not empty:
include(FeatureSummary)
set_property(GLOBAL APPEND PROPERTY FeatureSummary_PKG_TYPES BUILD)
find_package(FOO)
set_package_properties(FOO PROPERTIES TYPE BUILD)
feature_summary(WHAT BUILD_PACKAGES_FOUND
                Description "Build tools found:"
                QUIET_ON_EMPTY)
feature_summary(WHAT BUILD_PACKAGES_NOT_FOUND
                Description "Build tools not found:"
                QUIET_ON_EMPTY)





set_package_properties
set_package_properties(```<name>``` PROPERTIES
                       [ URL ```<url>``` ]
                       [ DESCRIPTION ```<description>``` ]
                       [ TYPE (RUNTIME|OPTIONAL|RECOMMENDED|REQUIRED) ]
                       [ PURPOSE ```<purpose>``` ]
                      )


Use this macro to set up information about the named package, which
can then be displayed via FEATURE_SUMMARY().  This can be done either
directly in the Find-module or in the project which uses the module
after the find_package() call.  The features for which information can
be set are added automatically by the find_package() command.

URL ```<url>```
This should be the homepage of the package, or something similar.
Ideally this is set already directly in the Find-module.
DESCRIPTION ```<description>```
A short description what that package is, at most one sentence.
Ideally this is set already directly in the Find-module.
TYPE ```<type>```
What type of dependency has the using project on that package.
Default is OPTIONAL.  In this case it is a package which can be used
by the project when available at buildtime, but it also work without.
RECOMMENDED is similar to OPTIONAL, i.e.  the project will build if
the package is not present, but the functionality of the resulting
binaries will be severely limited.  If a REQUIRED package is not
available at buildtime, the project may not even build.  This can be
combined with the FATAL_ON_MISSING_REQUIRED_PACKAGES argument for
feature_summary().  Last, a RUNTIME package is a package which is
actually not used at all during the build, but which is required for
actually running the resulting binaries.  So if such a package is
missing, the project can still be built, but it may not work later on.
If set_package_properties() is called multiple times for the same
package with different TYPEs, the TYPE is only changed to higher
TYPEs (RUNTIME ```< OPTIONAL ```< RECOMMENDED ```< REQUIRED), lower TYPEs are
ignored.  The TYPE property is project-specific, so it cannot be set
by the Find-module, but must be set in the project.
Type accepted can be changed by setting the
FeatureSummary_PKG_TYPES global property.
PURPOSE ```<purpose>```
This describes which features this package enables in the
project, i.e.  it tells the user what functionality he gets in the
resulting binaries.  If set_package_properties() is called multiple
times for a package, all PURPOSE properties are appended to a list of
purposes of the package in the project.  As the TYPE property, also
the PURPOSE property is project-specific, so it cannot be set by the
Find-module, but must be set in the project.

Example for setting the info for a package:
find_package(LibXml2)
set_package_properties(LibXml2 PROPERTIES
                       DESCRIPTION "A XML processing library."
                       URL "http://xmlsoft.org/")
# or
set_package_properties(LibXml2 PROPERTIES
                       TYPE RECOMMENDED
                       PURPOSE "Enables HTML-import in MyWordProcessor")
# or
set_package_properties(LibXml2 PROPERTIES
                       TYPE OPTIONAL
                       PURPOSE "Enables odt-export in MyWordProcessor")

find_package(DBUS)
set_package_properties(DBUS PROPERTIES
  TYPE RUNTIME
  PURPOSE "Necessary to disable the screensaver during a presentation")





add_feature_info
add_feature_info(```<name>``` ```<enabled>``` ```<description>```)


Use this macro to add information about a feature with the given ```<name>```.
```<enabled>``` contains whether this feature is enabled or not. It can be a
variable or a list of conditions.
```<description>``` is a text describing the feature.  The information can
be displayed using feature_summary() for ENABLED_FEATURES and
DISABLED_FEATURES respectively.
Example for setting the info for a feature:
option(WITH_FOO "Help for foo" ON)
add_feature_info(Foo WITH_FOO "The Foo feature provides very cool stuff.")



  


Legacy Macros
The following macros are provided for compatibility with previous
CMake versions:


set_package_info
set_package_info(```<name>``` ```<description>``` [ ```<url>``` [```<purpose>```] ])


Use this macro to set up information about the named package, which
can then be displayed via feature_summary().  This can be done either
directly in the Find-module or in the project which uses the module
after the find_package() call.  The features for which information
can be set are added automatically by the find_package() command.



set_feature_info
set_feature_info(```<name>``` ```<description>``` [```<url>```])


Does the same as:
set_package_info(```<name>``` ```<description>``` ```<url>```)





print_enabled_features
print_enabled_features()


Does the same as
feature_summary(WHAT ENABLED_FEATURES DESCRIPTION "Enabled features:")





print_disabled_features
print_disabled_features()


Does the same as
feature_summary(WHAT DISABLED_FEATURES DESCRIPTION "Disabled features:")



  

