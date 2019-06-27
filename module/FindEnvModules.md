  

# FindEnvModules  
Locate an environment module implementation and make commands available to
CMake scripts to use them.  This is compatible with both Lua-based Lmod
and TCL-based EnvironmentModules.  

This module is intended for the use case of setting up the compiler and library
environment within a CTest Script (ctest -S).  It can
also be used in a CMake Script (cmake -P).  


Note
The loaded environment will not survive past the end of the calling process.
Do not use this module in project code (CMakeLists.txt files) to load
a compiler environment; it will not be available during the build.  Instead
load the environment manually before running CMake or using the generated
build system.
  


Example Usage
set(CTEST_BUILD_NAME "CrayLinux-CrayPE-Cray-dynamic")
set(CTEST_BUILD_CONFIGURATION Release)
set(CTEST_BUILD_FLAGS "-k -j8")
set(CTEST_CMAKE_GENERATOR "Unix Makefiles")

...

find_package(EnvModules REQUIRED)

env_module(purge)
env_module(load modules)
env_module(load craype)
env_module(load PrgEnv-cray)
env_module(load craype-knl)
env_module(load cray-mpich)
env_module(load cray-libsci)

set(ENV{CRAYPE_LINK_TYPE} dynamic)

...


  


Result Variables
This module will set the following variables in your project:

EnvModules_FOUND
True if a compatible environment modules framework was found.

  


Cache Variables
The following cache variable will be set:

EnvModules_COMMAND
The low level module command to use.  Currently supported
implementations are the Lua based Lmod and TCL based EnvironmentModules.

  


Environment Variables

ENV{MODULESHOME}
Usually set by the module environment implementation, used as a hint to
locate the module command to execute.

  


Provided Functions
This defines the following CMake functions for interacting with environment
modules:


env_module
Execute an aribitrary module command:
env_module(cmd arg1 ... argN)
env_module(
  COMMAND cmd arg1 ... argN
  [OUTPUT_VARIABLE ```<out-var>```]
  [RESULT_VARIABLE ```<ret-var>```]
)


The options are:

cmd arg1 ... argN
The module sub-command and arguments to execute as if they were
passed directly to the module command in your shell environment.
OUTPUT_VARIABLE ```<out-var>```
The standard output from executing the module command.
RESULT_VARIABLE ```<ret-var>```
The return code from executing the module command.




env_module_swap
Swap one module for another:
env_module_swap(out_mod in_mod
  [OUTPUT_VARIABLE ```<out-var>```]
  [RESULT_VARIABLE ```<ret-var>```]
)


This is functionally equivalent to the module swap out_mod in_mod shell
command.  The options are:

OUTPUT_VARIABLE ```<out-var>```
The standard output from executing the module command.
RESULT_VARIABLE ```<ret-var>```
The return code from executing the module command.




env_module_list
Retrieve the list of currently loaded modules:
env_module_list(```<out-var>```)


This is functionally equivalent to the module list shell command.
The result is stored in ```<out-var>``` as a properly formatted CMake
semicolon-separated list variable.



env_module_avail
Retrieve the list of available modules:
env_module_avail([```<mod-prefix>```] ```<out-var>```)


This is functionally equivalent to the module avail ```<mod-prefix>``` shell
command.  The result is stored in ```<out-var>``` as a properly formatted
CMake semicolon-separated list variable.

  

