  

# CheckStructHasMember  
Check if the given struct or class has the specified member variable  



CHECK_STRUCT_HAS_MEMBER
CHECK_STRUCT_HAS_MEMBER(```<struct>``` ```<member>``` ```<header>``` ```<variable>```
                        [LANGUAGE ```<language>```])


```<struct>``` - the name of the struct or class you are interested in
```<member>``` - the member which existence you want to check
```<header>``` - the header(s) where the prototype should be declared
```<variable>``` - variable to store the result
```<language>``` - the compiler to use (C or CXX)


  

The following variables may be set before calling this macro to modify
the way the check is run:  

CMAKE_REQUIRED_FLAGS = string of compile command line flags
CMAKE_REQUIRED_DEFINITIONS = list of macros to define (-DFOO=bar)
CMAKE_REQUIRED_INCLUDES = list of include directories
CMAKE_REQUIRED_LINK_OPTIONS = list of options to pass to link command
CMAKE_REQUIRED_LIBRARIES = list of libraries to link
CMAKE_REQUIRED_QUIET = execute quietly without messages

  

Example:  

CHECK_STRUCT_HAS_MEMBER("struct timeval" tv_sec sys/select.h
                        HAVE_TIMEVAL_TV_SEC LANGUAGE C)

  

