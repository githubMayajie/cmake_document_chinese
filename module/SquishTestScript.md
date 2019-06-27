  

# SquishTestScript  
This script launches a GUI test using Squish.  You should not call the
script directly; instead, you should access it via the SQUISH_ADD_TEST
macro that is defined in FindSquish.cmake.  

This script starts the Squish server, launches the test on the client,
and finally stops the squish server.  If any of these steps fail
(including if the tests do not pass) then a fatal error is raised.  

