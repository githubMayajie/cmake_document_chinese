  

# CheckIPOSupported  
Check whether the compiler supports an interprocedural optimization (IPO/LTO).
Use this before enabling the INTERPROCEDURAL_OPTIMIZATION target
property.  



check_ipo_supported
check_ipo_supported([RESULT ```<result>```] [OUTPUT ```<output>```]
                    [LANGUAGES ```<lang>```...])


Options are:

RESULT ```<result>```
Set ```<result>``` variable to YES if IPO is supported by the
compiler and NO otherwise.  If this option is not given then
the command will issue a fatal error if IPO is not supported.
OUTPUT ```<output>```
Set ```<output>``` variable with details about any error.
LANGUAGES ```<lang>```...
Specify languages whose compilers to check.
Languages C, CXX, and Fortran are supported.

  

It makes no sense to use this module when CMP0069 is set to OLD so
module will return error in this case. See policy CMP0069 for details.  


Examples
check_ipo_supported() # fatal error if IPO is not supported
set_property(TARGET foo PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)


# Optional IPO. Do not use IPO if it's not supported by compiler.
check_ipo_supported(RESULT result OUTPUT output)
if(result)
  set_property(TARGET foo PROPERTY INTERPROCEDURAL_OPTIMIZATION TRUE)
else()
  message(WARNING "IPO is not supported: ${output}")
endif()


  

