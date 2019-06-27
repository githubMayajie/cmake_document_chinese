  

# INTERFACE_COMPILE_FEATURES  
List of public compile features requirements for a library.  

Targets may populate this property to publish the compile features
required to compile against the headers for the target.  The target_compile_features()
command populates this property with values given to the PUBLIC and
INTERFACE keywords.  Projects may also get and set the property directly.  

When target dependencies are specified using target_link_libraries(),
CMake will read this property from all target dependencies to determine the
build properties of the consumer.  

Contents of INTERFACE_COMPILE_FEATURES may use ¡°generator expressions¡±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
-manual for more on defining buildsystem properties.  

See the cmake-compile-features(7) manual for information on compile
features and a list of supported compilers.  

