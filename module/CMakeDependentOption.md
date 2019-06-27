  

# CMakeDependentOption  
Macro to provide an option dependent on other options.  

This macro presents an option to the user only if a set of other
conditions are true.  When the option is not presented a default value
is used, but any value set by the user is preserved for when the
option is presented again.  Example invocation:  

CMAKE_DEPENDENT_OPTION(USE_FOO "Use Foo" ON
                       "USE_BAR;NOT USE_ZOT" OFF)

  

If USE_BAR is true and USE_ZOT is false, this provides an option
called USE_FOO that defaults to ON.  Otherwise, it sets USE_FOO to
OFF.  If the status of USE_BAR or USE_ZOT ever changes, any value for
the USE_FOO option is saved so that when the option is re-enabled it
retains its old value.  

