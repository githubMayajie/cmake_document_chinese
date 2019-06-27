  

# CMAKE_XCODE_GENERATE_TOP_LEVEL_PROJECT_ONLY  
If enabled, the Xcode generator will generate only a
single Xcode project file for the topmost project() command
instead of generating one for every project() command.  

This could be useful to speed up the CMake generation step for
large projects and to work-around a bug in the ZERO_CHECK logic.  
