  

# VS_CSHARP_```<tagname>```  
Visual Studio and CSharp source-file-specific configuration.  

Tell the Visual Studio generators
to set the source file tag ```<tagname>```
to a given value in the generated Visual Studio CSharp
project. Ignored on other generators and languages. This property
can be used to define dependencies between source files or set any
other Visual Studio specific parameters.  

Example usage:  

set_source_files_property(```<filename>```
         PROPERTIES
         VS_CSHARP_DependentUpon ```<other file>```
         VS_CSHARP_SubType "Form")

  

