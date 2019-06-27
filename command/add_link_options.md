  

# add_link_options  
Add options to the link step for executable, shared library or module
library targets in the current directory and below that are added after
this command is invoked.  

add_link_options(```<option>``` ...)

  

This command can be used to add any link options, but alternative commands
exist to add libraries (target_link_libraries() or
link_libraries()).  See documentation of the
directory and
target LINK_OPTIONS properties.  


Note
This command cannot be used to add options for static library targets,
since they do not use a linker.  To add archiver or MSVC librarian flags,
see the STATIC_LIBRARY_OPTIONS target property.
  

Arguments to add_link_options may use ¡°generator expressions¡± with
the syntax $```<...>```.  See the cmake-generator-expressions(7)
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

To pass options to the linker tool, each compiler driver has is own syntax.
The LINKER: prefix can be used to specify, in a portable way, options
to pass to the linker tool. The LINKER: prefix is replaced by the required
driver option and the rest of the option string defines linker arguments using
, as separator. These arguments will be formatted according to the
CMAKE_```<LANG>```_LINKER_WRAPPER_FLAG and
CMAKE_```<LANG>```_LINKER_WRAPPER_FLAG_SEP variables.  

For example, "LINKER:-z,defs" becomes -Xlinker -z -Xlinker defs for
Clang and -Wl,-z,defs for GNU GCC.  

The LINKER: prefix can be specified as part of a SHELL: prefix
expression.  

The LINKER: prefix supports, as alternate syntax, specification of
arguments using SHELL: prefix and space as separator. Previous example
becomes "LINKER:SHELL:-z defs".  


Note
Specifying SHELL: prefix elsewhere than at the beginning of the
LINKER: prefix is not supported.
  

