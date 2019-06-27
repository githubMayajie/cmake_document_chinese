  

# CTestUseLaunchers  
Set the RULE_LAUNCH_* global properties when CTEST_USE_LAUNCHERS is on.  

CTestUseLaunchers is automatically included when you include(CTest).
However, it is split out into its own module file so projects can use
the CTEST_USE_LAUNCHERS functionality independently.  

To use launchers, set CTEST_USE_LAUNCHERS to ON in a ctest -S
dashboard script, and then also set it in the cache of the configured
project.  Both cmake and ctest need to know the value of it for the
launchers to work properly.  CMake needs to know in order to generate
proper build rules, and ctest, in order to produce the proper error
and warning analysis.  

For convenience, you may set the ENV variable
CTEST_USE_LAUNCHERS_DEFAULT in your ctest -S script, too.  Then, as
long as your CMakeLists uses include(CTest) or
include(CTestUseLaunchers), it will use the value of the ENV variable
to initialize a CTEST_USE_LAUNCHERS cache variable.  This cache
variable initialization only occurs if CTEST_USE_LAUNCHERS is not
already defined. If CTEST_USE_LAUNCHERS is on in a ctest -S script
the ctest_configure command will add -DCTEST_USE_LAUNCHERS:BOOL=TRUE
to the cmake command used to configure the project.  

