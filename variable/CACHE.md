  

# CACHE  
Operator to read cache variables.  

Use the syntax $CACHE{VAR} to read cache entry VAR.
See the cmake-language(7) variables
documentation for more complete documentation of the interaction of
normal variables and cache entries.  

When evaluating Variable References of the form ${VAR},
CMake first searches for a normal variable with that name, and if not
found CMake will search for a cache entry with that name.
The $CACHE{VAR} syntax can be used to do direct cache lookup and
ignore any existing normal variable.  

See the set() and unset() commands to see how to
write or remove cache variables.  

