  

# XCODE_GENERATE_SCHEME  
If enabled, the Xcode generator will generate schema files.  These
are useful to invoke analyze, archive, build-for-testing and test
actions from the command line.  

This property is initialized by the value of the variable
CMAKE_XCODE_GENERATE_SCHEME if it is set when a target
is created.  

The following target properties overwrite the default of the
corresponding settings on the ¡°Diagnostic¡± tab for each schema file.
Each of those is initialized by the respective CMAKE_ variable
at target creation time.  


XCODE_SCHEME_ADDRESS_SANITIZER
XCODE_SCHEME_ADDRESS_SANITIZER_USE_AFTER_RETURN
XCODE_SCHEME_DISABLE_MAIN_THREAD_CHECKER
XCODE_SCHEME_DYNAMIC_LIBRARY_LOADS
XCODE_SCHEME_DYNAMIC_LINKER_API_USAGE
XCODE_SCHEME_GUARD_MALLOC
XCODE_SCHEME_MAIN_THREAD_CHECKER_STOP
XCODE_SCHEME_MALLOC_GUARD_EDGES
XCODE_SCHEME_MALLOC_SCRIBBLE
XCODE_SCHEME_MALLOC_STACK
XCODE_SCHEME_THREAD_SANITIZER
XCODE_SCHEME_THREAD_SANITIZER_STOP
XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER
XCODE_SCHEME_UNDEFINED_BEHAVIOUR_SANITIZER_STOP
XCODE_SCHEME_ZOMBIE_OBJECTS
  

The following target properties will be applied on the
¡°Info¡± and ¡°Arguments¡± tab:  


XCODE_SCHEME_ARGUMENTS
XCODE_SCHEME_DEBUG_AS_ROOT
XCODE_SCHEME_ENVIRONMENT
XCODE_SCHEME_EXECUTABLE
  

