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
                - 对象库
        - 构建规范和使用要求
            - 目标属性
            - 使用传递要求
            - 接口兼容属性
            - 调试属性
            - Generator表达式构建规范
                - 加入目录和使用要求
            - 链接库和生成器表达式
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
使用[add_executable（）](../command/add_executable.md)和[add_library（）](../command/add_library.md)命令定义可执行文件和库文件。 该文件具有[PREFIX](../prop_tgt/PREFIX.md)，[SUFFIX](../prop_tgt/SUFFIX.md)和针对平台的扩展的属性。用[target_link_libraries](../command/target_link_libraries.md)定义二进制目标之间的依赖关系

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

##### 苹果架构
SHARED库用FRAMEWORK标记库属性用来创建macOS或iOS Framework Bundle。 MACOSX_FRAMEWORK_IDENTIFIER设置CFBundleIdentifier用来设置bundleID  
```cmake
add_library(MyFramework SHARED MyFramework.cpp)
set_target_properties(MyFramework PROPERTIES
  FRAMEWORK TRUE
  FRAMEWORK_VERSION A
  MACOSX_FRAMEWORK_IDENTIFIER org.cmake.MyFramework
)
```

#### 对象库
OBJECT库类型定义了编译给定源文件所产生的非归档目标文件集合。 目标文件集合可以用作其他目标的源输入   
```cmake
add_library(archive OBJECT archive.cpp zip.cpp lzma.cpp)

add_library(archiveExtras STATIC $<TARGET_OBJECTS:archive> extras.cpp)

add_executable(test_exe $<TARGET_OBJECTS:archive> test.cpp)
```
这些其他目标的链接（或归档）步骤将使用目标文件集合以及来自其自身来源的目标文件集合。  
另外，对象库可以链接到其他目标：  
```cmake
add_library(archive OBJECT archive.cpp zip.cpp lzma.cpp)

add_library(archiveExtras STATIC extras.cpp)
target_link_libraries(archiveExtras PUBLIC archive)

add_executable(test_exe test.cpp)
target_link_libraries(test_exe archive)
```
其他目标链接（或归档）的时候将直接链接的OBJECT库中的目标文件。 此外，在编译其他目标时，将遵守OBJECT库的使用要求。 此外，这些使用要求将传递给那些其他目标。  

在使用[add_custom_command（TARGET）](../command/add_custom_command.md)命令时，不能将对象库用作TARGET。 但是，[add_custom_command（OUTPUT）](../command/add_custom_command.md)或[file（GENERATE）](../command/file.md)可以使用$ <TARGET_OBJECTS：objlib>来使用OBJECT库  

## 构建规范和使用要求
[target_include_directories（）](../command/target_include_directories.md)，[target_compile_definitions（）](../command/target_compile_definitions.md)和[target_compile_options（）](../command/target_compile_options.md)命令指定构建规范和二进制目标的使用要求。 这些命令分别填充[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)，[COMPILE_DEFINITIONS](../prop_tgt/COMPILE_DEFINITIONS.md)和[COMPILE_OPTIONS](../prop_tgt/COMPILE_OPTIONS.md)目标属性，和或着和填充了[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)，[INTERFACE_COMPILE_DEFINITIONS](../prop_tgt/INTERFACE_COMPILE_DEFINITIONS.md)和[INTERFACE_COMPILE_OPTIONS](../prop_tgt/INTERFACE_COMPILE_OPTIONS.md)目标属性。

每个命令都有PRIVATE，PUBLIC和INTERFACE模式。 PRIVATE模式仅填充目标属性的非INTERFACE变量，INTERFACE模式仅填充INTERFACE变量。 PUBLIC模式填充相应目标属性的两个变量。 可以次使用每个关键字的调用每个命令：
```cmake
target_compile_definitions(archive
  PRIVATE BUILDING_WITH_LZMA
  INTERFACE USING_ARCHIVE_LIB
)
```
请注意，使用要求并非旨为方便使用COMPILE_OPTIONS或COMPILE_DEFINITIONS等，属性的内容必须强制要求。

