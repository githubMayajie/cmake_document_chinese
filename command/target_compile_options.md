  

# target_compile_options  
Add compile options to a target.  

target_compile_options(```<target>``` [BEFORE]
  ```<INTERFACE|PUBLIC|PRIVATE>``` [items1...]
  [```<INTERFACE|PUBLIC|PRIVATE>``` [items2...] ...])

  

Adds options to the COMPILE_OPTIONS or
INTERFACE_COMPILE_OPTIONS target properties. These options
are used when compiling the given ```<target>```, which must have been
created by a command such as add_executable() or
add_library() and must not be an ALIAS target.  


Arguments
If BEFORE is specified, the content will be prepended to the property
instead of being appended.
The INTERFACE, PUBLIC and PRIVATE keywords are required to
specify the scope of the following arguments.  PRIVATE and PUBLIC
items will populate the COMPILE_OPTIONS property of
```<target>```.  PUBLIC and INTERFACE items will populate the
INTERFACE_COMPILE_OPTIONS property of ```<target>```.
(IMPORTED targets only support INTERFACE items.)
The following arguments specify compile options.  Repeated calls for the same
```<target>``` append items in the order called.
Arguments to target_compile_options may use ˇ°generator expressionsˇ±
with the syntax $```<...>```. See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.
The final set of compile or link options used for a target is constructed by
accumulating options from the current target and the usage requirements of
it dependencies.  The set of options is de-duplicated to avoid repetition.
While beneficial for individual options, the de-duplication step can break
up option groups.  For example, -D A -D B becomes -D A B.  One may
specify a group of options using shell-like quoting along with a SHELL:
prefix.  The SHELL: prefix is dropped and the rest of the option string
is parsed using the separate_arguments() UNIX_COMMAND mode.
For example, "SHELL:-D A" "SHELL:-D B" becomes -D A -D B.
  


See Also
This command can be used to add any options. However, for adding
preprocessor definitions and include directories it is recommended
to use the more specific commands target_compile_definitions()
and target_include_directories().
For directory-wide settings, there is the command add_compile_options().
  

