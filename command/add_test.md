  

# add_test  
Add a test to the project to be run by ctest(1).  

add_test(NAME ```<name>``` COMMAND ```<command>``` [```<arg>```...]
         [CONFIGURATIONS ```<config>```...]
         [WORKING_DIRECTORY ```<dir>```])

  

Adds a test called ```<name>```.  The test name may not contain spaces,
quotes, or other characters special in CMake syntax.  The options are:  


COMMAND
Specify the test command-line.  If ```<command>``` specifies an
executable target (created by add_executable()) it will
automatically be replaced by the location of the executable created
at build time.
CONFIGURATIONS
Restrict execution of the test only to the named configurations.
WORKING_DIRECTORY
Set the WORKING_DIRECTORY test property to
specify the working directory in which to execute the test.
If not specified the test will be run with the current working
directory set to the build directory corresponding to the
current source directory.
  

The given test command is expected to exit with code 0 to pass and
non-zero to fail, or vice-versa if the WILL_FAIL test
property is set.  Any output written to stdout or stderr will be
captured by ctest(1) but does not affect the pass/fail status
unless the PASS_REGULAR_EXPRESSION or
FAIL_REGULAR_EXPRESSION test property is used.  

The COMMAND and WORKING_DIRECTORY options may use ˇ°generator
expressionsˇ± with the syntax $```<...>```.  See the
cmake-generator-expressions(7) manual for available expressions.  

Example usage:  

add_test(NAME mytest
         COMMAND testDriver --config $```<CONFIGURATION>```
                            --exe $```<TARGET_FILE:myexe>```)

  

This creates a test mytest whose command runs a testDriver tool
passing the configuration name and the full path to the executable
file produced by target myexe.  


Note
CMake will generate tests only if the enable_testing()
command has been invoked.  The CTest module invokes the
command automatically unless the BUILD_TESTING option is turned
OFF.
  

  

add_test(```<name>``` ```<command>``` [```<arg>```...])

  

Add a test called ```<name>``` with the given command-line.  Unlike
the above NAME signature no transformation is performed on the
command-line to support target names or generator expressions.  

