  

# CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY  
Skip System Package Registry in find_package() calls.  

In some cases, it is not desirable to use the
System Package Registry when searching for packages. If the
CMAKE_FIND_PACKAGE_NO_SYSTEM_PACKAGE_REGISTRY variable is
enabled, all the find_package() commands will skip
the System Package Registry as if they were called with the
NO_CMAKE_SYSTEM_PACKAGE_REGISTRY argument.  

See also Disabling the Package Registry.  

