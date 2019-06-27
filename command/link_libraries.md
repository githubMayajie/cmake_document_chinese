  

# LINK_LIBRARIES  
List of direct link dependencies.  

This property specifies the list of libraries or targets which will be
used for linking.  In addition to accepting values from the
target_link_libraries() command, values may be set directly on
any target using the set_property() command.  

The value of this property is used by the generators to set the link
libraries for the compiler.  

Contents of LINK_LIBRARIES may use ¡°generator expressions¡± with the
syntax $```<...>```.  See the cmake-generator-expressions(7) manual
for available expressions.  See the cmake-buildsystem(7) manual
for more on defining buildsystem properties.  


Note
A call to target_link_libraries(```<target>``` ...) may update this
property on ```<target>```.  If ```<target>``` was not created in the same
directory as the call then target_link_libraries() will add a
suffix of the form ::@```<directory-id>``` to each entry, where the
::@ is a separator and the ```<directory-id>``` is unspecified.
This tells the generators that the named libraries must be looked up in
the scope of the caller rather than in the scope in which the
```<target>``` was created.  Valid directory ids are stripped on export
by the install(EXPORT) and export() commands.
  

