  

# AUTOGEN_BUILD_DIR  
Directory where AUTOMOC, AUTOUIC and AUTORCC
generate files for the target.  

The directory is created on demand and automatically added to the
ADDITIONAL_CLEAN_FILES target property.  

When unset or empty the directory ```<dir>```/```<target-name>```_autogen is used where
```<dir>``` is CMAKE_CURRENT_BINARY_DIR and ```<target-name>```
is NAME.  

By default AUTOGEN_BUILD_DIR is unset.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  

