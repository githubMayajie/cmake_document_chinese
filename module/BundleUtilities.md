  

# BundleUtilities  
Functions to help assemble a standalone bundle application.  

A collection of CMake utility functions useful for dealing with .app
bundles on the Mac and bundle-like directories on any OS.  

The following functions are provided by this module:  

fixup_bundle
copy_and_fixup_bundle
verify_app
get_bundle_main_executable
get_dotapp_dir
get_bundle_and_executable
get_bundle_all_executables
get_item_key
get_item_rpaths
clear_bundle_keys
set_bundle_key_values
get_bundle_keys
copy_resolved_item_into_bundle
copy_resolved_framework_into_bundle
fixup_bundle_item
verify_bundle_prerequisites
verify_bundle_symlinks

  

Requires CMake 2.6 or greater because it uses function, break and
PARENT_SCOPE.  Also depends on GetPrerequisites.cmake.  

DO NOT USE THESE FUNCTIONS AT CONFIGURE TIME (from CMakeLists.txt)!
Instead, invoke them from an install(CODE) or
install(SCRIPT) rule.  

fixup_bundle(```<app>``` ```<libs>``` ```<dirs>```)

  

Fix up ```<app>``` bundle in-place and make it standalone, such that it can be
drag-n-drop copied to another machine and run on that machine as long
as all of the system libraries are compatible.  

If you pass plugins to fixup_bundle as the libs parameter, you should
install them or copy them into the bundle before calling fixup_bundle.
The ```<libs>``` parameter is a list of libraries that must be fixed up, but
that cannot be determined by otool output analysis  (i.e. plugins).  

Gather all the keys for all the executables and libraries in a bundle,
and then, for each key, copy each prerequisite into the bundle.  Then
fix each one up according to its own list of prerequisites.  

Then clear all the keys and call verify_app on the final bundle to
ensure that it is truly standalone.  

As an optional parameter (IGNORE_ITEM) a list of file names can be passed,
which are then ignored
(e.g. IGNORE_ITEM "vcredist_x86.exe;vcredist_x64.exe").  

copy_and_fixup_bundle(```<src>``` ```<dst>``` ```<libs>``` ```<dirs>```)

  

Makes a copy of the bundle ```<src>``` at location ```<dst>``` and then fixes up
the new copied bundle in-place at ```<dst>```.  

verify_app(```<app>```)

  

Verifies that an application ```<app>``` appears valid based on running
analysis tools on it.  Calls message(FATAL_ERROR) if the application
is not verified.  

As an optional parameter (IGNORE_ITEM) a list of file names can be passed,
which are then ignored
(e.g. IGNORE_ITEM "vcredist_x86.exe;vcredist_x64.exe")  

get_bundle_main_executable(```<bundle>``` ```<result_var>```)

  

The result will be the full path name of the bundle¡¯s main executable
file or an error: prefixed string if it could not be determined.  

get_dotapp_dir(```<exe>``` ```<dotapp_dir_var>```)

  

Returns the nearest parent dir whose name ends with .app given the
full path to an executable.  If there is no such parent dir, then
simply return the dir containing the executable.  

The returned directory may or may not exist.  

get_bundle_and_executable(```<app>``` ```<bundle_var>``` ```<executable_var>``` ```<valid_var>```)

  

Takes either a .app directory name or the name of an executable
nested inside a .app directory and returns the path to the .app
directory in ```<bundle_var>``` and the path to its main executable in
```<executable_var>```.  

get_bundle_all_executables(```<bundle>``` ```<exes_var>```)

  

Scans ```<bundle>``` bundle recursively for all ```<exes_var>``` executable
files and accumulates them into a variable.  

get_item_key(```<item>``` ```<key_var>```)

  

Given ```<item>``` file name, generate ```<key_var>``` key that should be unique
considering the set of libraries that need copying or fixing up to
make a bundle standalone.  This is essentially the file name including
extension with . replaced by _  

