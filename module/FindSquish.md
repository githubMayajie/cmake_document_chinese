  

# FindSquish  
¨C Typical Use  

This module can be used to find Squish.  Currently Squish versions 3
and 4 are supported.  

SQUISH_FOUND                    If false, don't try to use Squish
SQUISH_VERSION                  The full version of Squish found
SQUISH_VERSION_MAJOR            The major version of Squish found
SQUISH_VERSION_MINOR            The minor version of Squish found
SQUISH_VERSION_PATCH            The patch version of Squish found

  

SQUISH_INSTALL_DIR              The Squish installation directory
                                (containing bin, lib, etc)
SQUISH_SERVER_EXECUTABLE        The squishserver executable
SQUISH_CLIENT_EXECUTABLE        The squishrunner executable

  

SQUISH_INSTALL_DIR_FOUND        Was the install directory found?
SQUISH_SERVER_EXECUTABLE_FOUND  Was the server executable found?
SQUISH_CLIENT_EXECUTABLE_FOUND  Was the client executable found?

  

It provides the function squish_v4_add_test() for adding a squish test
to cmake using Squish 4.x:  

squish_v4_add_test(cmakeTestName
  AUT targetName SUITE suiteName TEST squishTestName
  [SETTINGSGROUP group] [PRE_COMMAND command] [POST_COMMAND command] )

  

The arguments have the following meaning:  


cmakeTestName
this will be used as the first argument for add_test()
AUT targetName
the name of the cmake target which will be used as AUT, i.e. the
executable which will be tested.
SUITE suiteName
this is either the full path to the squish suite, or just the
last directory of the suite, i.e. the suite name. In this case
the CMakeLists.txt which calls squish_add_test() must be located
in the parent directory of the suite directory.
TEST squishTestName
the name of the squish test, i.e. the name of the subdirectory
of the test inside the suite directory.
SETTINGSGROUP group
if specified, the given settings group will be used for executing the test.
If not specified, the groupname will be ¡°CTest_```<username>```¡±
PRE_COMMAND command
if specified, the given command will be executed before starting the squish test.
POST_COMMAND command
same as PRE_COMMAND, but after the squish test has been executed.
  

enable_testing()
find_package(Squish 4.0)
if (SQUISH_FOUND)
   squish_v4_add_test(myTestName
     AUT myApp
     SUITE ${CMAKE_SOURCE_DIR}/tests/mySuite
     TEST someSquishTest
     SETTINGSGROUP myGroup
     )
endif ()

  

For users of Squish version 3.x the macro squish_v3_add_test() is
provided:  

squish_v3_add_test(testName applicationUnderTest testCase envVars testWrapper)
Use this macro to add a test using Squish 3.x.

  

enable_testing()
find_package(Squish)
if (SQUISH_FOUND)
  squish_v3_add_test(myTestName myApplication testCase envVars testWrapper)
endif ()

  

macro SQUISH_ADD_TEST(testName applicationUnderTest testCase envVars
testWrapper)  

This is deprecated. Use SQUISH_V3_ADD_TEST() if you are using Squish 3.x instead.

  

