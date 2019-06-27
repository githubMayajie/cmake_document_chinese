  

# CTEST_CUSTOM_MAXIMUM_FAILED_TEST_OUTPUT_SIZE  
When saving a failing test¡¯s output, this is the maximum size, in bytes, that
will be collected by the ctest_test() command. Defaults to 307200
(300 KiB).  

It is initialized by ctest(1), but may be edited in a CTestCustom
file. See ctest_read_custom_files() documentation.  

