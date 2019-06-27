  

# MacroAddFileDependencies  
MACRO_ADD_FILE_DEPENDENCIES(```<_file>``` depend_files¡­)  

Using the macro MACRO_ADD_FILE_DEPENDENCIES() is discouraged.  There
are usually better ways to specify the correct dependencies.  

MACRO_ADD_FILE_DEPENDENCIES(```<_file>``` depend_files¡­) is just a
convenience wrapper around the OBJECT_DEPENDS source file property.
You can just use set_property(SOURCE ```<file>``` APPEND PROPERTY
OBJECT_DEPENDS depend_files) instead.  

