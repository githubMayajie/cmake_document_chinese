  

# SKIP_AUTOUIC  
Exclude the source file from AUTOUIC processing (for Qt projects).  

SKIP_AUTOUIC can be set on C++ header and source files and on
.ui files.  

For broader exclusion control see SKIP_AUTOGEN.  


EXAMPLE
# ...
set_property(SOURCE file.h PROPERTY SKIP_AUTOUIC ON)
set_property(SOURCE file.cpp PROPERTY SKIP_AUTOUIC ON)
set_property(SOURCE widget.ui PROPERTY SKIP_AUTOUIC ON)
# ...


  

