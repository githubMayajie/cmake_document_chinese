  

# CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION  
Default value for DOTNET_TARGET_FRAMEWORK_VERSION
property of targets.  

This variable is used to initialize the
DOTNET_TARGET_FRAMEWORK_VERSION property on all
targets. See that target property for additional information.  

Setting CMAKE_DOTNET_TARGET_FRAMEWORK_VERSION may be necessary
when working with C# and newer .NET framework versions to
avoid referencing errors with the ALL_BUILD CMake target.  

This variable is only evaluated for Visual Studio Generators
VS 2010 and above.  