有关在创建重新分发包时指定使用要求时必须采取的额外注意事项的讨论，请参阅cmake-packages（7）手册的[创建可重定位包](./cmake-packages.7.md)部分。

### 目标属性
编译二进制目标的源文件时，将使用[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)，[COMPILE_DEFINITIONS](../prop_tgt/COMPILE_DEFINITIONS.md)和[COMPILE_OPTIONS](../prop_tgt/COMPILE_DEFINITIONS.md) 目标属性的内容。

[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)中的内容将使用-I或-isystem前缀以及属性值中的顺序添加到编译命令中。

[COMPILE_DEFINITIONS](../prop_tgt/COMPILE_DEFINITIONS.md)中的内容 以-D或/ D为前缀，并以未指定的顺序添加到编译命令中。 [DEFINE_SYMBOL](../prop_tgt/DEFINE_SYMBOL.md)目标属性也作为编译定义添加为SHARED和MODULE库目标的特殊含义。

[COMPILE_OPTIONS](../prop_tgt/COMPILE_DEFINITIONS.md)中的内容将针对shell进行转义，并按属性值中的顺序添加到编译命令中。有些编译选项有特殊的单独处理，例如[POSITION_INDEPENDENT_CODE](../prop_tgt/POSITION_INDEPENDENT_CODE.md)。

[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)，[INTERFACE_COMPILE_DEFINITIONS](../prop_tgt/INTERFACE_COMPILE_DEFINITIONS.md)和[INTERFACE_COMPILE_OPTIONS](../prop_tgt/INTERFACE_COMPILE_OPTIONS.md)目标属性是有必要的 - 它们指定依赖目标必须使用内容才能正确编译并链接到目标。对于任何二进制目标，将使用[target_link_libraries（）](../command/target_link_libraries.md)命令中使用对应INTERFACE属性的内容：  

```cmake
set(srcs archive.cpp zip.cpp)
if (LZMA_FOUND)
  list(APPEND srcs lzma.cpp)
endif()
add_library(archive SHARED ${srcs})
if (LZMA_FOUND)
  # The archive library sources are compiled with -DBUILDING_WITH_LZMA
  target_compile_definitions(archive PRIVATE BUILDING_WITH_LZMA)
endif()
target_compile_definitions(archive INTERFACE USING_ARCHIVE_LIB)

add_executable(consumer)
# Link consumer to archive and consume its usage requirements. The consumer
# executable sources are compiled with -DUSING_ARCHIVE_LIB.
target_link_libraries(consumer archive)
```
通常将源目录和相应的构建目录添加到[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)，所以启用[CMAKE_INCLUDE_CURRENT_DIR](../prop_tgt/CMAKE_INCLUDE_CURRENT_DIR.md)变量以方便地将相应的目录添加到所有目标的[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)。 可以启用变量[CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE](../prop_tgt/CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE.md)以将相应的目录添加到所有目标的[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)。 这样可以通过使用[target_link_libraries（）](../command/target_link_libraries.md)命令方便地在多个不同目录中使用目标。  

### 使用传递要求
目标的使用要求可以传递给所依赖的目标。 [target_link_libraries（）](../command/target_link_libraries.md)命令具有PRIVATE，INTERFACE和PUBLIC关键字来控制传递要求。  

