  

# FindPackageMessage  
find_package_message(```<name>``` "message for user" "find result details")

  

This function is intended to be used in FindXXX.cmake modules files.
It will print a message once for each unique find result.  This is
useful for telling the user where a package was found.  The first
argument specifies the name (XXX) of the package.  The second argument
specifies the message to display.  The third argument lists details
about the find result so that if they change the message will be
displayed again.  The macro also obeys the QUIET argument to the
find_package command.  

Example:  

if(X11_FOUND)
  find_package_message(X11 "Found X11: ${X11_X11_LIB}"
    "[${X11_X11_LIB}][${X11_INCLUDE_DIR}]")
else()
 ...
endif()

  

