  

# GHS_NO_SOURCE_GROUP_FILE  
ON / OFF boolean to control if the project file for a target should
be one single file or multiple files.  

The default behavior or when the property is OFF is to generate a project
file for the target and then a sub-project file for each source group.  

When this property is ON or if CMAKE_GHS_NO_SOURCE_GROUP_FILE
is ON then only a single project file is generated for the target.  

Supported on Green Hills MULTI.  