```cmake
add_library(archive archive.cpp)
target_compile_definitions(archive INTERFACE USING_ARCHIVE_LIB)

add_library(serialization serialization.cpp)
target_compile_definitions(serialization INTERFACE USING_SERIALIZATION_LIB)

add_library(archiveExtras extras.cpp)
target_link_libraries(archiveExtras PUBLIC archive)
target_link_libraries(archiveExtras PRIVATE serialization)
# archiveExtras is compiled with -DUSING_ARCHIVE_LIB
# and -DUSING_SERIALIZATION_LIB

add_executable(consumer consumer.cpp)
# consumer is compiled with -DUSING_ARCHIVE_LIB
target_link_libraries(consumer archiveExtras)
```
由于archiveExtras目标通过PUBLIC 依赖 archive 库，archiveExtras全部继承了archive的目标属性（包括编译属性 -DUSING_ARCHIVE_LIB）,archiveExtras目标通过PRIVATE 依赖 seriallization 库，seriallization的目标属性不会传递给archiveExtras目标。    
通常，如果仅仅使用库文件，没有使用头文件，则应该使用PRIVATE定义[target_link_libraries（）](../command/target_link_libraries.md)，如果依赖目标需要引入头文件（例如，用于类继承），则应该设置PUBLIC依赖，如果没有使用库实现，只使用了库头文件，则应该设置INTERFACE依赖，[target_link_libraries（）](../command/target_link_libraries.md)可以使用多个关键词设置多项依赖。    
```cmake
target_link_libraries(archiveExtras
  PUBLIC archive
  PRIVATE serialization
)
```

使用要求。 例如，读取依赖项的INTERFACE_INCLUDE_DIRECTORIES并将其附加到操作数的INCLUDE_DIRECTORIES。 如果订单相关并且维护，并且target_link_libraries（）调用产生的订单不允许正确编译，则使用适当的命令直接设置属性可以更新订单。

使用要求通过从依赖项中读取目标属性的INTERFACE_变量并将非INTERFACE_变量值附加到目标。例如，读取依赖项的[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)并将其附加到目标的[INCLUDE_DIRECTORIES](../prop_tgt/INCLUDE_DIRECTORIES.md)。如果顺序已经被修改，并且[target_link_libraries（）](../command/target_link_libraries.md)调用产生的顺序不允许正确编译，则使用适当的命令直接设置属性可以更新顺序。  
例如，如果必须按lib1 lib2 lib3的顺序指定目标的链接库，但必须按lib3 lib1 lib2的顺序指定include目录：  
```cmake
target_link_libraries(myExe lib1 lib2 lib3)
target_include_directories(myExe
  PRIVATE $<TARGET_PROPERTY:lib3,INTERFACE_INCLUDE_DIRECTORIES>)
```
请注意，在使用[install（EXPORT）](../command/install.md)命令指定将导出以进行安装的目标的使用要求时必须小心。 请参阅[创建包](./cmake-packages.7.md)以获取更多。  

