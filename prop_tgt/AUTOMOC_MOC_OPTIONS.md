  

# AUTOMOC_MOC_OPTIONS  
Additional options for moc when using AUTOMOC  

This property is only used if the AUTOMOC property is ON
for this target.  In this case, it holds additional command line
options which will be used when moc is executed during the build, i.e.
it is equivalent to the optional OPTIONS argument of the
qt4_wrap_cpp() macro.  

By default it is empty.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  

