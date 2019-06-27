  

# FindPythonInterp  

Deprecated since version 3.12: Use FindPython3, FindPython2 or FindPython instead.
  

Find python interpreter  

This module finds if Python interpreter is installed and determines
where the executables are.  This code sets the following variables:  

PYTHONINTERP_FOUND         - Was the Python executable found
PYTHON_EXECUTABLE          - path to the Python interpreter

  

PYTHON_VERSION_STRING      - Python version found e.g. 2.5.2
PYTHON_VERSION_MAJOR       - Python major version found e.g. 2
PYTHON_VERSION_MINOR       - Python minor version found e.g. 5
PYTHON_VERSION_PATCH       - Python patch version found e.g. 2

  

The Python_ADDITIONAL_VERSIONS variable can be used to specify a list
of version numbers that should be taken into account when searching
for Python.  You need to set this variable before calling
find_package(PythonInterp).  

If calling both find_package(PythonInterp) and
find_package(PythonLibs), call find_package(PythonInterp) first to
get the currently active Python version by default with a consistent version
of PYTHON_LIBRARIES.  

