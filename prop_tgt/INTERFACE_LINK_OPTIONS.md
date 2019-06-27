  

# INTERFACE_LINK_OPTIONS  
List of public link options requirements for a library.  

Targets may populate this property to publish the link options
required to compile against the headers for the target.  The target_link_options()
command populates this property with values given to the PUBLIC and
INTERFACE keywords.  Projects may also get and set the property directly.  

When target dependencies are specified using target_link_libraries(),
CMake will read this property from all target dependencies to determine the
build properties of the consumer.  

Contents of INTERFACE_LINK_OPTIONS may use ��generator expressions��
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
-manual for more on defining buildsystem properties.  
