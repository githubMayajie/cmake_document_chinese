  

# FindPatch  
The module defines the following variables:  


Patch_EXECUTABLE
Path to patch command-line executable.
Patch_FOUND
True if the patch command-line executable was found.
  

The following IMPORTED targets are also defined:  


Patch::patch
The command-line executable.
  

Example usage:  

find_package(Patch)
if(Patch_FOUND)
  message("Patch found: ${Patch_EXECUTABLE}")
endif()

  

