  

# FindLibXslt  
Find the XSL Transformations, Extensible Stylesheet Language
Transformations (XSLT) library (LibXslt)  

Once done this will define  

LIBXSLT_FOUND - system has LibXslt
LIBXSLT_INCLUDE_DIR - the LibXslt include directory
LIBXSLT_LIBRARIES - Link these to LibXslt
LIBXSLT_DEFINITIONS - Compiler switches required for using LibXslt
LIBXSLT_VERSION_STRING - version of LibXslt found (since CMake 2.8.8)

  

Additionally, the following two variables are set (but not required
for using xslt):  


LIBXSLT_EXSLT_LIBRARIES
Link to these if you need to link against the exslt library.
LIBXSLT_XSLTPROC_EXECUTABLE
Contains the full path to the xsltproc executable if found.
  