### 接口兼容属性
某些目标属性需要在目标和每个依赖项的接口之间兼容，例如，[POSITION_INDEPENDENT_CODE](../prop_tgt/POSITION_INDEPENDENT_CODE.md)目标属性可以指定是否应将目标编译为位置无关代码，该代码具有特定于平台的后果。 目标还可以指定使用要求[INTERFACE_POSITION_INDEPENDENT_CODE](../prop_tgt/INTERFACE_POSITION_INDEPENDENT_CODE.md)以传达依赖目标必须编译为位置无关代码。  
```cmake
add_executable(exe1 exe1.cpp)
set_property(TARGET exe1 PROPERTY POSITION_INDEPENDENT_CODE ON)

add_library(lib1 SHARED lib1.cpp)
set_property(TARGET lib1 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)

add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1)
```
这里，exe1和exe2都将被编译为与位置无关的代码。 lib1也将被编译为与位置无关的代码，因为这是SHARED库的默认设置。 如果依赖关系具有冲突，不兼容的要求[cmake（1）](./cmake.1.md)发出诊断：
```cmake
add_library(lib1 SHARED lib1.cpp)
set_property(TARGET lib1 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)

add_library(lib2 SHARED lib2.cpp)
set_property(TARGET lib2 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE OFF)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1)
set_property(TARGET exe1 PROPERTY POSITION_INDEPENDENT_CODE OFF)

add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1 lib2)
```
lib1要求INTERFACE_POSITION_INDEPENDENT_CODE与exe1目标的POSITION_INDEPENDENT_CODE属性“不兼容”。 该库要求构建为与位置无关的代码，而可执行文件指定构建为与位置有关的代码，因此发出诊断。   
lib1和lib2是不“兼容的”。 其中一个要求构建参数为与位置无关的代码，而另一个要求构建参数为与位置有关的代码。 因为exe2链接到两者并且它们存在冲突，所以会发出诊断。    
要与[POSITION_INDEPENDENT_CODE](../prop_tgt/POSITION_INDEPENDENT_CODE.md)属性（如果设置）“兼容”，该值设置该属性的所有传递指定依赖项的[INTERFACE_POSITION_INDEPENDENT_CODE](../prop_tgt/INTERFACE_POSITION_INDEPENDENT_CODE.md)属性   
通过设置[COMPATIBLE_INTERFACE_BOOL](../prop_tgt/COMPATIBLE_INTERFACE_BOOL.md)指定属性，可以将“兼容接口要求”的此属性扩展到其他属性。 每个指定的属性必须在使用目标和相应的属性之间兼容，并且每个依赖项都有一个INTERFACE_前缀    
```cmake
add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_CUSTOM_PROP ON)
set_property(TARGET lib1Version2 APPEND PROPERTY
  COMPATIBLE_INTERFACE_BOOL CUSTOM_PROP
)

add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_CUSTOM_PROP OFF)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2) # CUSTOM_PROP will be ON

add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1Version2 lib1Version3) # Diagnostic
```
非布尔属性也可以参与“兼容接口”设置。 [COMPATIBLE_INTERFACE_STRING](../prop_tgt/COMPATIBLE_INTERFACE_STRING.md)属性中指定的属性必须是未指定的，或者与所有可传递指定的依赖项中的相同字符串进行比较。 这可以用于确保库的多个不兼容版本不会通过目标的传递要求链接在一起  
```cmake
add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_LIB_VERSION 2)
set_property(TARGET lib1Version2 APPEND PROPERTY
  COMPATIBLE_INTERFACE_STRING LIB_VERSION
)

add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_LIB_VERSION 3)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2) # LIB_VERSION will be "2"

add_executable(exe2 exe2.cpp)
target_link_libraries(exe2 lib1Version2 lib1Version3) # Diagnostic
```
用数字设置[COMPATIBLE_INTERFACE_NUMBER_MAX](../prop_tgt/COMPATIBLE_INTERFACE_NUMBER_MAX.md)目标属性指定评估内容，并指定的最大数量：  
```cmake
add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY INTERFACE_CONTAINER_SIZE_REQUIRED 200)
set_property(TARGET lib1Version2 APPEND PROPERTY
  COMPATIBLE_INTERFACE_NUMBER_MAX CONTAINER_SIZE_REQUIRED
)

add_library(lib1Version3 SHARED lib1_v3.cpp)
set_property(TARGET lib1Version3 PROPERTY INTERFACE_CONTAINER_SIZE_REQUIRED 1000)

add_executable(exe1 exe1.cpp)
# CONTAINER_SIZE_REQUIRED will be "200"
target_link_libraries(exe1 lib1Version2)

add_executable(exe2 exe2.cpp)
# CONTAINER_SIZE_REQUIRED will be "1000"
target_link_libraries(exe2 lib1Version2 lib1Version3)
```
同样，[COMPATIBLE_INTERFACE_NUMBER_MIN](../prop_tgt/COMPATIBLE_INTERFACE_NUMBER_MIN.md)可用于指定属性的最小值。  
可以使用生成器表达式在生成时在依赖目标中读取每个计算的“兼容”属性值。  
请注意，对于每个依赖项，每个兼容接口属性中指定的属性集不得与任何其他属性中指定的集相交。


