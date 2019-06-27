  

# CMakeVerifyManifest  
CMakeVerifyManifest.cmake  

This script is used to verify that embedded manifests and side by side
manifests for a project match.  To run this script, cd to a directory
and run the script with cmake -P.  On the command line you can pass in
versions that are OK even if not found in the .manifest files.  For
example, cmake -Dallow_versions=8.0.50608.0
-PCmakeVerifyManifest.cmake could be used to allow an embedded manifest
of 8.0.50608.0 to be used in a project even if that version was not
found in the .manifest file.  

