  

# CMAKE_DEBUG_TARGET_PROPERTIES  
Enables tracing output for target properties.  

This variable can be populated with a list of properties to generate
debug output for when evaluating target properties.  Currently it can
only be used when evaluating:  


AUTOUIC_OPTIONS
COMPILE_DEFINITIONS
COMPILE_FEATURES
COMPILE_OPTIONS
INCLUDE_DIRECTORIES
LINK_DIRECTORIES
LINK_OPTIONS
POSITION_INDEPENDENT_CODE
SOURCES
  

target properties and any other property listed in
COMPATIBLE_INTERFACE_STRING and other
COMPATIBLE_INTERFACE_ properties.  It outputs an origin for each entry
in the target property.  Default is unset.  

