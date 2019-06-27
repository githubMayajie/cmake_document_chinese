  

# FindBacktrace  
Find provider for backtrace(3).  

Checks if OS supports backtrace(3) via either libc or custom library.
This module defines the following variables:  


Backtrace_HEADER
The header file needed for backtrace(3). Cached.
Could be forcibly set by user.
Backtrace_INCLUDE_DIRS
The include directories needed to use backtrace(3) header.
Backtrace_LIBRARIES
The libraries (linker flags) needed to use backtrace(3), if any.
Backtrace_FOUND
Is set if and only if backtrace(3) support detected.
  

The following cache variables are also available to set or use:  


Backtrace_LIBRARY
The external library providing backtrace, if any.
Backtrace_INCLUDE_DIR
The directory holding the backtrace(3) header.
  

Typical usage is to generate of header file using configure_file()
with the contents like the following:  

#cmakedefine01 Backtrace_FOUND
#if Backtrace_FOUND
# include ```<${Backtrace_HEADER}>```
#endif

  

And then reference that generated header file in actual source.  

