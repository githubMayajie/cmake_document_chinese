  

# FC  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling Fortran language files. Will only be used
by CMake on the first configuration to determine Fortran compiler, after
which the value for Fortran is stored in the cache as
CMAKE_Fortran_COMPILER. For any
configuration run (including the first), the environment variable will be
ignored if the CMAKE_Fortran_COMPILER
variable is defined.  

