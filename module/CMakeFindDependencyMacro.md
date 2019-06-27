  

# CMakeFindDependencyMacro  


find_dependency
The find_dependency() macro wraps a find_package() call for
a package dependency:
find_dependency(```<dep>``` [...])


It is designed to be used in a
Package Configuration File
(```<PackageName>```Config.cmake).  find_dependency forwards the correct
parameters for QUIET and REQUIRED which were passed to
the original find_package() call.  Any additional arguments
specified are forwarded to find_package().
If the dependency could not be found it sets an informative diagnostic
message and calls return() to end processing of the calling
package configuration file and return to the find_package()
command that loaded it.

Note
The call to return() makes this macro unsuitable to call
from Find Modules.

  

