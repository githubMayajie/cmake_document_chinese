  

# INTERFACE_LINK_LIBRARIES  
List public interface libraries for a library.  

This property contains the list of transitive link dependencies.  When
the target is linked into another target using the
target_link_libraries() command, the libraries listed (and
recursively their link interface libraries) will be provided to the
other target also.  This property is overridden by the
LINK_INTERFACE_LIBRARIES or
LINK_INTERFACE_LIBRARIES_```<CONFIG>``` property if policy
CMP0022 is OLD or unset.  

Contents of INTERFACE_LINK_LIBRARIES may use ¡°generator expressions¡±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  


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
  


Creating Relocatable Packages
Note that it is not advisable to populate the
INTERFACE_LINK_LIBRARIES of a target with absolute paths to dependencies.
That would hard-code into installed packages the library file paths
for dependencies as found on the machine the package was made on.
See the Creating Relocatable Packages section of the
cmake-packages(7) manual for discussion of additional care
that must be taken when specifying usage requirements while creating
packages for redistribution.
  

