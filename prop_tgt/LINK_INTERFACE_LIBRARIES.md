  

# LINK_INTERFACE_LIBRARIES  
List public interface libraries for a shared library or executable.  

By default linking to a shared library target transitively links to
targets with which the library itself was linked.  For an executable
with exports (see the ENABLE_EXPORTS target property) no
default transitive link dependencies are used.  This property replaces the default
transitive link dependencies with an explicit list.  When the target
is linked into another target using the target_link_libraries()
command, the libraries listed (and recursively
their link interface libraries) will be provided to the other target
also.  If the list is empty then no transitive link dependencies will
be incorporated when this target is linked into another target even if
the default set is non-empty.  This property is initialized by the
value of the CMAKE_LINK_INTERFACE_LIBRARIES variable if it is
set when a target is created.  This property is ignored for STATIC
libraries.  

This property is overridden by the INTERFACE_LINK_LIBRARIES
property if policy CMP0022 is NEW.  

This property is deprecated.  Use INTERFACE_LINK_LIBRARIES
instead.  


Creating Relocatable Packages
Note that it is not advisable to populate the
LINK_INTERFACE_LIBRARIES of a target with absolute paths to dependencies.
That would hard-code into installed packages the library file paths
for dependencies as found on the machine the package was made on.
See the Creating Relocatable Packages section of the
cmake-packages(7) manual for discussion of additional care
that must be taken when specifying usage requirements while creating
packages for redistribution.
  

