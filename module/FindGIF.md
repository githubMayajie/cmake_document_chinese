  

# FindGIF  
This finds the Graphics Interchange Format (GIF) library (giflib)  


Imported targets
This module defines the following IMPORTED target:

GIF::GIF
The giflib library, if found.

  


Result variables
This module will set the following variables in your project:

GIF_FOUND
If false, do not try to use GIF.
GIF_INCLUDE_DIRS
where to find gif_lib.h, etc.
GIF_LIBRARIES
the libraries needed to use GIF.
GIF_VERSION
3, 4 or a full version string (eg 5.1.4) for versions >```= 4.1.6.

  


Cache variables
The following cache variables may also be set:

GIF_INCLUDE_DIR
where to find the GIF headers.
GIF_LIBRARY
where to find the GIF library.

  


Hints
GIF_DIR is an environment variable that would correspond to the
./configure --prefix=$GIF_DIR.
  

