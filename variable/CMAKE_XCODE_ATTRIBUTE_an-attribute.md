  

# CMAKE_XCODE_ATTRIBUTE_```<an-attribute>```  
Set Xcode target attributes directly.  

Tell the Xcode generator to set ¡®```<an-attribute>```¡¯ to a given value
in the generated Xcode project.  Ignored on other generators.  

See the XCODE_ATTRIBUTE_```<an-attribute>``` target property
to set attributes on a specific target.  

Contents of CMAKE_XCODE_ATTRIBUTE_```<an-attribute>``` may use
¡°generator expressions¡± with the syntax $```<...>```.  See the
cmake-generator-expressions(7) manual for available
expressions.  See the cmake-buildsystem(7) manual
for more on defining buildsystem properties.  

