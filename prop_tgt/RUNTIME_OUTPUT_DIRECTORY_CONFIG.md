  

# RUNTIME_OUTPUT_DIRECTORY_```<CONFIG>```  
Per-configuration output directory for
RUNTIME target files.  

This is a per-configuration version of the
RUNTIME_OUTPUT_DIRECTORY target property, but
multi-configuration generators (Visual Studio Generators,
Xcode) do NOT append a
per-configuration subdirectory to the specified directory.  This
property is initialized by the value of the
CMAKE_RUNTIME_OUTPUT_DIRECTORY_```<CONFIG>``` variable if
it is set when a target is created.  

Contents of RUNTIME_OUTPUT_DIRECTORY_```<CONFIG>``` may use
generator expressions.  

