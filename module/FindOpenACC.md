  

# FindOpenACC  
Detect OpenACC support by the compiler.  

This module can be used to detect OpenACC support in a compiler.
If the compiler supports OpenACC, the flags required to compile with
OpenACC support are returned in variables for the different languages.
Currently, only PGI, GNU and Cray compilers are supported.  


Variables
This module will set the following variables per language in your
project, where ```<lang>``` is one of C, CXX, or Fortran:

OpenACC_```<lang>```_FOUND
Variable indicating if OpenACC support for ```<lang>``` was detected.
OpenACC_```<lang>```_FLAGS
OpenACC compiler flags for ```<lang>```, separated by spaces.

The module will also try to provide the OpenACC version variables:

OpenACC_```<lang>```_SPEC_DATE
Date of the OpenACC specification implemented by the ```<lang>``` compiler.
OpenACC_```<lang>```_VERSION_MAJOR
Major version of OpenACC implemented by the ```<lang>``` compiler.
OpenACC_```<lang>```_VERSION_MINOR
Minor version of OpenACC implemented by the ```<lang>``` compiler.
OpenACC_```<lang>```_VERSION
OpenACC version implemented by the ```<lang>``` compiler.

The specification date is formatted as given in the OpenACC standard:
yyyymm where yyyy and mm represents the year and month of
the OpenACC specification implemented by the ```<lang>``` compiler.
  


Input Variables
OpenACC_ACCEL_TARGET=```<target>```
If set, will the correct target accelerator flag set to the ```<target>``` will
be returned with OpenACC_```<lang>```_FLAGS.
  

