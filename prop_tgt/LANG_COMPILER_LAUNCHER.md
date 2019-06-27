  

# ```<LANG>```_COMPILER_LAUNCHER  
This property is implemented only when ```<LANG>``` is C, CXX,
Fortran, or CUDA.  

Specify a semicolon-separated list containing a command line
for a compiler launching tool. The Makefile Generators and the
Ninja generator will run this tool and pass the compiler and
its arguments to the tool. Some example tools are distcc and ccache.  

This property is initialized by the value of
the CMAKE_```<LANG>```_COMPILER_LAUNCHER variable if it is set
when a target is created.  
