  

# CMakeFindPackageMode  
This file is executed by cmake when invoked with ¨Cfind-package.  It
expects that the following variables are set using -D:  


NAME
name of the package
COMPILER_ID
the CMake compiler ID for which the result is,
i.e. GNU/Intel/Clang/MSVC, etc.
LANGUAGE
language for which the result will be used,
i.e. C/CXX/Fortran/ASM
MODE

EXIST
only check for existence of the given package
COMPILE
print the flags needed for compiling an object file which uses
the given package
LINK
print the flags needed for linking when using the given package


QUIET
if TRUE, don¡¯t print anything
  

