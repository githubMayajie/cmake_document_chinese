  

# FetchContent  

Contents

FetchContent
Overview
Declaring Content Details
Populating The Content
Examples



  


Overview
This module enables populating content at configure time via any method
supported by the ExternalProject module.  Whereas
ExternalProject_Add() downloads at build time, the
FetchContent module makes content available immediately, allowing the
configure step to use the content in commands like add_subdirectory(),
include() or file() operations.
Content population details would normally be defined separately from the
command that performs the actual population.  This separation ensures that
all of the dependency details are defined before anything may try to use those
details to populate content.  This is particularly important in more complex
project hierarchies where dependencies may be shared between multiple projects.
The following shows a typical example of declaring content details:
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.8.0
)


For most typical cases, populating the content can then be done with a single
command like so:
FetchContent_MakeAvailable(googletest)


The above command not only populates the content, it also adds it to the main
build (if possible) so that the main build can use the populated project¡¯s
targets, etc.  In some cases, the main project may need to have more precise
control over the population or may be required to explicitly define the
population steps (e.g. if CMake versions earlier than 3.14 need to be
supported).  The typical pattern of such custom steps looks like this:
FetchContent_GetProperties(googletest)
if(NOT googletest_POPULATED)
  FetchContent_Populate(googletest)
  add_subdirectory(${googletest_SOURCE_DIR} ${googletest_BINARY_DIR})
endif()


Regardless of which population method is used, when using the
declare-populate pattern with a hierarchical project arrangement, projects at
higher levels in the hierarchy are able to override the population details of
content specified anywhere lower in the project hierarchy.  The ability to
detect whether content has already been populated ensures that even if
multiple child projects want certain content to be available, the first one
to populate it wins.  The other child project can simply make use of the
already available content instead of repeating the population for itself.
See the Examples section which demonstrates
this scenario.
The FetchContent module also supports defining and populating
content in a single call, with no check for whether the content has been
populated elsewhere in the project already.  This is a more low level
operation and would not normally be the way the module is used, but it is
sometimes useful as part of implementing some higher level feature or to
populate some content in CMake¡¯s script mode.
  


Declaring Content Details


FetchContent_Declare
FetchContent_Declare(```<name>``` ```<contentOptions>```...)


The FetchContent_Declare() function records the options that describe
how to populate the specified content, but if such details have already
been recorded earlier in this project (regardless of where in the project
hierarchy), this and all later calls for the same content ```<name>``` are
ignored.  This ¡°first to record, wins¡± approach is what allows hierarchical
projects to have parent projects override content details of child projects.
The content ```<name>``` can be any string without spaces, but good practice
would be to use only letters, numbers and underscores.  The name will be
treated case-insensitively and it should be obvious for the content it
represents, often being the name of the child project or the value given
to its top level project() command (if it is a CMake project).
For well-known public projects, the name should generally be the official
name of the project.  Choosing an unusual name makes it unlikely that other
projects needing that same content will use the same name, leading to
the content being populated multiple times.
The ```<contentOptions>``` can be any of the download or update/patch options
that the ExternalProject_Add() command understands.  The configure,
build, install and test steps are explicitly disabled and therefore options
related to them will be ignored.  In most cases, ```<contentOptions>``` will
just be a couple of options defining the download method and method-specific
details like a commit tag or archive hash.  For example:
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.8.0
)

FetchContent_Declare(
  myCompanyIcons
  URL      https://intranet.mycompany.com/assets/iconset_1.12.tar.gz
  URL_HASH 5588a7b18261c20068beabfb4f530b87
)

FetchContent_Declare(
  myCompanyCertificates
  SVN_REPOSITORY svn+ssh://svn.mycompany.com/srv/svn/trunk/certs
  SVN_REVISION   -r12345
)



  