### 调试属性
因为构建规范可以由依赖性来确定，缺少了创建目标的代码的局部性以及负责设置构建规范的代码可能使代码更难以推理。 [cmake（1）](./cmake.1.md)提供了一个调试工具来打印可能由依赖关系确定的属性内容。 可以调试的属性列在[CMAKE_DEBUG_TARGET_PROPERTIES](../variable/CMAKE_DEBUG_TARGET_PROPERTIES.md)变量文档中：
```cmake
set(CMAKE_DEBUG_TARGET_PROPERTIES
  INCLUDE_DIRECTORIES
  COMPILE_DEFINITIONS
  POSITION_INDEPENDENT_CODE
  CONTAINER_SIZE_REQUIRED
  LIB_VERSION
)
add_executable(exe1 exe1.cpp)
```
对于[COMPATIBLE_INTERFACE_BOOL](../prop_tgt/COMPATIBLE_INTERFACE_BOOL.md)或[COMPATIBLE_INTERFACE_STRING](../prop_tgt/COMPATIBLE_INTERFACE_STRING.md)中列出的属性，调试输出显示哪个目标负责设置哪个属性，以及哪些其他依赖项也定义了该属性。 对于[COMPATIBLE_INTERFACE_NUMBER_MAX](../prop_tgt/COMPATIBLE_INTERFACE_NUMBER_MAX.md)和[COMPATIBLE_INTERFACE_NUMBER_MIN](../prop_tgt/COMPATIBLE_INTERFACE_NUMBER_MIN.md)，调试输出显示每个依赖项的属性值，以及该值是否确定新的最大最小值。    

### Generator表达式构建规范
构建规范可以使用包含内容的[generator expressions](./cmake-generator-expressions.7.md)，该内容可以是某些条件的或仅限生成时信息。 例如，可以使用TARGET_PROPERTY表达式读取属性的“兼容”值：
```cmake
add_library(lib1Version2 SHARED lib1_v2.cpp)
set_property(TARGET lib1Version2 PROPERTY
  INTERFACE_CONTAINER_SIZE_REQUIRED 200)
set_property(TARGET lib1Version2 APPEND PROPERTY
  COMPATIBLE_INTERFACE_NUMBER_MAX CONTAINER_SIZE_REQUIRED
)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1Version2)
target_compile_definitions(exe1 PRIVATE
    CONTAINER_SIZE=$<TARGET_PROPERTY:CONTAINER_SIZE_REQUIRED>
)
```
在这种情况下，exe1源文件将使用-DCONTAINER_SIZE = 200进行编译。  

