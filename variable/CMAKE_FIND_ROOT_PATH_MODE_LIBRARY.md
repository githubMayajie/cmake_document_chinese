  

# CMAKE_FIND_ROOT_PATH_MODE_LIBRARY  
This variable controls whether the CMAKE_FIND_ROOT_PATH and
CMAKE_SYSROOT are used by find_library().  

If set to ONLY, then only the roots in CMAKE_FIND_ROOT_PATH
will be searched. If set to NEVER, then the roots in
CMAKE_FIND_ROOT_PATH will be ignored and only the host system
root will be used. If set to BOTH, then the host system paths and the
paths in CMAKE_FIND_ROOT_PATH will be searched.  

