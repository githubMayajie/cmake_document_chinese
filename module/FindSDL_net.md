  

# FindSDL_net  
Locate SDL_net library  

This module defines:  

SDL_NET_LIBRARIES, the name of the library to link against
SDL_NET_INCLUDE_DIRS, where to find the headers
SDL_NET_FOUND, if false, do not try to link against
SDL_NET_VERSION_STRING - human-readable string containing the version of SDL_net

  

For backward compatibility the following variables are also set:  

SDLNET_LIBRARY (same value as SDL_NET_LIBRARIES)
SDLNET_INCLUDE_DIR (same value as SDL_NET_INCLUDE_DIRS)
SDLNET_FOUND (same value as SDL_NET_FOUND)

  

$SDLDIR is an environment variable that would correspond to the
./configure ¨Cprefix=$SDLDIR used in building SDL.  

Created by Eric Wing.  This was influenced by the FindSDL.cmake
module, but with modifications to recognize OS X frameworks and
additional Unix paths (FreeBSD, etc).  

