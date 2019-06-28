  

# CMAKE_GENERATOR  
The generator used to build the project.  See cmake-generators(7).  

The name of the generator that is being used to generate the build
files.  (e.g.  Unix Makefiles, Ninja, etc.)  

The value of this variable should never be modified by project code.
A generator may be selected via the cmake(1) -G option,
interactively in cmake-gui(1), or via the CMAKE_GENERATOR
environment variable.  