This key is used as a prefix for CMake variables so that we can
associate a set of variables with a given item based on its key.  

clear_bundle_keys(```<keys_var>```)

  

Loop over the ```<keys_var>``` list of keys, clearing all the variables
associated with each key.  After the loop, clear the list of keys itself.  

Caller of get_bundle_keys should call clear_bundle_keys when done with
list of keys.  

set_bundle_key_values(```<keys_var>``` ```<context>``` ```<item>``` ```<exepath>``` ```<dirs>```
                      ```<copyflag>``` [```<rpaths>```])

  

Add ```<keys_var>``` key to the list (if necessary) for the given item.
If added, also set all the variables associated with that key.  

get_bundle_keys(```<app>``` ```<libs>``` ```<dirs>``` ```<keys_var>```)

  

Loop over all the executable and library files within ```<app>``` bundle (and
given as extra ```<libs>```) and accumulate a list of keys representing
them.  Set values associated with each key such that we can loop over
all of them and copy prerequisite libs into the bundle and then do
appropriate install_name_tool fixups.  

As an optional parameter (IGNORE_ITEM) a list of file names can be passed,
which are then ignored
(e.g. IGNORE_ITEM "vcredist_x86.exe;vcredist_x64.exe")  

copy_resolved_item_into_bundle(```<resolved_item>``` ```<resolved_embedded_item>```)

  

Copy a resolved item into the bundle if necessary.
Copy is not necessary, if the ```<resolved_item>``` is ¡°the same as¡± the
```<resolved_embedded_item>```.  

copy_resolved_framework_into_bundle(```<resolved_item>``` ```<resolved_embedded_item>```)

  

Copy a resolved framework into the bundle if necessary.
Copy is not necessary, if the ```<resolved_item>``` is ¡°the same as¡± the
```<resolved_embedded_item>```.  

By default, BU_COPY_FULL_FRAMEWORK_CONTENTS is not set.  If you want
full frameworks embedded in your bundles, set
BU_COPY_FULL_FRAMEWORK_CONTENTS to ON before calling fixup_bundle.  By
default, COPY_RESOLVED_FRAMEWORK_INTO_BUNDLE copies the framework
dylib itself plus the framework Resources directory.  

fixup_bundle_item(```<resolved_embedded_item>``` ```<exepath>``` ```<dirs>```)

  

Get the direct/non-system prerequisites of the ```<resolved_embedded_item>```.
For each prerequisite, change the way it is referenced to the value of
the _EMBEDDED_ITEM keyed variable for that prerequisite.  (Most likely
changing to an @executable_path style reference.)  

This function requires that the ```<resolved_embedded_item>``` be inside
the bundle already.  In other words, if you pass plugins to fixup_bundle
as the libs parameter, you should install them or copy them into the
bundle before calling fixup_bundle.  The libs parameter is a list of
libraries that must be fixed up, but that cannot be determined by
otool output analysis.  (i.e., plugins)  

Also, change the id of the item being fixed up to its own
_EMBEDDED_ITEM value.  

Accumulate changes in a local variable and make one call to
install_name_tool at the end of the function with all the changes at
once.  

If the BU_CHMOD_BUNDLE_ITEMS variable is set then bundle items will be
marked writable before install_name_tool tries to change them.  

verify_bundle_prerequisites(```<bundle>``` ```<result_var>``` ```<info_var>```)

  

Verifies that the sum of all prerequisites of all files inside the
bundle are contained within the bundle or are system libraries,
presumed to exist everywhere.  

As an optional parameter (IGNORE_ITEM) a list of file names can be passed,
which are then ignored
(e.g. IGNORE_ITEM "vcredist_x86.exe;vcredist_x64.exe")  

verify_bundle_symlinks(```<bundle>``` ```<result_var>``` ```<info_var>```)

  

Verifies that any symlinks found in the ```<bundle>``` bundle point to other files
that are already also in the bundle¡­  Anything that points to an
external file causes this function to fail the verification.  

