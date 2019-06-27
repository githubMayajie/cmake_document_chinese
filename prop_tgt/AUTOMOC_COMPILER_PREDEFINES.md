  

# AUTOMOC_COMPILER_PREDEFINES  
Boolean value used by AUTOMOC to determine if the
compiler pre definitions file moc_predefs.h should be generated.  

CMake generates a moc_predefs.h file with compiler pre definitions
from the output of the command defined in
CMAKE_CXX_COMPILER_PREDEFINES_COMMAND
when  


AUTOMOC is enabled,
AUTOMOC_COMPILER_PREDEFINES is enabled,
CMAKE_CXX_COMPILER_PREDEFINES_COMMAND isn¡¯t empty and
the Qt version is greater or equal 5.8.
  

The moc_predefs.h file, which is generated in AUTOGEN_BUILD_DIR,
is passed to moc as the argument to the --include option.  

By default AUTOMOC_COMPILER_PREDEFINES is initialized from
CMAKE_AUTOMOC_COMPILER_PREDEFINES, which is ON by default.  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  

