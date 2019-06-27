  

# CheckFortranSourceRuns  
Check if given Fortran source compiles and links into an executable and can
subsequently be run.  



check_fortran_source_runs
check_fortran_source_runs(```<code>``` ```<resultVar>```
    [SRC_EXT ```<extension>```])


Check that the source supplied in ```<code>``` can be compiled as a Fortran source
file, linked as an executable and then run. The ```<code>``` must be a Fortran program
containing at least an end statement�Cfor example:
check_fortran_source_runs("real :: x[*]; call co_sum(x); end" F2018coarrayOK)


This command can help avoid costly build processes when a compiler lacks support
for a necessary feature, or a particular vendor library is not compatible with
the Fortran compiler version being used. Some of these failures only occur at runtime
instead of linktime, and a trivial runtime example can catch the issue before the
main build process.
If the ```<code>``` could be built and run
successfully, the internal cache variable specified by ```<resultVar>``` will
be set to 1, otherwise it will be set to an value that evaluates to boolean
false (e.g. an empty string or an error message).
By default, the test source file will be given a .F90 file extension. The
SRC_EXT option can be used to override this with .```<extension>``` instead.
The underlying check is performed by the try_run() command. The
compile and link commands can be influenced by setting any of the following
variables prior to calling check_fortran_source_runs():

CMAKE_REQUIRED_FLAGS
Additional flags to pass to the compiler. Note that the contents of
CMAKE_Fortran_FLAGS and its associated
configuration-specific variable are automatically added to the compiler
command before the contents of CMAKE_REQUIRED_FLAGS.
CMAKE_REQUIRED_DEFINITIONS
A ;-list of compiler definitions of the form
-DFOO or -DFOO=bar. A definition for the name specified by
```<resultVar>``` will also be added automatically.
CMAKE_REQUIRED_INCLUDES
A ;-list of header search paths to pass to
the compiler. These will be the only header search paths used by
try_run(), i.e. the contents of the INCLUDE_DIRECTORIES
directory property will be ignored.
CMAKE_REQUIRED_LINK_OPTIONS
A ;-list of options to add to the link
command (see try_run() for further details).
CMAKE_REQUIRED_LIBRARIES
A ;-list of libraries to add to the link
command. These can be the name of system libraries or they can be
Imported Targets (see try_run() for
further details).
CMAKE_REQUIRED_QUIET
If this variable evaluates to a boolean true value, all status messages
associated with the check will be suppressed.

The check is only performed once, with the result cached in the variable
named by ```<resultVar>```. Every subsequent CMake run will re-use this cached
value rather than performing the check again, even if the ```<code>``` changes.
In order to force the check to be re-evaluated, the variable named by
```<resultVar>``` must be manually removed from the cache.
  

