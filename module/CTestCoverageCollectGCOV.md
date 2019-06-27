  

# CTestCoverageCollectGCOV  
This module provides the ctest_coverage_collect_gcov function.  

This function runs gcov on all .gcda files found in the binary tree
and packages the resulting .gcov files into a tar file.
This tarball also contains the following:  


data.json defines the source and build directories for use by CDash.
Labels.json indicates any LABELS that have been set on the
source files.
The uncovered directory holds any uncovered files found by
CTEST_EXTRA_COVERAGE_GLOB.
  

After generating this tar file, it can be sent to CDash for display with the
ctest_submit(CDASH_UPLOAD) command.  



cdash_coverage_collect_gcov
ctest_coverage_collect_gcov(TARBALL ```<tarfile>```
  [SOURCE ```<source_dir>```][BUILD ```<build_dir>```]
  [GCOV_COMMAND ```<gcov_command>```]
  [GCOV_OPTIONS ```<options>```...]
  )


Run gcov and package a tar file for CDash.  The options are:

TARBALL ```<tarfile>```
Specify the location of the .tar file to be created for later
upload to CDash.  Relative paths will be interpreted with respect
to the top-level build directory.
SOURCE ```<source_dir>```
Specify the top-level source directory for the build.
Default is the value of CTEST_SOURCE_DIRECTORY.
BUILD ```<build_dir>```
Specify the top-level build directory for the build.
Default is the value of CTEST_BINARY_DIRECTORY.
GCOV_COMMAND ```<gcov_command>```
Specify the full path to the gcov command on the machine.
Default is the value of CTEST_COVERAGE_COMMAND.
GCOV_OPTIONS ```<options>```...
Specify options to be passed to gcov.  The gcov command
is run as gcov ```<options>```... -o ```<gcov-dir>``` ```<file>```.gcda.
If not specified, the default option is just -b -x.
GLOB
Recursively search for .gcda files in build_dir rather than
determining search locations by reading TargetDirectories.txt.
DELETE
Delete coverage files after they¡¯ve been packaged into the .tar.
QUIET
Suppress non-error messages that otherwise would have been
printed out by this function.

  

