  

# FindIntl  
Find the Gettext libintl headers and libraries.  

This module reports information about the Gettext libintl
installation in several variables.  General variables:  

Intl_FOUND - true if the libintl headers and libraries were found
Intl_INCLUDE_DIRS - the directory containing the libintl headers
Intl_LIBRARIES - libintl libraries to be linked

  

The following cache variables may also be set:  

Intl_INCLUDE_DIR - the directory containing the libintl headers
Intl_LIBRARY - the libintl library (if any)

  


Note
On some platforms, such as Linux with GNU libc, the gettext
functions are present in the C standard library and libintl
is not required.  Intl_LIBRARIES will be empty in this
case.
  


Note
If you wish to use the Gettext tools (msgmerge,
msgfmt, etc.), use FindGettext.
  