Populating The Content
For most common scenarios, population means making content available to the
main build according to previously declared details for that dependency.
There are two main patterns for populating content, one based on calling
FetchContent_GetProperties() and
FetchContent_Populate() for more precise control and the other on
calling FetchContent_MakeAvailable() for a simpler, more automated
approach.  The former generally follows this canonical pattern:
# Check if population has already been performed
FetchContent_GetProperties(```<name>```)
string(TOLOWER "```<name>```" lcName)
if(NOT ${lcName}_POPULATED)
  # Fetch the content using previously declared details
  FetchContent_Populate(```<name>```)

  # Set custom variables, policies, etc.
  # ...

  # Bring the populated content into the build
  add_subdirectory(${${lcName}_SOURCE_DIR} ${${lcName}_BINARY_DIR})
endif()


The above is such a common pattern that, where no custom steps are needed
between the calls to FetchContent_Populate() and
add_subdirectory(), equivalent logic can be obtained by calling
FetchContent_MakeAvailable() instead (and should be preferred where
it meets the needs of the project).


FetchContent_Populate
FetchContent_Populate( ```<name>``` )


In most cases, the only argument given to FetchContent_Populate() is the
```<name>```.  When used this way, the command assumes the content details have
been recorded by an earlier call to FetchContent_Declare().  The
details are stored in a global property, so they are unaffected by things
like variable or directory scope.  Therefore, it doesn¡¯t matter where in the
project the details were previously declared, as long as they have been
declared before the call to FetchContent_Populate().  Those saved details
are then used to construct a call to ExternalProject_Add() in a
private sub-build to perform the content population immediately.  The
implementation of ExternalProject_Add() ensures that if the content has
already been populated in a previous CMake run, that content will be reused
rather than repopulating them again.  For the common case where population
involves downloading content, the cost of the download is only paid once.
An internal global property records when a particular content population
request has been processed.  If FetchContent_Populate() is called more
than once for the same content name within a configure run, the second call
will halt with an error.  Projects can and should check whether content
population has already been processed with the
FetchContent_GetProperties() command before calling
FetchContent_Populate().
FetchContent_Populate() will set three variables in the scope of the
caller; ```<lcName>```_POPULATED, ```<lcName>```_SOURCE_DIR and
```<lcName>```_BINARY_DIR, where ```<lcName>``` is the lowercased ```<name>```.
```<lcName>```_POPULATED will always be set to True by the call.
```<lcName>```_SOURCE_DIR is the location where the
content can be found upon return (it will have already been populated), while
```<lcName>```_BINARY_DIR is a directory intended for use as a corresponding
build directory.  The main use case for the two directory variables is to
call add_subdirectory() immediately after population, i.e.:
FetchContent_Populate(FooBar ...)
add_subdirectory(${foobar_SOURCE_DIR} ${foobar_BINARY_DIR})


The values of the three variables can also be retrieved from anywhere in the
project hierarchy using the FetchContent_GetProperties() command.
A number of cache variables influence the behavior of all content population
performed using details saved from a FetchContent_Declare() call:

FETCHCONTENT_BASE_DIR
In most cases, the saved details do not specify any options relating to the
directories to use for the internal sub-build, final source and build areas.
It is generally best to leave these decisions up to the FetchContent
module to handle on the project¡¯s behalf.  The FETCHCONTENT_BASE_DIR
cache variable controls the point under which all content population
directories are collected, but in most cases developers would not need to
change this.  The default location is ${CMAKE_BINARY_DIR}/_deps, but if
developers change this value, they should aim to keep the path short and
just below the top level of the build tree to avoid running into path
length problems on Windows.
FETCHCONTENT_QUIET
The logging output during population can be quite verbose, making the
configure stage quite noisy.  This cache option (ON by default) hides
all population output unless an error is encountered.  If experiencing
problems with hung downloads, temporarily switching this option off may
help diagnose which content population is causing the issue.
FETCHCONTENT_FULLY_DISCONNECTED
When this option is enabled, no attempt is made to download or update
any content.  It is assumed that all content has already been populated in
a previous run or the source directories have been pointed at existing
contents the developer has provided manually (using options described
further below).  When the developer knows that no changes have been made to
any content details, turning this option ON can significantly speed up
the configure stage.  It is OFF by default.
FETCHCONTENT_UPDATES_DISCONNECTED
This is a less severe download/update control compared to
FETCHCONTENT_FULLY_DISCONNECTED.  Instead of bypassing all download and
update logic, the FETCHCONTENT_UPDATES_DISCONNECTED only disables the
update stage.  Therefore, if content has not been downloaded previously,
it will still be downloaded when this option is enabled.  This can speed up
the configure stage, but not as much as
FETCHCONTENT_FULLY_DISCONNECTED.  It is OFF by default.

