# cmake-buildsystem(7) 

## source 
https://cmake.org/cmake/help/latest/manual/cmake-buildsystem.7.html

## 目录
    - cmake-buildsystem(7)  
        - 概述
        - 二进制目标
            - 运行文件
            - 库类型
                - 通用库
                    - 苹果框架
                - 其他库
        - Build Specification and Usage Requirements
            - Target Properties
            - Transitive Usage Requirements
            - Compatible Interface Properties
            - Property Origin Debugging
            - Build Specification with Generator Expressions
                - Include Directories and Usage Requirements
            - Link Libraries and Generator Expressions
            - Output Artifacts
            - Runtime Output Artifacts
            - Library Output Artifacts
            - Archive Output Artifacts
            - Directory-Scoped Commands
        - Pseudo Targets
            - Imported Targets
            - Alias Targets
            - Interface Libraries

## 概述
基于CMake的构建系统由一组高级逻辑目标组成。 每个目标对应一个可执行文件或库，或者是自定义命令的自定义目标。目标之间通过依赖关系来确定构建顺序和文件更新或更改导致的构建更新顺序

## 二进制目标
使用[add_executable（）](../command/add_executable.md)和[add_library（）](../command/add_library.md)命令定义可执行文件和库文件。 该文件具有[PREFIX]()，[SUFFIX]()和针对平台的扩展的属性。用[target_link_libraries](../command/target_link_libraries.md)定义二进制目标之间的依赖关系

```cmake
add_library(archive archive.cpp zip.cpp lzma.cpp)
add_executable(zipapp zipapp.cpp)
target_link_libraries(zipapp archive)
```
archive被定义为STATIC库 - 包含从archive.cpp，zip.cpp和lzma.cpp编译的对象的静态库。 zipapp.cpp通过编译和链接形成的可执行文件zipapp。 链接zipapp可执行文件时，静态库链接的时候需要用到  

### 运行文件 
[add_executable()](../command/add_executable.md) 定义二进制运行目标  
```cmake
add_executable(mytool mytool.cpp)
```
正如[add_custom_command（）](../command/add_custom_command.md)可以生成在build时运行的规则，该命令通过明确地将[EXECUTABLE](../prop_tgt/TYPE.md)目标作为COMMAND运行文件，构建系统规则将确保在尝试运行命令之前构建可执行文件。  

### 库类型
#### 通用库
使用命令时可以指定类型，如果没有指定种类，默认情况下，[add_library()](../command/add_library)定义生成静态库，
```cmake
add_library(archive SHARED archive.cpp zip.cpp lzma.cpp)
add_library(archive STATIC archive.cpp zip.cpp lzma.cpp)
```
设置内置参数[BUILD_SHARED_LIBS](../variable/BUILD_SHARED_LIBS.md)可以改变add_library默认为共享库   
在整个构建系统生成中，指定库是SHARED还是STATIC很大程度上无关紧要 - 无论库类型如何，命令，依赖规范和其他API的使用方式都相似。MODULE库类型与SHARED或者STATIC行为不同，因为它通常不会被链接，他不会被[target_link_libraries](../command/target_link_libraries.md)命令调用,他会在runtime时加载（eg:dlopen/LoadLibrary）,如果库不导出任何符号（例如Windows资源DLL，C ++ / CLI DLL），则不能设置为为SHARED库，因为CMake期望至少导出一个符号向SHARED库。  
```cmake
add_library(archive MODULE 7z.cpp)
```
