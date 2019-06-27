  

# FindSDL_mixer  
Locate SDL_mixer library  

This module defines:  

SDL_MIXER_LIBRARIES, the name of the library to link against
SDL_MIXER_INCLUDE_DIRS, where to find the headers
SDL_MIXER_FOUND, if false, do not try to link against
SDL_MIXER_VERSION_STRING - human-readable string containing the
                           version of SDL_mixer

  

For backward compatibility the following variables are also set:  

SDLMIXER_LIBRARY (same value as SDL_MIXER_LIBRARIES)
SDLMIXER_INCLUDE_DIR (same value as SDL_MIXER_INCLUDE_DIRS)
SDLMIXER_FOUND (same value as SDL_MIXER_FOUND)

  

$SDLDIR is an environment variable that would correspond to the
./configure ¨Cprefix=$SDLDIR used in building SDL.  

Created by Eric Wing.  This was influenced by the FindSDL.cmake
module, but with modifications to recognize OS X frameworks and
additional Unix paths (FreeBSD, etc).  

