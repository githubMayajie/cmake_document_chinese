  

# FindLua  
Locate Lua library.  

This module defines:  

::

  


LUA_FOUND          - if false, do not try to link to Lua
LUA_LIBRARIES      - both lua and lualib
LUA_INCLUDE_DIR    - where to find lua.h
LUA_VERSION_STRING - the version of Lua found
LUA_VERSION_MAJOR  - the major version of Lua
LUA_VERSION_MINOR  - the minor version of Lua
LUA_VERSION_PATCH  - the patch version of Lua  

Note that the expected include convention is  

#include "lua.h"

  

and not  

#include ```<lua/lua.h>```

  

This is because, the lua location is not standardized and may exist in
locations other than lua/  

