  

# ```<LANG>```_CPPLINT  
This property is supported only when ```<LANG>``` is C or CXX.  

Specify a semicolon-separated list containing a command line
for the cpplint style checker.  The Makefile Generators and the
Ninja generator will run cpplint along with the compiler
and report any problems.  

This property is initialized by the value of the
CMAKE_```<LANG>```_CPPLINT variable if it is set when a target is
created.  

