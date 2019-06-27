  

# CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY  
Skip User Package Registry in find_package() calls.  

In some cases, for example to locate only system wide installations, it
is not desirable to use the User Package Registry when searching
for packages. If the CMAKE_FIND_PACKAGE_NO_PACKAGE_REGISTRY
variable is enabled, all the find_package() commands will skip
the User Package Registry as if they were called with the
NO_CMAKE_PACKAGE_REGISTRY argument.  

See also Disabling the Package Registry.  

