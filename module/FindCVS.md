  

# FindCVS  
Find the Concurrent Versions System (CVS).  

The module defines the following variables:  

CVS_EXECUTABLE - path to cvs command line client
CVS_FOUND - true if the command line client was found

  

Example usage:  

find_package(CVS)
if(CVS_FOUND)
  message("CVS found: ${CVS_EXECUTABLE}")
endif()

  

