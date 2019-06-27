  

# CMAKE_BUILD_RPATH  
Semicolon-separated list specifying runtime path (RPATH)
entries to add to binaries linked in the build tree (for platforms that
support it).  The entries will not be used for binaries in the install
tree.  See also the CMAKE_INSTALL_RPATH variable.  

This is used to initialize the BUILD_RPATH target property
for all targets.  

