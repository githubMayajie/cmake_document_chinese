  

# FindODBC  
Find an Open Database Connectivity (ODBC) include directory and library.  

On Windows, when building with Visual Studio, this module assumes the ODBC
library is provided by the available Windows SDK.  

On Unix, this module allows to search for ODBC library provided by
unixODBC or iODBC implementations of ODBC API.
This module reads hint about location of the config program:  



ODBC_CONFIG
Location of odbc_config or iodbc-config program
  

Otherwise, this module tries to find the config program,
first from unixODBC, then from iODBC.
If no config program found, this module searches for ODBC header
and library in list of known locations.  


Imported targets
This module defines the following IMPORTED targets:


ODBC::ODBC
Imported target for using the ODBC library, if found.

  


Result variables


ODBC_FOUND
Set to true if ODBC library found, otherwise false or undefined.



ODBC_INCLUDE_DIRS
Paths to include directories listed in one variable for use by ODBC client.
May be empty on Windows, where the include directory corresponding to the
expected Windows SDK is already available in the compilation environment.



ODBC_LIBRARIES
Paths to libraries to linked against to use ODBC.
May just a library name on Windows, where the library directory corresponding
to the expected Windows SDK is already available in the compilation environment.



ODBC_CONFIG
Path to unixODBC or iODBC config program, if found or specified.

  


Cache variables
For users who wish to edit and control the module behavior, this module
reads hints about search locations from the following variables:


ODBC_INCLUDE_DIR
Path to ODBC include directory with sql.h header.



ODBC_LIBRARY
Path to ODBC library to be linked.

These variables should not be used directly by project code.
  


Limitations
On Windows, this module does not search for iODBC.
On Unix, there is no way to prefer unixODBC over iODBC, or vice versa,
other than providing the config program location using the ODBC_CONFIG.
This module does not allow to search for a specific ODBC driver.
  

