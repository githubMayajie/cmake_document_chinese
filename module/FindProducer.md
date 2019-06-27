  

# FindProducer  
Though Producer isn¡¯t directly part of OpenSceneGraph, its primary
user is OSG so I consider this part of the Findosg* suite used to find
OpenSceneGraph components.  You¡¯ll notice that I accept OSGDIR as an
environment path.  

Each component is separate and you must opt in to each module.  You
must also opt into OpenGL (and OpenThreads?) as these modules won¡¯t do
it for you.  This is to allow you control over your own system piece
by piece in case you need to opt out of certain components or change
the Find behavior for a particular module (perhaps because the default
FindOpenGL.cmake module doesn¡¯t work with your system as an example).
If you want to use a more convenient module that includes everything,
use the FindOpenSceneGraph.cmake instead of the Findosg*.cmake
modules.  

Locate Producer This module defines PRODUCER_LIBRARY PRODUCER_FOUND,
if false, do not try to link to Producer PRODUCER_INCLUDE_DIR, where
to find the headers  

$PRODUCER_DIR is an environment variable that would correspond to the
./configure ¨Cprefix=$PRODUCER_DIR used in building osg.  

Created by Eric Wing.  

