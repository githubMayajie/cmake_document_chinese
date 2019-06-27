  

# FindGit  
The module defines the following IMPORTED targets (when
CMAKE_ROLE is PROJECT):  


Git::Git
Executable of the Git command-line client.
  

The module defines the following variables:  


GIT_EXECUTABLE
Path to Git command-line client.
Git_FOUND, GIT_FOUND
True if the Git command-line client was found.
GIT_VERSION_STRING
The version of Git found.
  

Example usage:  

find_package(Git)
if(Git_FOUND)
  message("Git found: ${GIT_EXECUTABLE}")
endif()

  

