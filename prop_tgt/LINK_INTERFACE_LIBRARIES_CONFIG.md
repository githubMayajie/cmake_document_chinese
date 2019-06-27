  

# LINK_INTERFACE_LIBRARIES_```<CONFIG>```  
Per-configuration list of public interface libraries for a target.  

This is the configuration-specific version of
LINK_INTERFACE_LIBRARIES.  If set, this property completely
overrides the generic property for the named configuration.  

This property is overridden by the INTERFACE_LINK_LIBRARIES
property if policy CMP0022 is NEW.  

This property is deprecated.  Use INTERFACE_LINK_LIBRARIES
instead.  


Creating Relocatable Packages
Note that it is not advisable to populate the
LINK_INTERFACE_LIBRARIES_```<CONFIG>``` of a target with absolute paths to dependencies.
That would hard-code into installed packages the library file paths
for dependencies as found on the machine the package was made on.
See the Creating Relocatable Packages section of the
cmake-packages(7) manual for discussion of additional care
that must be taken when specifying usage requirements while creating
packages for redistribution.
  

