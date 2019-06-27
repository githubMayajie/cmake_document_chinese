  

# FindIconv  
This module finds the iconv() POSIX.1 functions on the system.
These functions might be provided in the regular C library or externally
in the form of an additional library.  

The following variables are provided to indicate iconv support:  



Iconv_FOUND
Variable indicating if the iconv support was found.
  



Iconv_INCLUDE_DIRS
The directories containing the iconv headers.
  



Iconv_LIBRARIES
The iconv libraries to be linked.
  



Iconv_IS_BUILT_IN
A variable indicating whether iconv support is stemming from the
C library or not. Even if the C library provides iconv(), the presence of
an external libiconv implementation might lead to this being false.
  

Additionally, the following IMPORTED target is being provided:  



Iconv::Iconv
Imported target for using iconv.
  

The following cache variables may also be set:  



Iconv_INCLUDE_DIR
The directory containing the iconv headers.
  



Iconv_LIBRARY
The iconv library (if not implicitly given in the C library).
  


Note
On POSIX platforms, iconv might be part of the C library and the cache
variables Iconv_INCLUDE_DIR and Iconv_LIBRARY might be empty.
  