可以使用CONFIG生成器表达式方便地设置配置确定的构建规范。
```cmake
target_compile_definitions(exe1 PRIVATE
    $<$<CONFIG:Debug>:DEBUG_BUILD>
)
```
CONFIG参数不区分大小写与正在构建的配置进行比较。 在存在[IMPORTED](../prop_tgt/IMPORTED.md)目标的情况下，此表达式还会受[MAP_IMPORTED_CONFIG_DEBUG](../prop_tgt/MAP_IMPORTED_CONFIG_DEBUG.md)的内容影响。    
由[cmake（1）](./cmake.1.md)生成的一些构建系统在[CMAKE_BUILD_TYPE](../variable/CMAKE_BUILD_TYPE.md)变量中具有预定的构建配置集。 诸如Visual Studio和Xcode之类的IDE的构建系统是独立于构建配置生成的，并且在构建时之前不知道实际的构建配置。 因此，代码如    
```cmake
string(TOLOWER ${CMAKE_BUILD_TYPE} _type)
if (_type STREQUAL debug)
  target_compile_definitions(exe1 PRIVATE DEBUG_BUILD)
endif()
```
可能适用于[Makefile生成器](./cmake-generators.7.md)和[Ninja生成器](../generator/Ninja.md)，但不能移植到IDE生成器。 此外，[IMPORTED](../prop_tgt/IMPORTED.md)配置映射也不会被IDE接受，因此应该避免。  
目标上下文计算一元TARGET_PROPERTY生成器表达式和TARGET_POLICY生成器表达式。 这意味着可以根据目标不同评估使用规范：  
```cmake
add_library(lib1 lib1.cpp)
target_compile_definitions(lib1 INTERFACE
  $<$<STREQUAL:$<TARGET_PROPERTY:TYPE>,EXECUTABLE>:LIB1_WITH_EXE>
  $<$<STREQUAL:$<TARGET_PROPERTY:TYPE>,SHARED_LIBRARY>:LIB1_WITH_SHARED_LIB>
  $<$<TARGET_POLICY:CMP0041>:CONSUMER_CMP0041_NEW>
)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1)

cmake_policy(SET CMP0041 NEW)

add_library(shared_lib shared_lib.cpp)
target_link_libraries(shared_lib lib1)
```
exe1可执行文件将使用-DLIB1_WITH_EXE进行编译，而shared_lib共享库将使用-DLIB1_WITH_SHARED_LIB和-DCONSUMER_CMP0041_NEW进行编译，因为策略[CMP0041](../policy/CMP0041.md)在创建shared_lib目标时为NEW。  
BUILD_INTERFACE表达式包含仅在从同一构建系统中的目标使用时使用的需求，或者使用export（）命令从导出到构建目录的目标使用时使用的需求。 INSTALL_INTERFACE表达式包含仅在使用install（EXPORT）命令安装和导出的目标使用时才使用的需求：    
```cmake
add_library(ClimbingStats climbingstats.cpp)
target_compile_definitions(ClimbingStats INTERFACE
  $<BUILD_INTERFACE:ClimbingStats_FROM_BUILD_LOCATION>
  $<INSTALL_INTERFACE:ClimbingStats_FROM_INSTALLED_LOCATION>
)
install(TARGETS ClimbingStats EXPORT libExport ${InstallArgs})
install(EXPORT libExport NAMESPACE Upstream::
        DESTINATION lib/cmake/ClimbingStats)
export(EXPORT libExport NAMESPACE Upstream::)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 ClimbingStats)
```
在这种情况下，exe1可执行文件将使用-DClimbingStats_FROM_BUILD_LOCATION进行编译。 导出命令生成IMPORTED目标，省略INSTALL_INTERFACE或BUILD_INTERFACE，并删除* _INTERFACE标记。 使用ClimbingStats包的单独项目将包含：  
```cmake
find_package(ClimbingStats REQUIRED)

add_executable(Downstream main.cpp)
target_link_libraries(Downstream Upstream::ClimbingStats)
```
根据是从构建位置还是安装位置使用ClimbingStats包，可以使用-DClimbingStats_FROM_BUILD_LOCATION或-DClimbingStats_FROM_INSTALL_LOCATION编译下游目标。 有关包和导出的更多信息，请参阅[cmake-packages（7）](./cmake-packages.7.md)手册。  
#### 加入目录和使用要求 
当指定为使用要求时以及与生成器表达式一起使用时，包含目录需要特别考虑。 target_include_directories（）命令接受相对和绝对包含目录：  
```cmake
add_library(lib1 lib1.cpp)
target_include_directories(lib1 PRIVATE
  /absolute/path
  relative/path
)
```
相对路径相对于命令出现的源目录进行解释。 [IMPORTED](../prop_tgt/IMPORTED.md)目标的[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)中不允许相对路径。  
在使用非平凡的生成器表达式的情况下，INSTALL_PREFIX表达式可以在INSTALL_INTERFACE表达式的参数内使用。 它是一个替换标记，在使用项目导入时会扩展为安装前缀。  
包含目录使用要求通常在构建树和安装树之间有所不同。 BUILD_INTERFACE和INSTALL_INTERFACE生成器表达式可用于根据使用位置描述单独的使用要求。 INSTALL_INTERFACE表达式中允许使用相对路径，并相对于安装前缀进行解释。 例如：  
```cmake
add_library(ClimbingStats climbingstats.cpp)
target_include_directories(ClimbingStats INTERFACE
  $<BUILD_INTERFACE:${CMAKE_CURRENT_BINARY_DIR}/generated>
  $<INSTALL_INTERFACE:/absolute/path>
  $<INSTALL_INTERFACE:relative/path>
  $<INSTALL_INTERFACE:$<INSTALL_PREFIX>/$<CONFIG>/generated>
)
```
提供了两个与包含目录使用要求相关的便利API。 可以启用[CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE](../variable/CMAKE_INCLUDE_CURRENT_DIR_IN_INTERFACE.md)变量，其效果与：  
```cmake
set_property(TARGET tgt APPEND PROPERTY INTERFACE_INCLUDE_DIRECTORIES
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR};${CMAKE_CURRENT_BINARY_DIR}>
)
```
对于每个受影响的目标 安装目标的便利性是带有安装[（TARGETS）](../command/install.md)命令的INCLUDES DESTINATION组件：  
```cmake
install(TARGETS foo bar bat EXPORT tgts ${dest_args}
  INCLUDES DESTINATION include
)
install(EXPORT tgts ${other_args})
install(FILES ${headers} DESTINATION include)
```
这相当于在[install（EXPORT）](../command/install.md)生成时将$ {CMAKE_INSTALL_PREFIX} / include附加到每个已安装的[IMPORTED](../prop_tgt/IMPORTED.md)目标的[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)。   
当使用[imported target]()的[INTERFACE_INCLUDE_DIRECTORIES](../prop_tgt/INTERFACE_INCLUDE_DIRECTORIES.md)时，属性中的条目将被视为SYSTEM包含目录，就好像它们列在依赖项的[INTERFACE_SYSTEM_INCLUDE_DIRECTORIES](../../prop_tgt/INTERFACE_SYSTEM_INCLUDE_DIRECTORIES.md)中一样。 这可能导致省略在这些目录中找到的标头的编译器警告。 可以通过在[imported target]()的使用者上设置[NO_SYSTEM_FROM_IMPORTED](../prop_tgt/NO_SYSTEM_FROM_IMPORTED.md)目标属性来控制导入目标的此行为。   
如果二进制目标与macOS [FRAMEWORK](../prop_tgt/FRAMEWORK.md)传递链接，则框架的Headers目录也会被视为使用要求。 这与将framework目录作为include目录传递具有相同的效果。    