In addition to the above cache variables, the following cache variables are
also defined for each content name (```<ucName>``` is the uppercased value of
```<name>```):

FETCHCONTENT_SOURCE_DIR_```<ucName>```
If this is set, no download or update steps are performed for the specified
content and the ```<lcName>```_SOURCE_DIR variable returned to the caller is
pointed at this location.  This gives developers a way to have a separate
checkout of the content that they can modify freely without interference
from the build.  The build simply uses that existing source, but it still
defines ```<lcName>```_BINARY_DIR to point inside its own build area.
Developers are strongly encouraged to use this mechanism rather than
editing the sources populated in the default location, as changes to
sources in the default location can be lost when content population details
are changed by the project.
FETCHCONTENT_UPDATES_DISCONNECTED_```<ucName>```
This is the per-content equivalent of
FETCHCONTENT_UPDATES_DISCONNECTED. If the global option or this option
is ON, then updates will be disabled for the named content.
Disabling updates for individual content can be useful for content whose
details rarely change, while still leaving other frequently changing
content with updates enabled.

The FetchContent_Populate() command also supports a syntax allowing the
content details to be specified directly rather than using any saved
details.  This is more low-level and use of this form is generally to be
avoided in favour of using saved content details as outlined above.
Nevertheless, in certain situations it can be useful to invoke the content
population as an isolated operation (typically as part of implementing some
other higher level feature or when using CMake in script mode):
FetchContent_Populate( ```<name>```
  [QUIET]
  [SUBBUILD_DIR ```<subBuildDir>```]
  [SOURCE_DIR ```<srcDir>```]
  [BINARY_DIR ```<binDir>```]
  ...
)


This form has a number of key differences to that where only ```<name>``` is
provided:

All required population details are assumed to have been provided directly
in the call to FetchContent_Populate(). Any saved details for
```<name>``` are ignored.
No check is made for whether content for ```<name>``` has already been
populated.
No global property is set to record that the population has occurred.
No global properties record the source or binary directories used for the
populated content.
The FETCHCONTENT_FULLY_DISCONNECTED and
FETCHCONTENT_UPDATES_DISCONNECTED cache variables are ignored.

The ```<lcName>```_SOURCE_DIR and ```<lcName>```_BINARY_DIR variables are still
returned to the caller, but since these locations are not stored as global
properties when this form is used, they are only available to the calling
scope and below rather than the entire project hierarchy.  No
```<lcName>```_POPULATED variable is set in the caller¡¯s scope with this form.
The supported options for FetchContent_Populate() are the same as those
for FetchContent_Declare().  Those few options shown just
above are either specific to FetchContent_Populate() or their behavior is
slightly modified from how ExternalProject_Add() treats them.

QUIET
The QUIET option can be given to hide the output associated with
populating the specified content.  If the population fails, the output will
be shown regardless of whether this option was given or not so that the
cause of the failure can be diagnosed.  The global FETCHCONTENT_QUIET
cache variable has no effect on FetchContent_Populate() calls where the
content details are provided directly.
SUBBUILD_DIR
The SUBBUILD_DIR argument can be provided to change the location of the
sub-build created to perform the population.  The default value is
${CMAKE_CURRENT_BINARY_DIR}/```<lcName>```-subbuild and it would be unusual
to need to override this default.  If a relative path is specified, it will
be interpreted as relative to CMAKE_CURRENT_BINARY_DIR.
SOURCE_DIR, BINARY_DIR
The SOURCE_DIR and BINARY_DIR arguments are supported by
ExternalProject_Add(), but different default values are used by
FetchContent_Populate().  SOURCE_DIR defaults to
${CMAKE_CURRENT_BINARY_DIR}/```<lcName>```-src and BINARY_DIR defaults to
${CMAKE_CURRENT_BINARY_DIR}/```<lcName>```-build.  If a relative path is
specified, it will be interpreted as relative to
CMAKE_CURRENT_BINARY_DIR.

