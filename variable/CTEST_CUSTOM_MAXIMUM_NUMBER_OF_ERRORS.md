  

# CTEST_CUSTOM_MAXIMUM_NUMBER_OF_ERRORS  
The maximum number of errors in a single build step which will be detected.
After this, the ctest_test() command will truncate the output.
Defaults to 50.  

It is initialized by ctest(1), but may be edited in a CTestCustom
file. See ctest_read_custom_files() documentation.  

