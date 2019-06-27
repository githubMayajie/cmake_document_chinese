  

# GetPrerequisites  
Functions to analyze and list executable file prerequisites.  

This module provides functions to list the .dll, .dylib or .so files
that an executable or shared library file depends on.  (Its
prerequisites.)  

It uses various tools to obtain the list of required shared library
files:  

dumpbin (Windows)
objdump (MinGW on Windows)
ldd (Linux/Unix)
otool (Mac OSX)

  

The following functions are provided by this module:  

get_prerequisites
list_prerequisites
list_prerequisites_by_glob
gp_append_unique
is_file_executable
gp_item_default_embedded_path
  (projects can override with gp_item_default_embedded_path_override)
gp_resolve_item
  (projects can override with gp_resolve_item_override)
gp_resolved_file_type
  (projects can override with gp_resolved_file_type_override)
gp_file_type

  

Requires CMake 2.6 or greater because it uses function, break, return
and PARENT_SCOPE.  

GET_PREREQUISITES(```<target>``` ```<prerequisites_var>``` ```<exclude_system>``` ```<recurse>```
                  ```<exepath>``` ```<dirs>``` [```<rpaths>```])

  

Get the list of shared library files required by ```<target>```.  The list
in the variable named ```<prerequisites_var>``` should be empty on first
entry to this function.  On exit, ```<prerequisites_var>``` will contain the
list of required shared library files.  

```<target>``` is the full path to an executable file.  ```<prerequisites_var>```
is the name of a CMake variable to contain the results.
```<exclude_system>``` must be 0 or 1 indicating whether to include or
exclude ¡°system¡± prerequisites.  If ```<recurse>``` is set to 1 all
prerequisites will be found recursively, if set to 0 only direct
prerequisites are listed.  ```<exepath>``` is the path to the top level
executable used for @executable_path replacment on the Mac.  ```<dirs>``` is
a list of paths where libraries might be found: these paths are
searched first when a target without any path info is given.  Then
standard system locations are also searched: PATH, Framework
locations, /usr/lib¡­  

The variable GET_PREREQUISITES_VERBOSE can be set to true to enable verbose
output.  

LIST_PREREQUISITES(```<target>``` [```<recurse>``` [```<exclude_system>``` [```<verbose>```]]])

  

Print a message listing the prerequisites of ```<target>```.  

```<target>``` is the name of a shared library or executable target or the
full path to a shared library or executable file.  If ```<recurse>``` is set
to 1 all prerequisites will be found recursively, if set to 0 only
direct prerequisites are listed.  ```<exclude_system>``` must be 0 or 1
indicating whether to include or exclude ¡°system¡± prerequisites.  With
```<verbose>``` set to 0 only the full path names of the prerequisites are
printed, set to 1 extra informatin will be displayed.  

LIST_PREREQUISITES_BY_GLOB(```<glob_arg>``` ```<glob_exp>```)

  

Print the prerequisites of shared library and executable files
matching a globbing pattern.  ```<glob_arg>``` is GLOB or GLOB_RECURSE and
```<glob_exp>``` is a globbing expression used with ¡°file(GLOB¡± or
¡°file(GLOB_RECURSE¡± to retrieve a list of matching files.  If a
matching file is executable, its prerequisites are listed.  

Any additional (optional) arguments provided are passed along as the
optional arguments to the list_prerequisites calls.  

GP_APPEND_UNIQUE(```<list_var>``` ```<value>```)

  

Append ```<value>``` to the list variable ```<list_var>``` only if the value is
not already in the list.  

IS_FILE_EXECUTABLE(```<file>``` ```<result_var>```)

  

Return 1 in ```<result_var>``` if ```<file>``` is a binary executable, 0
otherwise.  

GP_ITEM_DEFAULT_EMBEDDED_PATH(```<item>``` ```<default_embedded_path_var>```)

  

Return the path that others should refer to the item by when the item
is embedded inside a bundle.  

Override on a per-project basis by providing a project-specific
gp_item_default_embedded_path_override function.  

GP_RESOLVE_ITEM(```<context>``` ```<item>``` ```<exepath>``` ```<dirs>``` ```<resolved_item_var>```
                [```<rpaths>```])

  

Resolve an item into an existing full path file.  

Override on a per-project basis by providing a project-specific
gp_resolve_item_override function.  

GP_RESOLVED_FILE_TYPE(```<original_file>``` ```<file>``` ```<exepath>``` ```<dirs>``` ```<type_var>```
                      [```<rpaths>```])

  

Return the type of ```<file>``` with respect to ```<original_file>```.  String
describing type of prerequisite is returned in variable named
```<type_var>```.  

Use ```<exepath>``` and ```<dirs>``` if necessary to resolve non-absolute ```<file>```
values ¨C but only for non-embedded items.  

Possible types are:  

system
local
embedded
other

  

Override on a per-project basis by providing a project-specific
gp_resolved_file_type_override function.  

GP_FILE_TYPE(```<original_file>``` ```<file>``` ```<type_var>```)

  

Return the type of ```<file>``` with respect to ```<original_file>```.  String
describing type of prerequisite is returned in variable named
```<type_var>```.  

Possible types are:  

system
local
embedded
other

  

