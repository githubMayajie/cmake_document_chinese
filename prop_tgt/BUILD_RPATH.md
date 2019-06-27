  

# BUILD_RPATH  
A semicolon-separated list specifying runtime path (RPATH)
entries to add to binaries linked in the build tree (for platforms that
support it).  The entries will not be used for binaries in the install
tree.  See also the INSTALL_RPATH target property.  

This property is initialized by the value of the variable
CMAKE_BUILD_RPATH if it is set when a target is created.  

