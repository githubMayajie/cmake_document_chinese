  

# CMAKE_GLOBAL_AUTORCC_TARGET  
Switch to enable generation of a global autorcc target.  

When CMAKE_GLOBAL_AUTORCC_TARGET is enabled, a custom target
autorcc is generated. This target depends on all AUTORCC
generated ```<ORIGIN>```_arcc_```<QRC>``` targets in the project.
By building the global autorcc target, all AUTORCC
files in the project will be generated.  

The name of the global autorcc target can be changed by setting
CMAKE_GLOBAL_AUTORCC_TARGET_NAME.  

By default CMAKE_GLOBAL_AUTORCC_TARGET is unset.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  

