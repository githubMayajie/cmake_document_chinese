  

# add_compile_options  
Add options to the compilation of source files.  

add_compile_options(```<option>``` ...)

  

Adds options to the COMPILE_OPTIONS directory property.
These options are used when compiling targets from the current
directory and below.  


Arguments
Arguments to add_compile_options may use ˇ°generator expressionsˇ± with
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
  


Example
Since different compilers support different options, a typical use of
this command is in a compiler-specific conditional clause:
if (MSVC)
    # warning level 4 and all warnings as errors
    add_compile_options(/W4 /WX)
else()
    # lots of warnings and all warnings as errors
    add_compile_options(-Wall -Wextra -pedantic -Werror)
endif()


  


See Also
This command can be used to add any options. However, for
adding preprocessor definitions and include directories it is recommended
to use the more specific commands add_compile_definitions()
and include_directories().
The command target_compile_options() adds target-specific options.
  

