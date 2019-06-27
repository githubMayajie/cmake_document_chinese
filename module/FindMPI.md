  

# FindMPI  
Find a Message Passing Interface (MPI) implementation.  

The Message Passing Interface (MPI) is a library used to write
high-performance distributed-memory parallel applications, and is
typically deployed on a cluster.  MPI is a standard interface (defined
by the MPI forum) for which many implementations are available.  


Variables for using MPI
The module exposes the components C, CXX, MPICXX and Fortran.
Each of these controls the various MPI languages to search for.
The difference between CXX and MPICXX is that CXX refers to the
MPI C API being usable from C++, whereas MPICXX refers to the MPI-2 C++ API
that was removed again in MPI-3.
Depending on the enabled components the following variables will be set:

MPI_FOUND
Variable indicating that MPI settings for all requested languages have been found.
If no components are specified, this is true if MPI settings for all enabled languages
were detected. Note that the MPICXX component does not affect this variable.
MPI_VERSION
Minimal version of MPI detected among the requested languages, or all enabled languages
if no components were specified.

This module will set the following variables per language in your
project, where ```<lang>``` is one of C, CXX, or Fortran:

MPI_```<lang>```_FOUND
Variable indicating the MPI settings for ```<lang>``` were found and that
simple MPI test programs compile with the provided settings.
MPI_```<lang>```_COMPILER
MPI compiler for ```<lang>``` if such a program exists.
MPI_```<lang>```_COMPILE_OPTIONS
Compilation options for MPI programs in ```<lang>```, given as a ;-list.
MPI_```<lang>```_COMPILE_DEFINITIONS
Compilation definitions for MPI programs in ```<lang>```, given as a ;-list.
MPI_```<lang>```_INCLUDE_DIRS
Include path(s) for MPI header.
MPI_```<lang>```_LINK_FLAGS
Linker flags for MPI programs.
MPI_```<lang>```_LIBRARIES
All libraries to link MPI programs against.

Additionally, the following IMPORTED targets are defined:

MPI::MPI_```<lang>```
Target for using MPI from ```<lang>```.

The following variables indicating which bindings are present will be defined:

MPI_MPICXX_FOUND
Variable indicating whether the MPI-2 C++ bindings are present (introduced in MPI-2, removed with MPI-3).
MPI_Fortran_HAVE_F77_HEADER
True if the Fortran 77 header mpif.h is available.
MPI_Fortran_HAVE_F90_MODULE
True if the Fortran 90 module mpi can be used for accessing MPI (MPI-2 and higher only).
MPI_Fortran_HAVE_F08_MODULE
True if the Fortran 2008 mpi_f08 is available to MPI programs (MPI-3 and higher only).

If possible, the MPI version will be determined by this module. The facilities to detect the MPI version
were introduced with MPI-1.2, and therefore cannot be found for older MPI versions.

MPI_```<lang>```_VERSION_MAJOR
Major version of MPI implemented for ```<lang>``` by the MPI distribution.
MPI_```<lang>```_VERSION_MINOR
Minor version of MPI implemented for ```<lang>``` by the MPI distribution.
MPI_```<lang>```_VERSION
MPI version implemented for ```<lang>``` by the MPI distribution.

Note that there¡¯s no variable for the C bindings being accessible through mpi.h, since the MPI standards
always have required this binding to work in both C and C++ code.
For running MPI programs, the module sets the following variables

MPIEXEC_EXECUTABLE
Executable for running MPI programs, if such exists.
MPIEXEC_NUMPROC_FLAG
Flag to pass to mpiexec before giving it the number of processors to run on.
MPIEXEC_MAX_NUMPROCS
Number of MPI processors to utilize. Defaults to the number
of processors detected on the host system.
MPIEXEC_PREFLAGS
Flags to pass to mpiexec directly before the executable to run.
MPIEXEC_POSTFLAGS
Flags to pass to mpiexec after other flags.

  


Variables for locating MPI
This module performs a three step search for an MPI implementation:

Check if the compiler has MPI support built-in. This is the case if the user passed a
compiler wrapper as CMAKE_```<LANG>```_COMPILER or if they¡¯re on a Cray system.
Attempt to find an MPI compiler wrapper and determine the compiler information from it.
Try to find an MPI implementation that does not ship such a wrapper by guessing settings.
Currently, only Microsoft MPI and MPICH2 on Windows are supported.

For controlling the second step, the following variables may be set:

MPI_```<lang>```_COMPILER
Search for the specified compiler wrapper and use it.
MPI_```<lang>```_COMPILER_FLAGS
Flags to pass to the MPI compiler wrapper during interrogation. Some compiler wrappers
support linking debug or tracing libraries if a specific flag is passed and this variable
may be used to obtain them.
MPI_COMPILER_FLAGS
Used to initialize MPI_```<lang>```_COMPILER_FLAGS if no language specific flag has been given.
Empty by default.
MPI_EXECUTABLE_SUFFIX
A suffix which is appended to all names that are being looked for. For instance you may set this
to .mpich or .openmpi to prefer the one or the other on Debian and its derivatives.

In order to control the guessing step, the following variable may be set:

MPI_GUESS_LIBRARY_NAME
Valid values are MSMPI and MPICH2. If set, only the given library will be searched for.
By default, MSMPI will be preferred over MPICH2 if both are available.
This also sets MPI_SKIP_COMPILER_WRAPPER to true, which may be overridden.

