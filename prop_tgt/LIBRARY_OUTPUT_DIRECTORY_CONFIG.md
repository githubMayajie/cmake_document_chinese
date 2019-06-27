  

# LIBRARY_OUTPUT_DIRECTORY_```<CONFIG>```  
Per-configuration output directory for
LIBRARY target files.  

This is a per-configuration version of the
LIBRARY_OUTPUT_DIRECTORY target property, but
multi-configuration generators (Visual Studio Generators,
Xcode) do NOT append a
per-configuration subdirectory to the specified directory.  This
property is initialized by the value of the
CMAKE_LIBRARY_OUTPUT_DIRECTORY_```<CONFIG>``` variable if
it is set when a target is created.  

Contents of LIBRARY_OUTPUT_DIRECTORY_```<CONFIG>``` may use
generator expressions.  

