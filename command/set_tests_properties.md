  

# set_tests_properties  
Set a property of the tests.  

set_tests_properties(test1 [test2...] PROPERTIES prop1 value1 prop2 value2)

  

Sets a property for the tests.  If the test is not found, CMake
will report an error.
Generator expressions will be
expanded the same as supported by the test��s add_test() call.  

See also the set_property(TEST) command.  

See Properties on Tests for the list of properties known to CMake.  

