  

# FindOpenSceneGraph  
Find OpenSceneGraph (3D graphics application programming interface)  

This module searches for the OpenSceneGraph core ¡°osg¡± library as well
as FindOpenThreads, and whatever additional COMPONENTS
(nodekits) that you specify.  

See http://www.openscenegraph.org

  

NOTE: To use this module effectively you must either require CMake >```=
2.6.3 with  cmake_minimum_required(VERSION 2.6.3) or download
and place FindOpenThreads, Findosg functions,
Findosg and Find```<etc>```.cmake files into your
CMAKE_MODULE_PATH.  

  

This module accepts the following variables (note mixed case)  

OpenSceneGraph_DEBUG - Enable debugging output

  

OpenSceneGraph_MARK_AS_ADVANCED - Mark cache variables as advanced
                                  automatically

  

The following environment variables are also respected for finding the
OSG and it¡¯s various components.  CMAKE_PREFIX_PATH can also be
used for this (see find_library() CMake documentation).  


```<MODULE>```_DIR
(where MODULE is of the form ¡°OSGVOLUME¡± and there is
a FindosgVolume.cmake` file)
OSG_DIR

OSGDIR

OSG_ROOT

  

[CMake 2.8.10]: The CMake variable OSG_DIR can now be used as well to
influence detection, instead of needing to specify an environment
variable.  

This module defines the following output variables:  

OPENSCENEGRAPH_FOUND - Was the OSG and all of the specified components found?

  

OPENSCENEGRAPH_VERSION - The version of the OSG which was found

  

OPENSCENEGRAPH_INCLUDE_DIRS - Where to find the headers

  

OPENSCENEGRAPH_LIBRARIES - The OSG libraries

  

================================== Example Usage:  

find_package(OpenSceneGraph 2.0.0 REQUIRED osgDB osgUtil)
    # libOpenThreads & libosg automatically searched
include_directories(${OPENSCENEGRAPH_INCLUDE_DIRS})

  

add_executable(foo foo.cc)
target_link_libraries(foo ${OPENSCENEGRAPH_LIBRARIES})

  

