  

# CMAKE_SYSTEM_PREFIX_PATH  
Semicolon-separated list of directories specifying installation
prefixes to be searched by the find_package(),
find_program(), find_library(), find_file(), and
find_path() commands.  Each command will add appropriate
subdirectories (like bin, lib, or include) as specified in its own
documentation.  

By default this contains the standard directories for the current system, the
CMAKE_INSTALL_PREFIX, and the CMAKE_STAGING_PREFIX.
The installation and staging prefixes may be excluded by setting
the CMAKE_FIND_NO_INSTALL_PREFIX variable.  

CMAKE_SYSTEM_PREFIX_PATH is not intended to be modified by the project;
use CMAKE_PREFIX_PATH for this.  

See also CMAKE_SYSTEM_INCLUDE_PATH,
CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_SYSTEM_PROGRAM_PATH,
and CMAKE_SYSTEM_IGNORE_PATH.  

