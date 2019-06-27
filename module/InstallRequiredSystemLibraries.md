  

# InstallRequiredSystemLibraries  
Include this module to search for compiler-provided system runtime
libraries and add install rules for them.  Some optional variables
may be set prior to including the module to adjust behavior:  


CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS
Specify additional runtime libraries that may not be detected.
After inclusion any detected libraries will be appended to this.
CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_SKIP
Set to TRUE to skip calling the install(PROGRAMS) command to
allow the includer to specify its own install rule, using the value of
CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS to get the list of libraries.
CMAKE_INSTALL_DEBUG_LIBRARIES
Set to TRUE to install the debug runtime libraries when available
with MSVC tools.
CMAKE_INSTALL_DEBUG_LIBRARIES_ONLY
Set to TRUE to install only the debug runtime libraries with MSVC
tools even if the release runtime libraries are also available.
CMAKE_INSTALL_UCRT_LIBRARIES
Set to TRUE to install the Windows Universal CRT libraries for
app-local deployment (e.g. to Windows XP).  This is meaningful
only with MSVC from Visual Studio 2015 or higher.
One may set a CMAKE_WINDOWS_KITS_10_DIR environment variable
to an absolute path to tell CMake to look for Windows 10 SDKs in
a custom location.  The specified directory is expected to contain
Redist/ucrt/DLLs/* directories.

CMAKE_INSTALL_MFC_LIBRARIES
Set to TRUE to install the MSVC MFC runtime libraries.
CMAKE_INSTALL_OPENMP_LIBRARIES
Set to TRUE to install the MSVC OpenMP runtime libraries
CMAKE_INSTALL_SYSTEM_RUNTIME_DESTINATION
Specify the install(PROGRAMS) command DESTINATION
option.  If not specified, the default is bin on Windows
and lib elsewhere.
CMAKE_INSTALL_SYSTEM_RUNTIME_LIBS_NO_WARNINGS
Set to TRUE to disable warnings about required library files that
do not exist.  (For example, Visual Studio Express editions may
not provide the redistributable files.)
CMAKE_INSTALL_SYSTEM_RUNTIME_COMPONENT
Specify the install(PROGRAMS) command COMPONENT
option.  If not specified, no such option will be used.
  

