  

# FindLua51  
Locate Lua library.
This module defines:  

::

  


LUA51_FOUND, if false, do not try to link to Lua
LUA_LIBRARIES
LUA_INCLUDE_DIR, where to find lua.h
LUA_VERSION_STRING, the version of Lua found (since CMake 2.8.8)  

Note that the expected include convention is  

#include "lua.h"

  

and not  

#include ```<lua/lua.h>```

  

This is because, the lua location is not standardized and may exist in
locations other than lua/  

