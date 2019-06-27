  

# FindDCMTK  
Find DICOM ToolKit (DCMTK) libraries and applications  

The module defines the following variables:  

DCMTK_INCLUDE_DIRS  - Directories to include to use DCMTK
DCMTK_LIBRARIES     - Files to link against to use DCMTK
DCMTK_FOUND         - If false, don't try to use DCMTK
DCMTK_DIR           - (optional) Source directory for DCMTK

  


Compatibility
This module is able to find a version of DCMTK that does or does not export
a DCMTKConfig.cmake file. It applies a two step process:

Step 1:  Attempt to find DCMTK version providing a DCMTKConfig.cmake file.
Step 2:  If step 1 failed, rely on FindDCMTK.cmake to set DCMTK_* variables details below.

Recent DCMTK
provides a DCMTKConfig.cmake package configuration file. To exclusively use the package configuration file
(recommended when possible), pass the NO_MODULE option to
find_package(). For example, find_package(DCMTK NO_MODULE).
This requires official DCMTK snapshot 3.6.1_20140617 or newer.
Until all clients update to the more recent DCMTK, build systems will need
to support different versions of DCMTK.
On any given system, the following combinations of DCMTK versions could be
considered:









SYSTEM DCMTK
LOCAL DCMTK
Supported ?

Case A
NA
[ ] DCMTKConfig
YES

Case B
NA
[X] DCMTKConfig
YES

Case C
[ ] DCMTKConfig
NA
YES

Case D
[X] DCMTKConfig
NA
YES

Case E
[ ] DCMTKConfig
[ ] DCMTKConfig
YES (*)

Case F
[X] DCMTKConfig
[ ] DCMTKConfig
NO

Case G
[ ] DCMTKConfig
[X] DCMTKConfig
YES

Case H
[X] DCMTKConfig
[X] DCMTKConfig
YES




(*) See Troubleshooting section.
Legend:

NA ¡­¡­¡­¡­¡­: Means that no System or Local DCMTK is available
[ ] DCMTKConfig ..: Means that the version of DCMTK does NOT export a DCMTKConfig.cmake file.
[X] DCMTKConfig ..: Means that the version of DCMTK exports a DCMTKConfig.cmake file.

  


Troubleshooting
What to do if my project finds a different version of DCMTK?
Remove DCMTK entry from the CMake cache per find_package()
documentation.
  