In addition to the above explicit options, any other unrecognized options are
passed through unmodified to ExternalProject_Add() to perform the
download, patch and update steps.  The following options are explicitly
prohibited (they are disabled by the FetchContent_Populate() command):

CONFIGURE_COMMAND
BUILD_COMMAND
INSTALL_COMMAND
TEST_COMMAND

If using FetchContent_Populate() within CMake¡¯s script mode, be aware
that the implementation sets up a sub-build which therefore requires a CMake
generator and build tool to be available. If these cannot be found by
default, then the CMAKE_GENERATOR and/or
CMAKE_MAKE_PROGRAM variables will need to be set appropriately
on the command line invoking the script.



FetchContent_GetProperties
When using saved content details, a call to FetchContent_Populate()
records information in global properties which can be queried at any time.
This information includes the source and binary directories associated with
the content and also whether or not the content population has been processed
during the current configure run.
FetchContent_GetProperties( ```<name>```
  [SOURCE_DIR ```<srcDirVar>```]
  [BINARY_DIR ```<binDirVar>```]
  [POPULATED ```<doneVar>```]
)


The SOURCE_DIR, BINARY_DIR and POPULATED options can be used to
specify which properties should be retrieved.  Each option accepts a value
which is the name of the variable in which to store that property.  Most of
the time though, only ```<name>``` is given, in which case the call will then
set the same variables as a call to
FetchContent_Populate(name).  This allows
the following canonical pattern to be used, which ensures that the relevant
variables will always be defined regardless of whether or not the population
has been performed elsewhere in the project already:
FetchContent_GetProperties(foobar)
if(NOT foobar_POPULATED)
  FetchContent_Populate(foobar)
  ...
endif()


The above pattern allows other parts of the overall project hierarchy to
re-use the same content and ensure that it is only populated once.



FetchContent_MakeAvailable
FetchContent_MakeAvailable( ```<name1>``` [```<name2>```...] )


This command implements the common pattern typically needed for most
dependencies.  It iterates over each of the named dependencies in turn
and for each one it loosely follows the same
canonical pattern as
presented at the beginning of this section.  One small difference to
that pattern is that it will only call add_subdirectory() on the
populated content if there is a CMakeLists.txt file in its top level
source directory.  This allows the command to be used for dependencies
that make downloaded content available at a known location but which do
not need or support being added directly to the build.

  


Examples
This first fairly straightforward example ensures that some popular testing
frameworks are available to the main build:
include(FetchContent)
FetchContent_Declare(
  googletest
  GIT_REPOSITORY https://github.com/google/googletest.git
  GIT_TAG        release-1.8.0
)
FetchContent_Declare(
  Catch2
  GIT_REPOSITORY https://github.com/catchorg/Catch2.git
  GIT_TAG        v2.5.0
)

# After the following call, the CMake targets defined by googletest and
# Catch2 will be defined and available to the rest of the build
FetchContent_MakeAvailable(googletest Catch2)


In more complex project hierarchies, the dependency relationships can be more
complicated.  Consider a hierarchy where projA is the top level project and
it depends directly on projects projB and projC.  Both projB and
projC can be built standalone and they also both depend on another project
projD.  projB additionally depends on projE.  This example assumes
that all five projects are available on a company git server.  The
CMakeLists.txt of each project might have sections like the following:
projA:
include(FetchContent)
FetchContent_Declare(
  projB
  GIT_REPOSITORY git@mycompany.com:git/projB.git
  GIT_TAG        4a89dc7e24ff212a7b5167bef7ab079d
)
FetchContent_Declare(
  projC
  GIT_REPOSITORY git@mycompany.com:git/projC.git
  GIT_TAG        4ad4016bd1d8d5412d135cf8ceea1bb9
)
FetchContent_Declare(
  projD
  GIT_REPOSITORY git@mycompany.com:git/projD.git
  GIT_TAG        origin/integrationBranch
)
FetchContent_Declare(
  projE
  GIT_REPOSITORY git@mycompany.com:git/projE.git
  GIT_TAG        origin/release/2.3-rc1
)

