  

# JOB_POOLS  
Ninja only: List of available pools.  

A pool is a named integer property and defines the maximum number
of concurrent jobs which can be started by a rule assigned to the pool.
The JOB_POOLS property is a semicolon-separated list of
pairs using the syntax NAME=integer (without a space after the equality sign).  

For instance:  

set_property(GLOBAL PROPERTY JOB_POOLS two_jobs=2 ten_jobs=10)

  

Defined pools could be used globally by setting
CMAKE_JOB_POOL_COMPILE and CMAKE_JOB_POOL_LINK
or per target by setting the target properties
JOB_POOL_COMPILE and JOB_POOL_LINK.
Custom commands and
custom targets can specify pools using the
option JOB_POOL.
Using a pool that is not defined by JOB_POOLS causes
an error by ninja at build time.  

If not set, this property uses the value of the CMAKE_JOB_POOLS
variable.  

Build targets provided by CMake that are meant for individual interactive
use, such as install, are placed in the console pool automatically.  

