  

# FindRuby  
Find Ruby  

This module finds if Ruby is installed and determines where the
include files and libraries are.  Ruby 1.8, 1.9, 2.0 and 2.1 are
supported.  

The minimum required version of Ruby can be specified using the
standard syntax, e.g.  find_package(Ruby 1.8)  

It also determines what the name of the library is.  This code sets
the following variables:  


RUBY_EXECUTABLE
full path to the ruby binary
RUBY_INCLUDE_DIRS
include dirs to be used when using the ruby library
RUBY_LIBRARY
full path to the ruby library
RUBY_VERSION
the version of ruby which was found, e.g. ¡°1.8.7¡±
RUBY_FOUND
set to true if ruby ws found successfully
  

Also:  


RUBY_INCLUDE_PATH
same as RUBY_INCLUDE_DIRS, only provided for compatibility reasons, don¡¯t use it
  

