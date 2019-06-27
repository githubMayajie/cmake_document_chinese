  

# FindIce  
Find the ZeroC Internet Communication Engine (ICE) programs,
libraries and datafiles.  

This module supports multiple components.
Components can include any of: Freeze, Glacier2, Ice,
IceBox, IceDB, IceDiscovery, IceGrid,
IceLocatorDiscovery, IcePatch, IceSSL, IceStorm,
IceUtil, IceXML, or Slice.  

Ice 3.7 and later also include C++11-specific components:
Glacier2++11, Ice++11, IceBox++11, IceDiscovery++11
IceGrid, IceLocatorDiscovery++11, IceSSL++11,
IceStorm++11  

Note that the set of supported components is Ice version-specific.  

This module reports information about the Ice installation in
several variables.  General variables:  

Ice_VERSION - Ice release version
Ice_FOUND - true if the main programs and libraries were found
Ice_LIBRARIES - component libraries to be linked
Ice_INCLUDE_DIRS - the directories containing the Ice headers
Ice_SLICE_DIRS - the directories containing the Ice slice interface
                 definitions

  

Imported targets:  

Ice::```<C>```

  

Where ```<C>``` is the name of an Ice component, for example
Ice::Glacier2 or Ice++11.  

Ice slice programs are reported in:  

Ice_SLICE2CONFLUENCE_EXECUTABLE - path to slice2confluence executable
Ice_SLICE2CPP_EXECUTABLE - path to slice2cpp executable
Ice_SLICE2CS_EXECUTABLE - path to slice2cs executable
Ice_SLICE2FREEZEJ_EXECUTABLE - path to slice2freezej executable
Ice_SLICE2FREEZE_EXECUTABLE - path to slice2freeze executable
Ice_SLICE2HTML_EXECUTABLE - path to slice2html executable
Ice_SLICE2JAVA_EXECUTABLE - path to slice2java executable
Ice_SLICE2JS_EXECUTABLE - path to slice2js executable
Ice_SLICE2MATLAB_EXECUTABLE - path to slice2matlab executable
Ice_SLICE2OBJC_EXECUTABLE - path to slice2objc executable
Ice_SLICE2PHP_EXECUTABLE - path to slice2php executable
Ice_SLICE2PY_EXECUTABLE - path to slice2py executable
Ice_SLICE2RB_EXECUTABLE - path to slice2rb executable

  

Ice programs are reported in:  

Ice_GLACIER2ROUTER_EXECUTABLE - path to glacier2router executable
Ice_ICEBOX_EXECUTABLE - path to icebox executable
Ice_ICEBOXXX11_EXECUTABLE - path to icebox++11 executable
Ice_ICEBOXADMIN_EXECUTABLE - path to iceboxadmin executable
Ice_ICEBOXD_EXECUTABLE - path to iceboxd executable
Ice_ICEBOXNET_EXECUTABLE - path to iceboxnet executable
Ice_ICEBRIDGE_EXECUTABLE - path to icebridge executable
Ice_ICEGRIDADMIN_EXECUTABLE - path to icegridadmin executable
Ice_ICEGRIDDB_EXECUTABLE - path to icegriddb executable
Ice_ICEGRIDNODE_EXECUTABLE - path to icegridnode executable
Ice_ICEGRIDNODED_EXECUTABLE - path to icegridnoded executable
Ice_ICEGRIDREGISTRY_EXECUTABLE - path to icegridregistry executable
Ice_ICEGRIDREGISTRYD_EXECUTABLE - path to icegridregistryd executable
Ice_ICEPATCH2CALC_EXECUTABLE - path to icepatch2calc executable
Ice_ICEPATCH2CLIENT_EXECUTABLE - path to icepatch2client executable
Ice_ICEPATCH2SERVER_EXECUTABLE - path to icepatch2server executable
Ice_ICESERVICEINSTALL_EXECUTABLE - path to iceserviceinstall executable
Ice_ICESTORMADMIN_EXECUTABLE - path to icestormadmin executable
Ice_ICESTORMDB_EXECUTABLE - path to icestormdb executable
Ice_ICESTORMMIGRATE_EXECUTABLE - path to icestormmigrate executable

  

Ice db programs (Windows only; standard system versions on all other
platforms) are reported in:  

Ice_DB_ARCHIVE_EXECUTABLE - path to db_archive executable
Ice_DB_CHECKPOINT_EXECUTABLE - path to db_checkpoint executable
Ice_DB_DEADLOCK_EXECUTABLE - path to db_deadlock executable
Ice_DB_DUMP_EXECUTABLE - path to db_dump executable
Ice_DB_HOTBACKUP_EXECUTABLE - path to db_hotbackup executable
Ice_DB_LOAD_EXECUTABLE - path to db_load executable
Ice_DB_LOG_VERIFY_EXECUTABLE - path to db_log_verify executable
Ice_DB_PRINTLOG_EXECUTABLE - path to db_printlog executable
Ice_DB_RECOVER_EXECUTABLE - path to db_recover executable
Ice_DB_STAT_EXECUTABLE - path to db_stat executable
Ice_DB_TUNER_EXECUTABLE - path to db_tuner executable
Ice_DB_UPGRADE_EXECUTABLE - path to db_upgrade executable
Ice_DB_VERIFY_EXECUTABLE - path to db_verify executable
Ice_DUMPDB_EXECUTABLE - path to dumpdb executable
Ice_TRANSFORMDB_EXECUTABLE - path to transformdb executable

  

Ice component libraries are reported in:  

Ice_```<C>```_FOUND - ON if component was found
Ice_```<C>```_LIBRARIES - libraries for component

  

Note that ```<C>``` is the uppercased name of the component.  

This module reads hints about search results from:  

Ice_HOME - the root of the Ice installation

  

The environment variable ICE_HOME may also be used; the
Ice_HOME variable takes precedence.  


Note
On Windows, Ice 3.7.0 and later provide libraries via the NuGet
package manager.  Appropriate NuGet packages will be searched for
using CMAKE_PREFIX_PATH, or alternatively Ice_HOME may be
set to the location of a specific NuGet package to restrict the
search.
  

The following cache variables may also be set:  

Ice_```<P>```_EXECUTABLE - the path to executable ```<P>```
Ice_INCLUDE_DIR - the directory containing the Ice headers
Ice_SLICE_DIR - the directory containing the Ice slice interface
                definitions
Ice_```<C>```_LIBRARY - the library for component ```<C>```

  


Note
In most cases none of the above variables will require setting,
unless multiple Ice versions are available and a specific version
is required.  On Windows, the most recent version of Ice will be
found through the registry.  On Unix, the programs, headers and
libraries will usually be in standard locations, but Ice_SLICE_DIRS
might not be automatically detected (commonly known locations are
searched).  All the other variables are defaulted using Ice_HOME,
if set.  It¡¯s possible to set Ice_HOME and selectively specify
alternative locations for the other components; this might be
required for e.g. newer versions of Visual Studio if the
heuristics are not sufficient to identify the correct programs and
libraries for the specific Visual Studio version.
  

Other variables one may set to control this module are:  

Ice_DEBUG - Set to ON to enable debug output from FindIce.

  

