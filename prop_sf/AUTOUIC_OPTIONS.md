  

# AUTOUIC_OPTIONS  
Additional options for uic when using AUTOUIC  

This property holds additional command line options which will be used when
uic is executed during the build via AUTOUIC, i.e. it is
equivalent to the optional OPTIONS argument of the
qt4_wrap_ui() macro.  

By default it is empty.  

This property is initialized by the value of the
CMAKE_AUTOUIC_OPTIONS variable if it is set when a target is
created.  

The options set on the target may be overridden by AUTOUIC_OPTIONS
set on the .ui source file.  

This property may use ¡°generator expressions¡± with the syntax $```<...>```.
See the cmake-generator-expressions(7) manual for available
expressions.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  


EXAMPLE
# ...
set_property(TARGET tgt PROPERTY AUTOUIC_OPTIONS "--no-protection")
# ...


  

