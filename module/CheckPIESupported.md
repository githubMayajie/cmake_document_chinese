  

# CheckPIESupported  
Check whether the linker supports Position Independent Code (PIE) or No
Position Independent Code (NO_PIE) for executables.
Use this to ensure that the POSITION_INDEPENDENT_CODE target
property for executables will be honored at link time.  



check_pie_supported
check_pie_supported([OUTPUT_VARIABLE ```<output>```]
                    [LANGUAGES ```<lang>```...])


Options are:

OUTPUT_VARIABLE ```<output>```
Set ```<output>``` variable with details about any error.
LANGUAGES ```<lang>```...
Check the linkers used for each of the specified languages.
Supported languages are C, CXX, and Fortran.

  

It makes no sense to use this module when CMP0083 is set to OLD,
so the command will return an error in this case.  See policy CMP0083
for details.  


Variables
For each language checked, two boolean cache variables are defined.


CMAKE_```<lang>```_LINK_PIE_SUPPORTED
Set to YES if PIE is supported by the linker and NO otherwise.
CMAKE_```<lang>```_LINK_NO_PIE_SUPPORTED
Set to YES if NO_PIE is supported by the linker and NO otherwise.


  


Examples
check_pie_supported()
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)


# Retrieve any error message.
check_pie_supported(OUTPUT_VARIABLE output LANGUAGES C)
set_property(TARGET foo PROPERTY POSITION_INDEPENDENT_CODE TRUE)
if(NOT CMAKE_C_LINK_PIE_SUPPORTED)
  message(WARNING "PIE is not supported at link time: ${output}.\n"
                  "PIE link options will not be passed to linker.")
endif()


  

