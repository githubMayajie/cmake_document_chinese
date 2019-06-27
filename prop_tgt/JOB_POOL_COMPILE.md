  

# JOB_POOL_COMPILE  
Ninja only: Pool used for compiling.  

The number of parallel compile processes could be limited by defining
pools with the global JOB_POOLS
property and then specifying here the pool name.  

For instance:  

set_property(TARGET myexe PROPERTY JOB_POOL_COMPILE ten_jobs)

  

This property is initialized by the value of
CMAKE_JOB_POOL_COMPILE.  

