  

# CMakeAddFortranSubdirectory  
Add a fortran-only subdirectory, find a fortran compiler, and build.  

The cmake_add_fortran_subdirectory function adds a subdirectory
to a project that contains a fortran-only subproject.  The module will
check the current compiler and see if it can support fortran.  If no
fortran compiler is found and the compiler is MSVC, then this module
will find the MinGW gfortran.  It will then use an external project to
build with the MinGW tools.  It will also create imported targets for
the libraries created.  This will only work if the fortran code is
built into a dll, so BUILD_SHARED_LIBS is turned on in
the project.  In addition the CMAKE_GNUtoMS option is set
to on, so that Microsoft .lib files are created.  Usage is as follows:  

cmake_add_fortran_subdirectory(
 ```<subdir>```                # name of subdirectory
 PROJECT ```<project_name>```  # project name in subdir top CMakeLists.txt
 ARCHIVE_DIR ```<dir>```       # dir where project places .lib files
 RUNTIME_DIR ```<dir>```       # dir where project places .dll files
 LIBRARIES ```<lib>```...      # names of library targets to import
 LINK_LIBRARIES          # link interface libraries for LIBRARIES
  [LINK_LIBS ```<lib>``` ```<dep>```...]...
 CMAKE_COMMAND_LINE ...  # extra command line flags to pass to cmake
 NO_EXTERNAL_INSTALL     # skip installation of external project
 )

  

Relative paths in ARCHIVE_DIR and RUNTIME_DIR are interpreted with
respect to the build directory corresponding to the source directory
in which the function is invoked.  

Limitations:  

NO_EXTERNAL_INSTALL is required for forward compatibility with a
future version that supports installation of the external project
binaries during make install.  

