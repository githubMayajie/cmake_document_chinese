  

# VS_DOTNET_REFERENCEPROP_```<refname>```_TAG_```<tagname>```  
Defines an XML property ```<tagname>``` for a .NET reference
```<refname>```.  

Reference properties can be set for .NET references which are
defined by the target properties VS_DOTNET_REFERENCES,
VS_DOTNET_REFERENCE_```<refname>```
and also for project references to other C# targets which are
established by target_link_libraries().  

This property is only applicable to C# targets and Visual Studio
generators 2010 and later.  

