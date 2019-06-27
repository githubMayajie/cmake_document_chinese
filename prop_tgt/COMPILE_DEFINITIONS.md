  

# COMPILE_DEFINITIONS  
Preprocessor definitions for compiling a directory¡¯s sources.  

This property specifies the list of options given so far to the
add_compile_definitions() (or add_definitions()) command.  

The COMPILE_DEFINITIONS property may be set to a semicolon-separated
list of preprocessor definitions using the syntax VAR or VAR=value.
Function-style definitions are not supported.  CMake will
automatically escape the value correctly for the native build system
(note that CMake language syntax may require escapes to specify some
values).  

This property will be initialized in each directory by its value in the
directory¡¯s parent.  

CMake will automatically drop some definitions that are not supported
by the native build tool.  

Disclaimer: Most native build tools have poor support for escaping
certain values.  CMake has work-arounds for many cases but some values
may just not be possible to pass correctly.  If a value does not seem
to be escaped correctly, do not attempt to work-around the problem by
adding escape sequences to the value.  Your work-around may break in a
future version of CMake that has improved escape support.  Instead
consider defining the macro in a (configured) header file.  Then
report the limitation.  Known limitations include:  

#          - broken almost everywhere
;          - broken in VS IDE 7.0 and Borland Makefiles
,          - broken in VS IDE
%          - broken in some cases in NMake
& |        - broken in some cases on MinGW
^ ```< >``` \"   - broken in most Make tools on Windows

  

CMake does not reject these values outright because they do work in
some cases.  Use with caution.  

Contents of COMPILE_DEFINITIONS may use ¡°generator expressions¡± with
the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  

The corresponding COMPILE_DEFINITIONS_```<CONFIG>``` property may
be set to specify per-configuration definitions.  Generator expressions
should be preferred instead of setting the alternative property.  

