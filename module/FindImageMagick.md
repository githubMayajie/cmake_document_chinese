  

# FindImageMagick  
Find ImageMagick binary suite.  

This module will search for a set of ImageMagick tools specified as
components in the find_package() call.  Typical components include,
but are not limited to (future versions of ImageMagick might have
additional components not listed here):  

animate
compare
composite
conjure
convert
display
identify
import
mogrify
montage
stream

  

If no component is specified in the find_package() call, then it only
searches for the ImageMagick executable directory.  This code defines
the following variables:  

ImageMagick_FOUND                  - TRUE if all components are found.
ImageMagick_EXECUTABLE_DIR         - Full path to executables directory.
ImageMagick_```<component>```_FOUND      - TRUE if ```<component>``` is found.
ImageMagick_```<component>```_EXECUTABLE - Full path to ```<component>``` executable.
ImageMagick_VERSION_STRING         - the version of ImageMagick found
                                     (since CMake 2.8.8)

  

ImageMagick_VERSION_STRING will not work for old versions like 5.2.3.  

There are also components for the following ImageMagick APIs:  

Magick++
MagickWand
MagickCore

  

For these components the following variables are set:  

ImageMagick_FOUND                    - TRUE if all components are found.
ImageMagick_INCLUDE_DIRS             - Full paths to all include dirs.
ImageMagick_LIBRARIES                - Full paths to all libraries.
ImageMagick_```<component>```_FOUND        - TRUE if ```<component>``` is found.
ImageMagick_```<component>```_INCLUDE_DIRS - Full path to ```<component>``` include dirs.
ImageMagick_```<component>```_LIBRARIES    - Full path to ```<component>``` libraries.

  

Example Usages:  

find_package(ImageMagick)
find_package(ImageMagick COMPONENTS convert)
find_package(ImageMagick COMPONENTS convert mogrify display)
find_package(ImageMagick COMPONENTS Magick++)
find_package(ImageMagick COMPONENTS Magick++ convert)

  

Note that the standard find_package() features are supported (i.e.,
QUIET, REQUIRED, etc.).  

