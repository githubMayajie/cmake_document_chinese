  

# CMAKE_```<LANG>```_CLANG_TIDY  
Default value for ```<LANG>```_CLANG_TIDY target property
when ```<LANG>``` is C or CXX.  

This variable is used to initialize the property on each target as it is
created.  For example:  

set(CMAKE_CXX_CLANG_TIDY clang-tidy -checks=-*,readability-*)
add_executable(foo foo.cxx)

  

