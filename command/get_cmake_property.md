  

# get_cmake_property  
Get a global property of the CMake instance.  

get_cmake_property(```<var>``` ```<property>```)

  

Gets a global property from the CMake instance.  The value of
the ```<property>``` is stored in the variable ```<var>```.
If the property is not found, ```<var>``` will be set to NOTFOUND.
See the cmake-properties(7) manual for available properties.  

See also the get_property() command GLOBAL option.  

In addition to global properties, this command (for historical reasons)
also supports the VARIABLES and MACROS directory
properties.  It also supports a special COMPONENTS global property that
lists the components given to the install() command.  

