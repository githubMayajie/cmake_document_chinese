  

# FindDevIL  
This module locates the developer¡¯s image library.
http://openil.sourceforge.net/  

This module sets:  

IL_LIBRARIES -   the name of the IL library. These include the full path to
                 the core DevIL library. This one has to be linked into the
                 application.
ILU_LIBRARIES -  the name of the ILU library. Again, the full path. This
                 library is for filters and effects, not actual loading. It
                 doesn't have to be linked if the functionality it provides
                 is not used.
ILUT_LIBRARIES - the name of the ILUT library. Full path. This part of the
                 library interfaces with OpenGL. It is not strictly needed
                 in applications.
IL_INCLUDE_DIR - where to find the il.h, ilu.h and ilut.h files.
DevIL_FOUND    - this is set to TRUE if all the above variables were set.
                 This will be set to false if ILU or ILUT are not found,
                 even if they are not needed. In most systems, if one
                 library is found all the others are as well. That's the
                 way the DevIL developers release it.

  

