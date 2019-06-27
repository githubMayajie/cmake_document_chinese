  

# FindSDL_image  
Locate SDL_image library  

This module defines:  

SDL_IMAGE_LIBRARIES, the name of the library to link against
SDL_IMAGE_INCLUDE_DIRS, where to find the headers
SDL_IMAGE_FOUND, if false, do not try to link against
SDL_IMAGE_VERSION_STRING - human-readable string containing the
                           version of SDL_image

  

For backward compatibility the following variables are also set:  

SDLIMAGE_LIBRARY (same value as SDL_IMAGE_LIBRARIES)
SDLIMAGE_INCLUDE_DIR (same value as SDL_IMAGE_INCLUDE_DIRS)
SDLIMAGE_FOUND (same value as SDL_IMAGE_FOUND)

  

$SDLDIR is an environment variable that would correspond to the
./configure ¨Cprefix=$SDLDIR used in building SDL.  

Created by Eric Wing.  This was influenced by the FindSDL.cmake
module, but with modifications to recognize OS X frameworks and
additional Unix paths (FreeBSD, etc).  

