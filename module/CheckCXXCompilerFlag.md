  

# CheckCXXCompilerFlag  
Check whether the CXX compiler supports a given flag.  



check_cxx_compiler_flag
check_cxx_compiler_flag(```<flag>``` ```<var>```)


Check that the ```<flag>``` is accepted by the compiler without
a diagnostic.  Stores the result in an internal cache entry
named ```<var>```.
  

This command temporarily sets the CMAKE_REQUIRED_DEFINITIONS variable
and calls the check_cxx_source_compiles macro from the
CheckCXXSourceCompiles module.  See documentation of that
module for a listing of variables that can otherwise modify the build.  

A positive result from this check indicates only that the compiler did not
issue a diagnostic message when given the flag.  Whether the flag has any
effect or even a specific one is beyond the scope of this module.  


Note
Since the try_compile() command forwards flags from variables
like CMAKE_CXX_FLAGS, unknown flags
in such variables may cause a false negative for this check.
  

