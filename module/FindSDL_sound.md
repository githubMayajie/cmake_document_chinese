  

# FindSDL_sound  
Locates the SDL_sound library  

This module depends on SDL being found and must be called AFTER
FindSDL.cmake is called.  

This module defines  

SDL_SOUND_INCLUDE_DIR, where to find SDL_sound.h
SDL_SOUND_FOUND, if false, do not try to link to SDL_sound
SDL_SOUND_LIBRARIES, this contains the list of libraries that you need
  to link against.
SDL_SOUND_EXTRAS, this is an optional variable for you to add your own
  flags to SDL_SOUND_LIBRARIES. This is prepended to SDL_SOUND_LIBRARIES.
  This is available mostly for cases this module failed to anticipate for
  and you must add additional flags. This is marked as ADVANCED.
SDL_SOUND_VERSION_STRING, human-readable string containing the
  version of SDL_sound

  

This module also defines (but you shouldn¡¯t need to use directly)  

SDL_SOUND_LIBRARY, the name of just the SDL_sound library you would link
against. Use SDL_SOUND_LIBRARIES for you link instructions and not this one.

  

And might define the following as needed  

MIKMOD_LIBRARY
MODPLUG_LIBRARY
OGG_LIBRARY
VORBIS_LIBRARY
SMPEG_LIBRARY
FLAC_LIBRARY
SPEEX_LIBRARY

  

Typically, you should not use these variables directly, and you should
use SDL_SOUND_LIBRARIES which contains SDL_SOUND_LIBRARY and the other
audio libraries (if needed) to successfully compile on your system.  

Created by Eric Wing.  This module is a bit more complicated than the
other FindSDL* family modules.  The reason is that SDL_sound can be
compiled in a large variety of different ways which are independent of
platform.  SDL_sound may dynamically link against other 3rd party
libraries to get additional codec support, such as Ogg Vorbis, SMPEG,
ModPlug, MikMod, FLAC, Speex, and potentially others.  Under some
circumstances which I don¡¯t fully understand, there seems to be a
requirement that dependent libraries of libraries you use must also be
explicitly linked against in order to successfully compile.  SDL_sound
does not currently have any system in place to know how it was
compiled.  So this CMake module does the hard work in trying to
discover which 3rd party libraries are required for building (if any).
This module uses a brute force approach to create a test program that
uses SDL_sound, and then tries to build it.  If the build fails, it
parses the error output for known symbol names to figure out which
libraries are needed.  

Responds to the $SDLDIR and $SDLSOUNDDIR environmental variable that
would correspond to the ./configure ¨Cprefix=$SDLDIR used in building
SDL.  

On OSX, this will prefer the Framework version (if found) over others.
People will have to manually change the cache values of SDL_LIBRARY to
override this selectionor set the CMake environment CMAKE_INCLUDE_PATH
to modify the search paths.  

