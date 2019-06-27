  

# SUBDIRECTORIES  
This read-only directory property contains a
semicolon-separated list of subdirectories processed so far by
the add_subdirectory() or subdirs() commands.  Each entry is
the absolute path to the source directory (containing the CMakeLists.txt
file).  This is suitable to pass to the get_property() command
DIRECTORY option.  


Note
The subdirs() command does not process its arguments until
after the calling directory is fully processed.  Therefore looking
up this property in the current directory will not see them.
  

