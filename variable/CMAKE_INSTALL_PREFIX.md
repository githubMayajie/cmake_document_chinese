  

# CMAKE_INSTALL_PREFIX  
Install directory used by install().  

If make install is invoked or INSTALL is built, this directory is
prepended onto all install directories.  This variable defaults to
/usr/local on UNIX and c:/Program Files/${PROJECT_NAME} on Windows.
See CMAKE_INSTALL_PREFIX_INITIALIZED_TO_DEFAULT for how a
project might choose its own default.  

On UNIX one can use the DESTDIR mechanism in order to relocate the
whole installation. See DESTDIR for more information.  

The installation prefix is also added to CMAKE_SYSTEM_PREFIX_PATH
so that find_package(), find_program(),
find_library(), find_path(), and find_file()
will search the prefix for other software.  


Note
Use the GNUInstallDirs module to provide GNU-style
options for the layout of directories within the installation.
  

