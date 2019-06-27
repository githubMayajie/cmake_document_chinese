  

# CheckLanguage  
Check if a language can be enabled  

Usage:  

check_language(```<lang>```)

  

where ```<lang>``` is a language that may be passed to enable_language()
such as Fortran.  If CMAKE_```<LANG>```_COMPILER is already defined
the check does nothing.  Otherwise it tries enabling the language in a
test project.  The result is cached in CMAKE_```<LANG>```_COMPILER
as the compiler that was found, or NOTFOUND if the language cannot be
enabled. For CUDA which can have an explicit host compiler, the cache
CMAKE_CUDA_HOST_COMPILER variable will be set if it was required
for compilation.  

Example:  

check_language(Fortran)
if(CMAKE_Fortran_COMPILER)
  enable_language(Fortran)
else()
  message(STATUS "No Fortran support")
endif()

  

