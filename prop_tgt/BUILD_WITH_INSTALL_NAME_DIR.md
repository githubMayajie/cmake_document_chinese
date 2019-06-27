  

# BUILD_WITH_INSTALL_NAME_DIR  
BUILD_WITH_INSTALL_NAME_DIR is a boolean specifying whether the macOS
install_name of a target in the build tree uses the directory given by
INSTALL_NAME_DIR.  This setting only applies to targets on macOS.  

This property is initialized by the value of the variable
CMAKE_BUILD_WITH_INSTALL_NAME_DIR if it is set when a target is
created.  

If this property is not set and policy CMP0068 is not NEW, the
value of BUILD_WITH_INSTALL_RPATH is used in its place.  