# Order is important, see notes in the discussion further below
FetchContent_MakeAvailable(projD projB projC)


projB:
include(FetchContent)
FetchContent_Declare(
  projD
  GIT_REPOSITORY git@mycompany.com:git/projD.git
  GIT_TAG        20b415f9034bbd2a2e8216e9a5c9e632
)
FetchContent_Declare(
  projE
  GIT_REPOSITORY git@mycompany.com:git/projE.git
  GIT_TAG        68e20f674a48be38d60e129f600faf7d
)

FetchContent_MakeAvailable(projD projE)


projC:
include(FetchContent)
FetchContent_Declare(
  projD
  GIT_REPOSITORY git@mycompany.com:git/projD.git
  GIT_TAG        7d9a17ad2c962aa13e2fbb8043fb6b8a
)

# This particular version of projD requires workarounds
FetchContent_GetProperties(projD)
if(NOT projd_POPULATED)
  FetchContent_Populate(projD)

  # Copy an additional/replacement file into the populated source
  file(COPY someFile.c DESTINATION ${projd_SOURCE_DIR}/src)

  add_subdirectory(${projd_SOURCE_DIR} ${projd_BINARY_DIR})
endif()


A few key points should be noted in the above:

projB and projC define different content details for projD,
but projA also defines a set of content details for projD.
Because projA will define them first, the details from projB and
projC will not be used.  The override details defined by projA
are not required to match either of those from projB or projC, but
it is up to the higher level project to ensure that the details it does
define still make sense for the child projects.
In the projA call to FetchContent_MakeAvailable(), projD
is listed ahead of projB and projC to ensure that projA is in
control of how projD is populated.
While projA defines content details for projE, it does not need
to explicitly call FetchContent_MakeAvailable(projE) or
FetchContent_Populate(projD) itself.  Instead, it leaves that to the
child projB.  For higher level projects, it is often enough to just
define the override content details and leave the actual population to the
child projects.  This saves repeating the same thing at each level of the
project hierarchy unnecessarily.

Projects don¡¯t always need to add the populated content to the build.
Sometimes the project just wants to make the downloaded content available at
a predictable location.  The next example ensures that a set of standard
company toolchain files (and potentially even the toolchain binaries
themselves) is available early enough to be used for that same build.
cmake_minimum_required(VERSION 3.14)

include(FetchContent)
FetchContent_Declare(
  mycom_toolchains
  URL  https://intranet.mycompany.com//toolchains_1.3.2.tar.gz
)
FetchContent_MakeAvailable(mycom_toolchains)

project(CrossCompileExample)


The project could be configured to use one of the downloaded toolchains like
so:
cmake -DCMAKE_TOOLCHAIN_FILE=_deps/mycom_toolchains-src/toolchain_arm.cmake /path/to/src


When CMake processes the CMakeLists.txt file, it will download and unpack
the tarball into _deps/mycompany_toolchains-src relative to the build
directory.  The CMAKE_TOOLCHAIN_FILE variable is not used until
the project() command is reached, at which point CMake looks for the
named toolchain file relative to the build directory.  Because the tarball has
already been downloaded and unpacked by then, the toolchain file will be in
place, even the very first time that cmake is run in the build directory.
Lastly, the following example demonstrates how one might download and unpack a
firmware tarball using CMake¡¯s script mode.  The call to
FetchContent_Populate() specifies all the content details and the
unpacked firmware will be placed in a firmware directory below the
current working directory.
getFirmware.cmake:
# NOTE: Intended to be run in script mode with cmake -P
include(FetchContent)
FetchContent_Populate(
  firmware
  URL        https://mycompany.com/assets/firmware-1.23-arm.tar.gz
  URL_HASH   MD5=68247684da89b608d466253762b0ff11
  SOURCE_DIR firmware
)


  

