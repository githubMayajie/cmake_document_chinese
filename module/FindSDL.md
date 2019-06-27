  

# FindSDL  
Locate SDL library  

This module defines  

SDL_LIBRARY, the name of the library to link against
SDL_FOUND, if false, do not try to link to SDL
SDL_INCLUDE_DIR, where to find SDL.h
SDL_VERSION_STRING, human-readable string containing the version of SDL

  

This module responds to the flag:  

SDL_BUILDING_LIBRARY
  If this is defined, then no SDL_main will be linked in because
  only applications need main().
  Otherwise, it is assumed you are building an application and this
  module will attempt to locate and set the proper link flags
  as part of the returned SDL_LIBRARY variable.

  

Don¡¯t forget to include SDLmain.h and SDLmain.m your project for the
OS X framework based version.  (Other versions link to -lSDLmain which
this module will try to find on your behalf.) Also for OS X, this
module will automatically add the -framework Cocoa on your behalf.  

Additional Note: If you see an empty SDL_LIBRARY_TEMP in your
configuration and no SDL_LIBRARY, it means CMake did not find your SDL
library (SDL.dll, libsdl.so, SDL.framework, etc).  Set
SDL_LIBRARY_TEMP to point to your SDL library, and configure again.
Similarly, if you see an empty SDLMAIN_LIBRARY, you should set this
value as appropriate.  These values are used to generate the final
SDL_LIBRARY variable, but when these values are unset, SDL_LIBRARY
does not get created.  

$SDLDIR is an environment variable that would correspond to the
./configure ¨Cprefix=$SDLDIR used in building SDL.  l.e.galup 9-20-02  

Modified by Eric Wing.  Added code to assist with automated building
by using environmental variables and providing a more
controlled/consistent search behavior.  Added new modifications to
recognize OS X frameworks and additional Unix paths (FreeBSD, etc).
Also corrected the header search path to follow ¡°proper¡± SDL
guidelines.  Added a search for SDLmain which is needed by some
platforms.  Added a search for threads which is needed by some
platforms.  Added needed compile switches for MinGW.  

On OSX, this will prefer the Framework version (if found) over others.
People will have to manually change the cache values of SDL_LIBRARY to
override this selection or set the CMake environment
CMAKE_INCLUDE_PATH to modify the search paths.  

Note that the header path has changed from SDL/SDL.h to just SDL.h
This needed to change because ¡°proper¡± SDL convention is #include
¡°SDL.h¡±, not ```<SDL/SDL.h>```.  This is done for portability reasons
because not all systems place things in SDL/ (see FreeBSD).  

