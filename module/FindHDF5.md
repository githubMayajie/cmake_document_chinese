  

# FindHDF5  
Find Hierarchical Data Format (HDF5), a library for reading and writing
self describing array data.  

This module invokes the HDF5 wrapper compiler that should be installed
alongside HDF5.  Depending upon the HDF5 Configuration, the wrapper
compiler is called either h5cc or h5pcc.  If this succeeds, the module
will then call the compiler with the show argument to see what flags
are used when compiling an HDF5 client application.  

The module will optionally accept the COMPONENTS argument.  If no
COMPONENTS are specified, then the find module will default to finding
only the HDF5 C library.  If one or more COMPONENTS are specified, the
module will attempt to find the language bindings for the specified
components.  The only valid components are C, CXX, Fortran, HL,
and Fortran_HL.  If the COMPONENTS argument is not given, the module will
attempt to find only the C bindings.  

This module will read the variable
HDF5_USE_STATIC_LIBRARIES to determine whether or not to prefer a
static link to a dynamic link for HDF5 and all of it¡¯s dependencies.
To use this feature, make sure that the HDF5_USE_STATIC_LIBRARIES
variable is set before the call to find_package.  

To provide the module with a hint about where to find your HDF5
installation, you can set the environment variable HDF5_ROOT.  The
Find module will then look in this path when searching for HDF5
executables, paths, and libraries.  

Both the serial and parallel HDF5 wrappers are considered and the first
directory to contain either one will be used.  In the event that both appear
in the same directory the serial version is preferentially selected. This
behavior can be reversed by setting the variable HDF5_PREFER_PARALLEL to
True.  

In addition to finding the includes and libraries required to compile
an HDF5 client application, this module also makes an effort to find
tools that come with the HDF5 distribution that may be useful for
regression testing.  


Result Variables
This module will set the following variables in your project:

HDF5_FOUND
HDF5 was found on the system
HDF5_VERSION
HDF5 library version
HDF5_INCLUDE_DIRS
Location of the HDF5 header files
HDF5_DEFINITIONS
Required compiler definitions for HDF5
HDF5_LIBRARIES
Required libraries for all requested bindings
HDF5_HL_LIBRARIES
Required libraries for the HDF5 high level API for all bindings,
if the HL component is enabled

Available components are: C CXX Fortran and HL.
For each enabled language binding, a corresponding HDF5_${LANG}_LIBRARIES
variable, and potentially HDF5_${LANG}_DEFINITIONS, will be defined.
If the HL component is enabled, then an HDF5_${LANG}_HL_LIBRARIES will
also be defined.  With all components enabled, the following variables will be defined:

HDF5_C_DEFINITIONS
Required compiler definitions for HDF5 C bindings
HDF5_CXX_DEFINITIONS
Required compiler definitions for HDF5 C++ bindings
HDF5_Fortran_DEFINITIONS
Required compiler definitions for HDF5 Fortran bindings
HDF5_C_INCLUDE_DIRS
Required include directories for HDF5 C bindings
HDF5_CXX_INCLUDE_DIRS
Required include directories for HDF5 C++ bindings
HDF5_Fortran_INCLUDE_DIRS
Required include directories for HDF5 Fortran bindings
HDF5_C_LIBRARIES
Required libraries for the HDF5 C bindings
HDF5_CXX_LIBRARIES
Required libraries for the HDF5 C++ bindings
HDF5_Fortran_LIBRARIES
Required libraries for the HDF5 Fortran bindings
HDF5_C_HL_LIBRARIES
Required libraries for the high level C bindings
HDF5_CXX_HL_LIBRARIES
Required libraries for the high level C++ bindings
HDF5_Fortran_HL_LIBRARIES
Required libraries for the high level Fortran bindings.
HDF5_IS_PARALLEL
HDF5 library has parallel IO support
HDF5_C_COMPILER_EXECUTABLE
path to the HDF5 C wrapper compiler
HDF5_CXX_COMPILER_EXECUTABLE
path to the HDF5 C++ wrapper compiler
HDF5_Fortran_COMPILER_EXECUTABLE
path to the HDF5 Fortran wrapper compiler
HDF5_C_COMPILER_EXECUTABLE_NO_INTERROGATE
path to the primary C compiler which is also the HDF5 wrapper
HDF5_CXX_COMPILER_EXECUTABLE_NO_INTERROGATE
path to the primary C++ compiler which is also the HDF5 wrapper
HDF5_Fortran_COMPILER_EXECUTABLE_NO_INTERROGATE
path to the primary Fortran compiler which is also the HDF5 wrapper
HDF5_DIFF_EXECUTABLE
path to the HDF5 dataset comparison tool

  


Hints
The following variable can be set to guide the search for HDF5 libraries and includes:

HDF5_ROOT
Specify the path to the HDF5 installation to use.
HDF5_FIND_DEBUG
Set true to get extra debugging output.
HDF5_NO_FIND_PACKAGE_CONFIG_FILE
Set true to skip trying to find hdf5-config.cmake.

  

