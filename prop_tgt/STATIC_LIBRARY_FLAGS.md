  

# STATIC_LIBRARY_FLAGS  
Archiver (or MSVC librarian) flags for a static library target.
Targets that are shared libraries, modules, or executables need to use
the LINK_OPTIONS or LINK_FLAGS target properties.  

The STATIC_LIBRARY_FLAGS property, managed as a string, can be used to add
extra flags to the link step of a static library target.
STATIC_LIBRARY_FLAGS_```<CONFIG>``` will add to the configuration
```<CONFIG>```, for example, DEBUG, RELEASE, MINSIZEREL,
RELWITHDEBINFO, бн  


Note
This property has been superseded by STATIC_LIBRARY_OPTIONS
property.
  

