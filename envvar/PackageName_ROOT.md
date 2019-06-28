  

# ```<PackageName>```_ROOT  
Calls to find_package(```<PackageName>```) will search in prefixes
specified by the ```<PackageName>```_ROOT CMake variable, where
```<PackageName>``` is the name given to the find_package() call
and _ROOT is literal.  For example, find_package(Foo) will search
prefixes specified in the Foo_ROOT CMake variable (if set).
See policy CMP0074.  

This variable may hold a single prefix or a
semicolon-separated list of multiple prefixes.  

See also the ```<PackageName>```_ROOT environment variable.  

