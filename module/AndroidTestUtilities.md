  

# AndroidTestUtilities  
Create a test that automatically loads specified data onto an Android device.  


Introduction
Use this module to push data needed for testing an Android device behavior
onto a connected Android device. The module will accept files and libraries as
well as separate destinations for each. It will create a test that loads the
files into a device object store and link to them from the specified
destination. The files are only uploaded if they are not already in the object
store.
For example:
include(AndroidTestUtilities)
android_add_test_data(
  example_setup_test
  FILES ```<files>```...
  LIBS ```<libs>```...
  DEVICE_TEST_DIR "/data/local/tests/example"
  DEVICE_OBJECT_STORE "/sdcard/.ExternalData/SHA"
  )


At build time a test named ¡°example_setup_test¡± will be created.  Run this test
on the command line with ctest(1) to load the data onto the Android
device.
  


Module Functions


android_add_test_data
android_add_test_data(```<test-name>```
  [FILES ```<files>```...] [FILES_DEST ```<device-dir>```]
  [LIBS ```<libs>```...]   [LIBS_DEST ```<device-dir>```]
  [DEVICE_OBJECT_STORE ```<device-dir>```]
  [DEVICE_TEST_DIR ```<device-dir>```]
  [NO_LINK_REGEX ```<strings>```...]
  )


The android_add_test_data function is used to copy files and libraries
needed to run project-specific tests. On the host operating system, this is
done at build time. For on-device testing, the files are loaded onto the
device by the manufactured test at run time.
This function accepts the following named parameters:

FILES ```<files>```...
zero or more files needed for testing
LIBS ```<libs>```...
zero or more libraries needed for testing
FILES_DEST ```<device-dir>```
absolute path where the data files are expected to be
LIBS_DEST ```<device-dir>```
absolute path where the libraries are expected to be
DEVICE_OBJECT_STORE ```<device-dir>```
absolute path to the location where the data is stored on-device
DEVICE_TEST_DIR ```<device-dir>```
absolute path to the root directory of the on-device test location
NO_LINK_REGEX ```<strings>```...
list of regex strings matching the names of files that should be
copied from the object store to the testing directory


  

