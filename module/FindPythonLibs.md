  

# FindPythonLibs  

Deprecated since version 3.12: Use FindPython3, FindPython2 or FindPython instead.
  

Find python libraries  

This module finds if Python is installed and determines where the
include files and libraries are.  It also determines what the name of
the library is.  This code sets the following variables:  

PYTHONLIBS_FOUND           - have the Python libs been found
PYTHON_LIBRARIES           - path to the python library
PYTHON_INCLUDE_PATH        - path to where Python.h is found (deprecated)
PYTHON_INCLUDE_DIRS        - path to where Python.h is found
PYTHON_DEBUG_LIBRARIES     - path to the debug library (deprecated)
PYTHONLIBS_VERSION_STRING  - version of the Python libs found (since CMake 2.8.8)

  

The Python_ADDITIONAL_VERSIONS variable can be used to specify a list
of version numbers that should be taken into account when searching
for Python.  You need to set this variable before calling
find_package(PythonLibs).  

If you¡¯d like to specify the installation of Python to use, you should
modify the following cache variables:  

PYTHON_LIBRARY             - path to the python library
PYTHON_INCLUDE_DIR         - path to where Python.h is found

  

If calling both find_package(PythonInterp) and
find_package(PythonLibs), call find_package(PythonInterp) first to
get the currently active Python version by default with a consistent version
of PYTHON_LIBRARIES.  

