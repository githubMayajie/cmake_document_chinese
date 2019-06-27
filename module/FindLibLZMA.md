  

# FindLibLZMA  
Find LZMA compression algorithm headers and library.  


Imported Targets
This module defines IMPORTED target LibLZMA::LibLZMA, if
liblzma has been found.
  


Result variables
This module will set the following variables in your project:

LIBLZMA_FOUND
True if liblzma headers and library were found.
LIBLZMA_INCLUDE_DIRS
Directory where liblzma headers are located.
LIBLZMA_LIBRARIES
Lzma libraries to link against.
LIBLZMA_HAS_AUTO_DECODER
True if lzma_auto_decoder() is found (required).
LIBLZMA_HAS_EASY_ENCODER
True if lzma_easy_encoder() is found (required).
LIBLZMA_HAS_LZMA_PRESET
True if lzma_lzma_preset() is found (required).
LIBLZMA_VERSION_MAJOR
The major version of lzma
LIBLZMA_VERSION_MINOR
The minor version of lzma
LIBLZMA_VERSION_PATCH
The patch version of lzma
LIBLZMA_VERSION_STRING
version number as a string (ex: ¡°5.0.3¡±)

  

