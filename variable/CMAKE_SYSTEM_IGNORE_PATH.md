  

# CMAKE_SYSTEM_IGNORE_PATH  
Semicolon-separated list of directories to be ignored by
the find_program(), find_library(), find_file(),
and find_path() commands.  This is useful in cross-compiling
environments where some system directories contain incompatible but
possibly linkable libraries.  For example, on cross-compiled cluster
environments, this allows a user to ignore directories containing
libraries meant for the front-end machine.  

By default this contains a list of directories containing incompatible
binaries for the host system.  See the CMAKE_IGNORE_PATH variable
that is intended to be set by the project.  

See also the CMAKE_SYSTEM_PREFIX_PATH,
CMAKE_SYSTEM_LIBRARY_PATH, CMAKE_SYSTEM_INCLUDE_PATH,
and CMAKE_SYSTEM_PROGRAM_PATH variables.  

