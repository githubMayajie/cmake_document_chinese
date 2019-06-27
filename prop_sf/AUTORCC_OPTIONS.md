  

# AUTORCC_OPTIONS  
Additional options for rcc when using AUTORCC  

This property holds additional command line options which will be used
when rcc is executed during the build via AUTORCC,
i.e. it is equivalent to the optional OPTIONS argument of the
qt4_add_resources() macro.  

By default it is empty.  

This property is initialized by the value of the
CMAKE_AUTORCC_OPTIONS variable if it is set when a target is
created.  

The options set on the target may be overridden by AUTORCC_OPTIONS
set on the .qrc source file.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  


EXAMPLE
# ...
set_property(TARGET tgt PROPERTY AUTORCC_OPTIONS "--compress;9")
# ...


  

