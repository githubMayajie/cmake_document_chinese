  

# FindSDL_ttf  
Locate SDL_ttf library  

This module defines:  

SDL_TTF_LIBRARIES, the name of the library to link against
SDL_TTF_INCLUDE_DIRS, where to find the headers
SDL_TTF_FOUND, if false, do not try to link against
SDL_TTF_VERSION_STRING - human-readable string containing the version of SDL_ttf

  

For backward compatibility the following variables are also set:  

SDLTTF_LIBRARY (same value as SDL_TTF_LIBRARIES)
SDLTTF_INCLUDE_DIR (same value as SDL_TTF_INCLUDE_DIRS)
SDLTTF_FOUND (same value as SDL_TTF_FOUND)

  

$SDLDIR is an environment variable that would correspond to the
./configure ¨Cprefix=$SDLDIR used in building SDL.  

Created by Eric Wing.  This was influenced by the FindSDL.cmake
module, but with modifications to recognize OS X frameworks and
additional Unix paths (FreeBSD, etc).  

