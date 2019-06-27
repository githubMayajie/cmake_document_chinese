  

# FindArmadillo  
Find the Armadillo C++ library.
Armadillo is library for linear algebra & scientific computing.  

Using Armadillo:  

find_package(Armadillo REQUIRED)
include_directories(${ARMADILLO_INCLUDE_DIRS})
add_executable(foo foo.cc)
target_link_libraries(foo ${ARMADILLO_LIBRARIES})

  

This module sets the following variables:  

ARMADILLO_FOUND - set to true if the library is found
ARMADILLO_INCLUDE_DIRS - list of required include directories
ARMADILLO_LIBRARIES - list of libraries to be linked
ARMADILLO_VERSION_MAJOR - major version number
ARMADILLO_VERSION_MINOR - minor version number
ARMADILLO_VERSION_PATCH - patch version number
ARMADILLO_VERSION_STRING - version number as a string (ex: "1.0.4")
ARMADILLO_VERSION_NAME - name of the version (ex: "Antipodean Antileech")

  

