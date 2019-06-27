  

# UsewxWidgets  
Convenience include for using wxWidgets library.  

Determines if wxWidgets was FOUND and sets the appropriate libs,
incdirs, flags, etc.  INCLUDE_DIRECTORIES and LINK_DIRECTORIES are
called.  

USAGE  

# Note that for MinGW users the order of libs is important!
find_package(wxWidgets REQUIRED net gl core base)
include(${wxWidgets_USE_FILE})
# and for each of your dependent executable/library targets:
target_link_libraries(```<YourTarget>``` ${wxWidgets_LIBRARIES})

  

DEPRECATED  

LINK_LIBRARIES is not called in favor of adding dependencies per target.

  

AUTHOR  

Jan Woetzel ```<jw -at- mip.informatik.uni-kiel.de>```

  

