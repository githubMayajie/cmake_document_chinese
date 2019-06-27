  

# CMakePrintHelpers  
Convenience functions for printing properties and variables, useful
e.g. for debugging.  

cmake_print_properties([TARGETS target1 ..  targetN]
                      [SOURCES source1 .. sourceN]
                      [DIRECTORIES dir1 .. dirN]
                      [TESTS test1 .. testN]
                      [CACHE_ENTRIES entry1 .. entryN]
                      PROPERTIES prop1 .. propN )

  

This function prints the values of the properties of the given targets,
source files, directories, tests or cache entries.  Exactly one of the
scope keywords must be used.  Example:  

cmake_print_properties(TARGETS foo bar PROPERTIES
                       LOCATION INTERFACE_INCLUDE_DIRS)

  

This will print the LOCATION and INTERFACE_INCLUDE_DIRS properties for
both targets foo and bar.  

cmake_print_variables(var1 var2 ..  varN)

  

This function will print the name of each variable followed by its value.
Example:  

cmake_print_variables(CMAKE_C_COMPILER CMAKE_MAJOR_VERSION DOES_NOT_EXIST)

  

Gives:  

-- CMAKE_C_COMPILER="/usr/bin/gcc" ; CMAKE_MAJOR_VERSION="2" ; DOES_NOT_EXIST=""

  