### 链接库和生成器表达式
与构建规范一样，可以使用生成器表达条件指定[链接库](../prop_tgt/LINK_LIBRARIES.md)。 但是，由于使用要求是基于链接依赖关系，因此链接依赖关系必须形成“有向非循环图”的另一个限制。 也就是说，如果链接到目标依赖于目标属性的值，那么该目标属性可能不依赖于链接的依赖项：  
```cmake
add_library(lib1 lib1.cpp)
add_library(lib2 lib2.cpp)
target_link_libraries(lib1 PUBLIC
  $<$<TARGET_PROPERTY:POSITION_INDEPENDENT_CODE>:lib2>
)
add_library(lib3 lib3.cpp)
set_property(TARGET lib3 PROPERTY INTERFACE_POSITION_INDEPENDENT_CODE ON)

add_executable(exe1 exe1.cpp)
target_link_libraries(exe1 lib1 lib3)
```
由于exe1目标的[POSITION_INDEPENDENT_CODE](../prop_tgt/POSITION_INDEPENDENT_CODE.md)属性的值取决于链接库（lib3），并且链接exe1的边缘由相同的[POSITION_INDEPENDENT_CODE](../prop_tgt/POSITION_INDEPENDENT_CODE.md)属性确定，因此上面的依赖关系图包含一个循环。 [cmake（1）](./cmake.1.md)在这种情况下发出诊断。  

### Output Artifacts

### Runtime Output Artifacts

### Library Output Artifacts


### Archive Output Artifacts

### Directory-Scoped Commands

## Pseudo Targets

### Imported Targets

### Alias Targets

### Interface Libraries