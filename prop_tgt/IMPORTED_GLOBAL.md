  

# IMPORTED_GLOBAL  
Indication of whether an IMPORTED target is
globally visible.  

The boolean value of this property is True for targets created with the
IMPORTED GLOBAL options to add_executable() or
add_library(). It is always False for targets built within the
project.  

For targets created with the IMPORTED option to
add_executable() or add_library() but without the
additional option GLOBAL this is False, too. However, setting this
property for such a locally IMPORTED target to True promotes that
target to global scope. This promotion can only be done in the same
directory where that IMPORTED target was created in the first place.  

Once an imported target has been made global, it cannot be changed back to
non-global. Therefore, if a project sets this property, it may only
provide a value of True. CMake will issue an error if the project tries to
set the property to a non-True value, even if the value was already False.  