Each of the search steps may be skipped with the following control variables:

MPI_ASSUME_NO_BUILTIN_MPI
If true, the module assumes that the compiler itself does not provide an MPI implementation and
skips to step 2.
MPI_SKIP_COMPILER_WRAPPER
If true, no compiler wrapper will be searched for.
MPI_SKIP_GUESSING
If true, the guessing step will be skipped.

Additionally, the following control variable is available to change search behavior:

MPI_CXX_SKIP_MPICXX
Add some definitions that will disable the MPI-2 C++ bindings.
Currently supported are MPICH, Open MPI, Platform MPI and derivatives thereof,
for example MVAPICH or Intel MPI.

If the find procedure fails for a variable MPI_```<lang>```_WORKS, then the settings detected by or passed to
the module did not work and even a simple MPI test program failed to compile.
If all of these parameters were not sufficient to find the right MPI implementation, a user may
disable the entire autodetection process by specifying both a list of libraries in MPI_```<lang>```_LIBRARIES
and a list of include directories in MPI_```<lang>```_ADDITIONAL_INCLUDE_DIRS.
Any other variable may be set in addition to these two. The module will then validate the MPI settings and store the
settings in the cache.
  


Cache variables for MPI
The variable MPI_```<lang>```_INCLUDE_DIRS will be assembled from the following variables.
For C and CXX:

MPI_```<lang>```_HEADER_DIR
Location of the mpi.h header on disk.

For Fortran:

MPI_Fortran_F77_HEADER_DIR
Location of the Fortran 77 header mpif.h, if it exists.
MPI_Fortran_MODULE_DIR
Location of the mpi or mpi_f08 modules, if available.

For all languages the following variables are additionally considered:

MPI_```<lang>```_ADDITIONAL_INCLUDE_DIRS
A ;-list of paths needed in addition to the normal include directories.
MPI_```<include_name>```_INCLUDE_DIR
Path variables for include folders referred to by ```<include_name>```.
MPI_```<lang>```_ADDITIONAL_INCLUDE_VARS
A ;-list of ```<include_name>``` that will be added to the include locations of ```<lang>```.

The variable MPI_```<lang>```_LIBRARIES will be assembled from the following variables:

MPI_```<lib_name>```_LIBRARY
The location of a library called ```<lib_name>``` for use with MPI.
MPI_```<lang>```_LIB_NAMES
A ;-list of ```<lib_name>``` that will be added to the include locations of ```<lang>```.

  


Usage of mpiexec
When using MPIEXEC_EXECUTABLE to execute MPI applications, you should typically
use all of the MPIEXEC_EXECUTABLE flags as follows:
${MPIEXEC_EXECUTABLE} ${MPIEXEC_NUMPROC_FLAG} ${MPIEXEC_MAX_NUMPROCS}
  ${MPIEXEC_PREFLAGS} EXECUTABLE ${MPIEXEC_POSTFLAGS} ARGS


where EXECUTABLE is the MPI program, and ARGS are the arguments to
pass to the MPI program.
  


Advanced variables for using MPI
The module can perform some advanced feature detections upon explicit request.
Important notice: The following checks cannot be performed without executing an MPI test program.
Consider the special considerations for the behavior of try_run() during cross compilation.
Moreover, running an MPI program can cause additional issues, like a firewall notification on some systems.
You should only enable these detections if you absolutely need the information.
If the following variables are set to true, the respective search will be performed:

MPI_DETERMINE_Fortran_CAPABILITIES
Determine for all available Fortran bindings what the values of MPI_SUBARRAYS_SUPPORTED and
MPI_ASYNC_PROTECTS_NONBLOCKING are and make their values available as MPI_Fortran_```<binding>```_SUBARRAYS
and MPI_Fortran_```<binding>```_ASYNCPROT, where ```<binding>``` is one of F77_HEADER, F90_MODULE and
F08_MODULE.
MPI_DETERMINE_LIBRARY_VERSION
For each language, find the output of MPI_Get_library_version and make it available as MPI_```<lang>```_LIBRARY_VERSION_STRING.
This information is usually tied to the runtime component of an MPI implementation and might differ depending on ```<lang>```.
Note that the return value is entirely implementation defined. This information might be used to identify
the MPI vendor and for example pick the correct one of multiple third party binaries that matches the MPI vendor.

  


Backward Compatibility
For backward compatibility with older versions of FindMPI, these
variables are set, but deprecated:
MPI_COMPILER        MPI_LIBRARY        MPI_EXTRA_LIBRARY
MPI_COMPILE_FLAGS   MPI_INCLUDE_PATH   MPI_LINK_FLAGS
MPI_LIBRARIES


In new projects, please use the MPI_```<lang>```_XXX equivalents.
Additionally, the following variables are deprecated:

MPI_```<lang>```_COMPILE_FLAGS
Use MPI_```<lang>```_COMPILE_OPTIONS and MPI_```<lang>```_COMPILE_DEFINITIONS instead.
MPI_```<lang>```_INCLUDE_PATH
For consumption use MPI_```<lang>```_INCLUDE_DIRS and for specifying folders use MPI_```<lang>```_ADDITIONAL_INCLUDE_DIRS instead.
MPIEXEC
Use MPIEXEC_EXECUTABLE instead.

  

