  

# FindOpenThreads  
OpenThreads is a C++ based threading library.  Its largest userbase
seems to OpenSceneGraph so you might notice I accept OSGDIR as an
environment path.  I consider this part of the Findosg* suite used to
find OpenSceneGraph components.  Each component is separate and you
must opt in to each module.  

Locate OpenThreads This module defines OPENTHREADS_LIBRARY
OPENTHREADS_FOUND, if false, do not try to link to OpenThreads
OPENTHREADS_INCLUDE_DIR, where to find the headers  

$OPENTHREADS_DIR is an environment variable that would correspond to
the ./configure ¨Cprefix=$OPENTHREADS_DIR used in building osg.  

[CMake 2.8.10]: The CMake variables OPENTHREADS_DIR or OSG_DIR can now
be used as well to influence detection, instead of needing to specify
an environment variable.  

Created by Eric Wing.  

