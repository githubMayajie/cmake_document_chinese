  

# CheckTypeSize  
Check sizeof a type  



CHECK_TYPE_SIZE
CHECK_TYPE_SIZE(TYPE VARIABLE [BUILTIN_TYPES_ONLY]
                              [LANGUAGE ```<language>```])


Check if the type exists and determine its size.  On return,
HAVE_${VARIABLE} holds the existence of the type, and ${VARIABLE}
holds one of the following:
```<size>``` = type has non-zero size ```<size>```
"0"    = type has arch-dependent size (see below)
""     = type does not exist


Both HAVE_${VARIABLE} and ${VARIABLE} will be created as internal
cache variables.
Furthermore, the variable ${VARIABLE}_CODE holds C preprocessor code
to define the macro ${VARIABLE} to the size of the type, or leave
the macro undefined if the type does not exist.
The variable ${VARIABLE} may be 0 when
CMAKE_OSX_ARCHITECTURES has multiple architectures for building
OS X universal binaries.  This indicates that the type size varies across
architectures.  In this case ${VARIABLE}_CODE contains C preprocessor
tests mapping from each architecture macro to the corresponding type size.
The list of architecture macros is stored in ${VARIABLE}_KEYS, and the
value for each key is stored in ${VARIABLE}-${KEY}.
If the BUILTIN_TYPES_ONLY option is not given, the macro checks for
headers ```<sys/types.h>```, ```<stdint.h>```, and ```<stddef.h>```, and saves
results in HAVE_SYS_TYPES_H, HAVE_STDINT_H, and HAVE_STDDEF_H.
The type size check automatically includes the available headers, thus
supporting checks of types defined in the headers.
If LANGUAGE is set, the specified compiler will be used to perform the
check. Acceptable values are C and CXX.
  

Despite the name of the macro you may use it to check the size of more
complex expressions, too.  To check e.g.  for the size of a struct
member you can do something like this:  

check_type_size("((struct something*)0)->```member" SIZEOF_MEMBER)

  

The following variables may be set before calling this macro to modify
the way the check is run:  

CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LINK_OPTIONS  = list of options to pass to link command
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages
CMAKE_EXTRA_INCLUDE_FILES = list of extra headers to include

  

