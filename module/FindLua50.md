  

# FindLua50  
Locate Lua library.
This module defines:  

::

  


LUA50_FOUND, if false, do not try to link to Lua
LUA_LIBRARIES, both lua and lualib
LUA_INCLUDE_DIR, where to find lua.h and lualib.h (and probably lauxlib.h)  

Note that the expected include convention is  

#include "lua.h"

  

and not  

#include ```<lua/lua.h>```

  

This is because, the lua location is not standardized and may exist in
locations other than lua/  

