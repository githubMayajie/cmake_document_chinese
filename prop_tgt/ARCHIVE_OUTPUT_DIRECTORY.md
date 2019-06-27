  

# ARCHIVE_OUTPUT_DIRECTORY  
Output directory in which to build ARCHIVE target files.  

This property specifies the directory into which archive target files
should be built.  The property value may use
generator expressions.
Multi-configuration generators (VS, Xcode) append a per-configuration
subdirectory to the specified directory unless a generator expression
is used.  

This property is initialized by the value of the variable
CMAKE_ARCHIVE_OUTPUT_DIRECTORY if it is set when a target is created.  

See also the ARCHIVE_OUTPUT_DIRECTORY_```<CONFIG>``` target property.  

