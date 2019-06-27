  

# STATIC_LIBRARY_OPTIONS  
Archiver (or MSVC librarian) flags for a static library target.
Targets that are shared libraries, modules, or executables need to use
the LINK_OPTIONS target property.  

This property holds a semicolon-separated list of options
specified so far for its target.  Use set_target_properties() or
set_property() commands to set its content.  

Contents of STATIC_LIBRARY_OPTIONS may use ¡°generator expressions¡± with the
syntax $```<...>```.  See the cmake-generator-expressions(7) manual
for available expressions.  See the cmake-buildsystem(7) manual
for more on defining buildsystem properties.  


Note
This property must be used in preference to STATIC_LIBRARY_FLAGS
property.
  

