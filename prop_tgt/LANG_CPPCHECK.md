  

# ```<LANG>```_CPPCHECK  
This property is supported only when ```<LANG>``` is C or CXX.  

Specify a semicolon-separated list containing a command line
for the cppcheck static analysis tool.  The Makefile Generators
and the Ninja generator will run cppcheck along with the
compiler and report any problems.  If the command-line specifies the
exit code options to cppcheck then the build  will fail if the
tool returns non-zero.  

This property is initialized by the value of the
CMAKE_```<LANG>```_CPPCHECK variable if it is set when a target is
created.  
