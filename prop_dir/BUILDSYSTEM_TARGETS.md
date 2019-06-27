  

# BUILDSYSTEM_TARGETS  
This read-only directory property contains a
semicolon-separated list of buildsystem targets added in the
directory by calls to the add_library(), add_executable(),
and add_custom_target() commands.  The list does not include any
Imported Targets or Alias Targets, but does include
Interface Libraries.  Each entry in the list is the logical name
of a target, suitable to pass to the get_property() command
TARGET option.  

