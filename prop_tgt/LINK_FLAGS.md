  

# LINK_FLAGS  
Additional flags to use when linking this target if it is a shared library,
module library, or an executable. Static libraries need to use
STATIC_LIBRARY_OPTIONS or STATIC_LIBRARY_FLAGS
properties.  

The LINK_FLAGS property, managed as a string, can be used to add extra
flags to the link step of a target.  LINK_FLAGS_```<CONFIG>``` will add
to the configuration ```<CONFIG>```, for example, DEBUG, RELEASE,
MINSIZEREL, RELWITHDEBINFO, бн  


Note
This property has been superseded by LINK_OPTIONS property.
  

