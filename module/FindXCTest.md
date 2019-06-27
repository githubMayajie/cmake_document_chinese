  

# FindXCTest  
Functions to help creating and executing XCTest bundles.  

An XCTest bundle is a CFBundle with a special product-type
and bundle extension. The Mac Developer Library provides more
information in the Testing with Xcode document.  


Module Functions


xctest_add_bundle
The xctest_add_bundle function creates a XCTest bundle named
```<target>``` which will test the target ```<testee>```. Supported target types
for testee are Frameworks and App Bundles:
xctest_add_bundle(
  ```<target>```  # Name of the XCTest bundle
  ```<testee>```  # Target name of the testee
  )





xctest_add_test
The xctest_add_test function adds an XCTest bundle to the
project to be run by ctest(1). The test will be named
```<name>``` and tests ```<bundle>```:
xctest_add_test(
  ```<name>```    # Test name
  ```<bundle>```  # Target name of XCTest bundle
  )



  


Module Variables
The following variables are set by including this module:


XCTest_FOUND
True if the XCTest Framework and executable were found.



XCTest_EXECUTABLE
The path to the xctest command line tool used to execute XCTest bundles.



XCTest_INCLUDE_DIRS
The directory containing the XCTest Framework headers.



XCTest_LIBRARIES
The location of the XCTest Framework.

  

