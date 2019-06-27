  

# SelectLibraryConfigurations  
select_library_configurations(basename)

  

This macro takes a library base name as an argument, and will choose
good values for the variables  

basename_LIBRARY
basename_LIBRARIES
basename_LIBRARY_DEBUG
basename_LIBRARY_RELEASE

  

depending on what has been found and set.  

If only basename_LIBRARY_RELEASE is defined, basename_LIBRARY will
be set to the release value, and basename_LIBRARY_DEBUG will be set
to basename_LIBRARY_DEBUG-NOTFOUND.  If only basename_LIBRARY_DEBUG
is defined, then basename_LIBRARY will take the debug value, and
basename_LIBRARY_RELEASE will be set to basename_LIBRARY_RELEASE-NOTFOUND.  

If the generator supports configuration types, then basename_LIBRARY
and basename_LIBRARIES will be set with debug and optimized flags
specifying the library to be used for the given configuration.  If no
build type has been set or the generator in use does not support
configuration types, then basename_LIBRARY and basename_LIBRARIES
will take only the release value, or the debug value if the release one
is not set.  

