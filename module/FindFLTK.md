  

# FindFLTK  
Find the Fast Light Toolkit (FLTK) library  


Input Variables
By default this module will search for all of the FLTK components and
add them to the FLTK_LIBRARIES variable.  You can limit the components
which get placed in FLTK_LIBRARIES by defining one or more of the
following three options:

FLTK_SKIP_OPENGL
Set to true to disable searching for the FLTK GL library
FLTK_SKIP_FORMS
Set to true to disable searching for the FLTK Forms library
FLTK_SKIP_IMAGES
Set to true to disable searching for the FLTK Images library

FLTK is composed also by a binary tool. You can set the following option:

FLTK_SKIP_FLUID
Set to true to not look for the FLUID binary

  


Result Variables
The following variables will be defined:

FLTK_FOUND
True if all components not skipped were found
FLTK_INCLUDE_DIR
Path to the include directory for FLTK header files
FLTK_LIBRARIES
List of the FLTK libraries found
FLTK_FLUID_EXECUTABLE
Path to the FLUID binary tool
FLTK_WRAP_UI
True if FLUID is found, used to enable the FLTK_WRAP_UI command

  


Cache Variables
The following cache variables are also available to set or use:

FLTK_BASE_LIBRARY_RELEASE
The FLTK base library (optimized)
FLTK_BASE_LIBRARY_DEBUG
The FLTK base library (debug)
FLTK_GL_LIBRARY_RELEASE
The FLTK GL library (optimized)
FLTK_GL_LIBRARY_DEBUG
The FLTK GL library (debug)
FLTK_FORMS_LIBRARY_RELEASE
The FLTK Forms library (optimized)
FLTK_FORMS_LIBRARY_DEBUG
The FLTK Forms library (debug)
FLTK_IMAGES_LIBRARY_RELEASE
The FLTK Images protobuf library (optimized)
FLTK_IMAGES_LIBRARY_DEBUG
The FLTK Images library (debug)

  

