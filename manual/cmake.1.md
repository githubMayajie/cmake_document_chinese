# cmake(1)

## source
https://cmake.org/cmake/help/latest/manual/cmake.1.html  

## <h2 id="Synopsis">概要</h2>

[生成构建系统](#Generate_a_Project_Buildsystem)
```cmake
cmake [<options>] <path-to-source>
cmake [<options>] <path-to-existing-build>
cmake [<options>] -S <path-to-source> -B <path-to-build>
```

[build项目](#Build_a_Project)
```cmake
cmake --build <dir> [<options>] [-- <build-tool-options>]
```

[安装项目](#Install_a_Project)
```sh
cmake --install <dir> [<options>]
```

[打开项目](#Open_a_Project)
```cmake
cmake --open <dir>
```

[运行脚本](#Run_a_Script)
```cmake
cmake [{-D <var>=<value>}...] -P <cmake-script-file>
```

[运行命令工具](#Run_a_Command_Line_Tool)
```cmake
cmake -E <command> [<options>]
```

[运行findPackage工具](#Run_the_Find_Package_Tool)
```cmake
cmake --find-package [<options>]
```

[help](#View_Help)
```cmake
cmake --help[-<topic>]
```

## 描述
cmake运行文件是CMake(一种跨平台生成构建系统)的命令行交互工具，上面的[概要](#Synopsis)列举该工具如下面描述的各种操作  

使用Cmake[生成项目构建系统](#Generate_a_Project_Buildsystem)，可使用cmake [build一个项目](#Build_a_Project)，[install一个项目](#Install_a_Project)或者直接运行构建工具（make），或者查看[帮助文档](#View_Help)    

其他操作旨在让[cmake语言](./cmake-language.7.md)脚本支持他们的构建集合  

需要可视操作，可以使用[ccmake](./ccmake.1.md)和[cmake-gui](./cmake-gui.1.md)代替cmake，[ctest](ctest.1.md)和[cpack](cpack.1.md)用于测试和打包  

需要查看更多信息和文档，可参考[see also](#See_Also)

## CMake构建系统

构建系统描述了如何使用构建工具从源码生成可运行或者库文件(eg:构建系统可能是为了make工具使用MakeFile或者IDE的项目文件)。 为了避免维护多个这样的构建系统，项目可以使用CMake语言编写的文件描述其构建系统。cmake通过这些文件为每个用户生成项目的本地首选构建系统  

使用CMake生成构建系统，必须指定以下内容：
* Source Tree  
使用[cmake-language(7)](./cmake-language.7.md)手册中描述的文件指定其构建系统的项目中包含源文件的顶级目录，已最顶层的CMakeLists.txt文件开始， 这些文件指定了构建目标及其依赖关系，如[cmake-buildsystem（7）](./cmake-buildsystem.7.md)手册中所述。

* Build Tree  
用于存储构建系统文件和构建输出工件（例如可执行文件和库）的顶级目录。CMake将目录标识为构建树并存储持久性信息，例如构建系统配置选项。写入CMakeCache.txt文件。    
要维护原始源树，请使用单独的专用构建树执行源外构建。 不鼓励使用构建树与源树位于同一目录中。

* Generator  
选择了生成的构建系统。 有关Generator的文档，请参见[cmake-generators（7）](./cmake-generators.7.md)手册。 运行cmake --help以查看本地可用的生成器列表。 （可选）使用下面的-G选项指定生成器，或者只接受当前平台的默认CMake选择。
当使用[命令行构建工具生成器](./cmake-generators.7.md)时，CMake期望已在shell中配置编译器工具链所需的环境。 使用[IDE构建工具生成器](./cmake-generators.7.md)时，则不需要特定的环境。  


## <h2 id = "Generate_a_Project_Buildsystem">生成构建系统</h2>
使用以下命令签名运行CMake以指定源树和构建树并生成构建系统：

* ```cmake [<options>] <path-to-source>```  
使用当前工作目录作为build tree，使用```<path-to-source>```作为源树。 指定的路径可以是当前工作目录的绝对路径或相对路径。 源树必须包含CMakeLists.txt文件，并且不得包含CMakeCache.txt文件，因为标识现有的构建树。 例如：
```sh
$ mkdir build ; cd build
$ cmake ../src
```

* ```cmake [<options>] <path-to-existing-build>```  
使用```<path-to-existing-build>```作为构建树，并从其CMakeCache.txt文件加载源树的路径，该文件必须已由上一次运行的CMake生成。 指定的路径可以是当前工作目录的绝对路径或相对路径。 例如：  
```sh
$ cd build
$ cmake .
```

* ```cmake [<options>] -S <path-to-source> -B <path-to-build>```  
使用```<path-to-build>```作为构建树，使用```<path-to-source>```作为源树。 指定的路径可以是绝对路径或相对于当前工作目录。 源树必须包含CMakeLists.txt文件。 如果构建树尚不存在，则会自动创建构建树。 例如：  
```sh
$ cmake -S src -B build
```
上面集中情况下 ```<options>``` 可能使多个或者0个下面的[选项](#Options)。  
在生成构建系统之后，可以使用相应的本机构建工具来构建项目。 例如，在使用[Unix Makefiles](../generator/Unix_Makefiles.md)生成器之后，可以直接运行make：  
```sh
$ make
$ make install
```
或者，可以通过自动选择和调用适当的本机构建工具来使用cmake来[构建项目](#Build_a_Project)。
## <h2 id = "Options">选项 </h2>
* ```-S <path-to-source>```  
要构建的CMake项目的根目录的路径。 
* ```-B <path-to-build>```  
CMake将用作构建目录的根目录的路径，如果目录不存在，CMake将会创建。  
* ```-C <initial-cache>```  
预加载脚本以填充缓存。  
当CMake首次在空的构建树中运行时，它会创建一个CMakeCache.txt文件，项目可自定义设置填充它。 此选项可用于指定在第一次通过项目的CMake列表文件之前从中加载缓存条目的文件。 加载的参数优先于项目的默认值。 该文件通过包含使用CACHE选项的set（）命令的CMake脚本设置，而不是缓存格式文件。
* ```-D <var>:<type>=<value>, -D <var>=<value>```  
创建或更新CMake 缓存条目。
当CMake首次在空构建树中运行时，它会创建一个CMakeCache.txt文件，项目的可自定义设置填充它。 此选项可用于指定优先于项目默认值的设置。 可以根据需要针对尽可能多的使用缓存条目  
如果设置了```<type>```部分，则它必须是set（）命令文档为其CACHE签名指定的类型之一。 如果省略了```<type>```部分，则如果条目如果不存在，则创建没有类型的条目。 如果项目中的命令将类型设置为PATH或FILEPATH，则```<value>```将转换为绝对路径。  
此选项也可以作为单个参数给出```-D<var>:<type>=<value>``` or ````-D<var>=<value>``` 
* ```-U <globbing_expr>```  
从CMake CACHE中删除匹配的条目。  
此选项可用于从CMakeCache.txt文件中删除一个或多个变量，支持使用*和？表示表达式。 可以根据需要针对尽可能多的CACHE条目重复该选项。  
小心使用，可以使您的CMakeCache.txt无法正常工作。
* ```-G <generator-name>```  
指定构建系统生成器。  
CMake可能在某些平台上支持多个本机构建系统。 生成器负责生成特定的构建系统。 可能的生成器名称在[cmake-generators（7）](./cmake-generators.7.md)手册中指定。  
如果未指定，CMake将检查[CMAKE_GENERATOR](../envvar/CMAKE_GENERATOR.md)环境变量，否则将回退到内置默认选择。  
* ```-T <toolset-spec>```  
如果支持,设置生成器的工具集规范。  
一些CMake生成器支持工具集规范，以告诉本机构建系统如何选择编译器。 有关详细信息，请参阅[CMAKE_GENERATOR_TOOLSET](../variable/CMAKE_GENERATOR_TOOLSET.md)变量。  
* ```-A <platform-name>```
如果生成器支持，请指定平台名称。  
一些CMake生成器支持为本机构建系统提供的平台名称，以选择编译器或SDK。 有关详细信息，请参阅[CMAKE_GENERATOR_PLATFORM](../variable/CMAKE_GENERATOR_PLATFORM.md)变量。  
* ```-Wno-dev```
关闭开发人员警告。  
禁止针对CMakeLists.txt文件的作者的警告。 默认情况下，这也会关闭弃用警告。
* ```-Wdev```  
启用开发人员警告。  
启用适用于CMakeLists.txt文件作者的警告。 默认情况下，这也会启用弃用警告。
* ```-Werror=dev```  
使开发人员警告变为错误。  
发出针对CMakeLists.txt文件作者错误的警告。 默认情况下，这也会将已弃用的警告设置为错误。  
* ```-Wno-error=dev```  
使开发人员警告不变为错误。  
针对CMakeLists.txt文件的作者发出的警告不是错误。 默认情况下，这也会关闭将已弃用的警告作为错误。
* ```-Wdeprecated```  
启用已弃用的功能警告。  
启用警告以使用已弃用的功能，这些功能适用于CMakeLists.txt文件的作者。
* ```-Wno-deprecated```  
禁止弃用功能警告。  
禁止使用已弃用的功能的警告，这些功能适用于CMakeLists.txt文件的作者。
* ```-Werror=deprecated```  
使弃用的宏和函数警告错误。  
对使用不推荐使用的宏和函数发出警告，这些宏和函数适用于CMakeLists.txt文件的作者，错误
* ```-Wno-error=deprecated```  
弃用的宏和函数警告不是错误。  
对使用不推荐使用的宏和函数发出警告，这些宏和函数适用于CMakeLists.txt文件的作者，而不是错误。
* ```-L[A][H]```  
列出非高级缓存变量。  
cmake运行时候列出没有被标记为INTERNAL或者ADVANCED的缓存变量。 这将有效地显示当前的CMake设置，然后可以使用-D选项进行更改。 更改某些变量可能会导致创建更多变量。 如果指定了A，则它还将显示高级变量。 如果指定了H，它还将显示每个变量的帮助..
* ```-N```  
仅查看模式。  
仅加载缓存。 实际上不要运行configure和生成步骤。
* ```--graphviz=[file]```  
生成依赖关系的graphviz，有关更多信息，请参阅[CMakeGraphVizOptions](../module/CMakeGraphVizOptions.md)。  
生成graphviz输入文件，该文件将包含项目中的所有库和可执行依赖项。 有关更多详细信息，请参阅[CMakeGraphVizOptions](../module/CMakeGraphVizOptions.md)的文档。
* ```--system-information [file]```  
转储有关此系统的信息。  
转储有关当前系统的各种信息。 如果从CMake项目的二叉树顶部运行，它将转储其他信息，如缓存，日志文件等。
* ```--loglevel=<error|warning|notice|status|verbose|debug|trace>```  
设置日志级别。    
[message](../command/message.md)（）命令仅输出指定日志级别或更高级别的消息。 默认日志级别为status。
* ```--debug-trycompile```  
不要删除[try_compile](../command/try_compile.md)（）构建树。 仅在一次[try_compile](../command/try_compile.md)（）上有用。    
不要删除[try_compile](../command/try_compile.md)（）调用创建的文件和目录。 这在调试失败的try_compiles时很有用。 然而，它可能会改变try-compiles的结果，因为之前的try-compile中的旧垃圾可能导致不同的测试无法正确通过或失败。 此选项最好一次用于一次try-compile，并且仅在调试时使用。
* ```--debug-output```  
将cmake置于调试模式。   
在cmake运行期间打印额外信息，如带有[message](../command/message.md)调用的堆栈跟踪。
* ```--trace```  
将cmake置于跟踪模式。      
打印所有调用的跟踪记录。
* ```--trace-expand```  
将cmake置于跟踪模式。  
类似--trace，但扩展了变量。
* ```--trace-source=<file>```  
将cmake置于跟踪模式，但仅输出指定文件的行。  
允许多个选项。
* ```--warn-uninitialized```  
警告未初始化的值。  
使用未初始化的变量时打印警告。
* ```--warn-unused-vars```  
警告未使用的变量。  
查找已声明或已设置但未使用的变量。
* ```--no-warn-unused-cli```  
不要警告命令行选项。  
找不到在命令行上声明但未使用的变量。
* ```--check-system-vars```  
查找系统文件中变量使用的问题。  
通常，仅在[CMAKE_SOURCE_DIR](../variable/CMAKE_SOURCE_DIR.md)和[CMAKE_BINARY_DIR](../variable/CMAKE_BINARY_DIR.md)中搜索未使用和未初始化的变量。 该标志告诉CMake也警告其他文件。


## <h2 id = "Build_a_Project">build项目</h2>
CMake提供命令行来构建已生成构建结构的项目  
```sh
cmake --build <dir> [<options>] [-- <build-tool-options>]
```
该命令将使用以下选项： 
* ```--build <dir>```  
要构建的项目二进制目录。 必需的且必须第一个参数  
* ```--parallel [<jobs>], -j [<jobs>]```  
构建时使用的最大并发进程数。 如果省略```<jobs>```，则使用本机构建工具的默认编号。  
如果设置了[CMAKE_BUILD_PARALLEL_LEVEL](../envvar/CMAKE_BUILD_PARALLEL_LEVEL.md)环境变量，则用改值，否则指定默认并行级别。  
一些本机构建工具始终并行构建。 ```<jobs>``值为1的使用可用于限制单个作业。
* ```--target <tgt>..., -t <tgt>..```  
构建```<tgt>```而不是默认目标。 可以多次指定。 
* ```--config <cfg>```  
对于多配置工具，请选择配置```<cfg>```。 
* ```--clean-firs```  
先构建目标清理，然后构建。 （要仅清理，请使用--target clean。）  
* ```--use-stderr```  
忽略。 行为在CMake> = 3.0中是默认的。
* ```--verbose, -v```  
启用详细输出 - 如果支持 - 包括要执行的构建命令。  
如果设置了[VERBOSE](../envvar/VERBOSE.md)环境变量或[CMAKE_VERBOSE_MAKEFILE](../envvar/CMAKE_VERBOSE_MAKEFILE.md)缓存变量，则可以省略此选项。
* ```--```  
将选项传递给本机工具。  
运行cmake --build并且没有其他选项（参数）则显示帮助。
## <h2 id = "Install_a_Project">安装项目</h2>
CMake提供命令行来安装已生成的项目  
```sh
cmake --install <dir> [<options>]
```
可以在构建项目不使用生成的构建系统或本机构建工具的情况下安装。可接受选项
* ```--install <dir>```  
项目二进制安装目录。 必需的且必须第一个参数
* ```--config <cfg>```  
对于多配置工具，请选择配置```<cfg>```。
* ```--component <comp>```  
基于组件的安装。 仅安装组件```<comp>```。
* ```--prefix <prefix>```  
安装前缀[CMAKE_INSTALL_PREFIX](../variable/CMAKE_INSTALL_PREFIX.md)。
* ```--strip```  
通过设置[CMAKE_INSTALL_DO_STRIP](not foud)在安装前剥离
* ```-v, --verbose```  
启用详细输出。  
如果设置了[VERBOSE](../envvar/VERBOSE.md)环境变量，则可以省略此选项。

运行cmake --install并且没有其他选项（参数）则显示帮助。

## <h2 id = "Open_a_Project">打开项目</h2>
```sh
cmake --open <dir>
```
在关联的应用程序中打开生成的项目。 这仅由一些生成器支持。
## <h2 id = "Run_a_Script">运行脚本</h2>
```sh
cmake [{-D <var>=<value>}...] -P <cmake-script-file>
```
将```<cmake-script-file>```文件处理为以CMake语言编写的脚本。 不执行配置或生成步骤，并且不修改缓存。 如果使用-D定义变量，则必须在-P参数之前完成。
## <h2 id = "Run_a_Command_Line_Tool">运行命令工具 </h2>
CMake内置以下命令行工具 
```sh 
cmake -E <command> [<options>]
```
运行cmake -E或cmake -E help以显示帮助。 可用的命令是：
* ```capabilities```  
以JSON格式报告cmake功能。 输出是一个JSON对象，具有以下key    
&nbsp;version    带有版本信息的JSON对象。   
&nbsp;&nbsp;string  
&nbsp;&nbsp;&nbsp;&nbsp;cmake --version显示的完整版本字符串   
&nbsp;&nbsp;major  
&nbsp;&nbsp;&nbsp;&nbsp;整数形式的主要版本号。    
&nbsp;&nbsp;minor  
&nbsp;&nbsp;&nbsp;&nbsp;整数形式的次要版本号。    
&nbsp;&nbsp;patch  
&nbsp;&nbsp;&nbsp;&nbsp;整数形式的补丁号。  
&nbsp;&nbsp;suffix  
&nbsp;&nbsp;&nbsp;&nbsp;cmake版本后缀字符串。  
&nbsp;&nbsp;isDirty  
&nbsp;&nbsp;&nbsp;&nbsp;如果cmake构建来自脏树，则设置bool。   
&nbsp;generators  可用的生成器的列表。 每个生成器都是一个JSON对象，具有以下key  
&nbsp;&nbsp;name  
&nbsp;&nbsp;&nbsp;&nbsp;包含生成器名称的字符串。    
&nbsp;&nbsp;toolsetSupport  
&nbsp;&nbsp;&nbsp;&nbsp;如果生成器支持工具集，则为true，否则为false。    
&nbsp;&nbsp;platformSupport   
&nbsp;&nbsp;&nbsp;&nbsp;如果生成器支持平台则为true，否则为false。  
&nbsp;&nbsp;extraGenerators  
&nbsp;&nbsp;&nbsp;&nbsp;包含与生成器兼容的所有额外生成器的字符串列表。  
&nbsp;fileApi  [cmake-file-api](./cmake-file-api.7.md)（7）可用时存在的可选成员。 该值是一个具有一个成员的JSON对象：   
&nbsp;&nbsp;requests  包含零个或多个受支持的file-api请求的JSON数组。 每个请求都是一个带有成员的JSON对象：  
&nbsp;&nbsp;&nbsp;&nbsp;kind  指定一个受支持的对象类型。    
&nbsp;&nbsp;&nbsp;&nbsp;version 一个JSON数组，其元素都是一个JSON对象，包含指定非负整数版本组件的主要成员和次要成员。    
&nbsp;serverMode  如果cmake支持服务器模式，则为true，否则为false。   
* ```chdir <dir> <cmd> [<arg>...]```  
更改当前工作目录并运行命令。  
* ```compare_files [--ignore-eol] <file1> <file2>```  
检查```<file1>```是否与```<file2>```相同。 如果文件相同，则返回0，否则返回1.-ignore-eol选项意味着按行比较并忽略LF / CRLF差异。
* ```copy <file>... <destination>```  
将文件复制到```<destination>```（文件或目录）。 如果指定了多个文件，则```<destination>```必须是目录，并且必须存在。 不支持通配符。 复制确实遵循符号链接。 这意味着它不会复制符号链接，而是指向它指向的文件或目录。
* ```copy_directory <dir>... <destination>```  
将目录复制到```<destination>```目录。 如果```<destination>```目录不存在，则将创建该目录。 copy_directory确实遵循符号链接。    
* ```copy_if_different <file>... <destination>```  
如果文件已更改，则将文件复制到```<destination>```（文件或目录）。 如果指定了多个文件，则```<destination>```必须是目录，并且必须存在。 copy_if_different确实遵循符号链接。
* ```echo [<string>...]```  
echo  
* ```echo_append [<string>...]```  
将参数显示为文本并且不会显示新行（和上个命令比起来最后是否多了空的一行）。 
* ```env [--unset=NAME]... [NAME=VALUE]... COMMAND [ARG]...```  
在修改后的环境中运行命令。  
* ```environment```  
显示当前环境变量。  
* ```make_directory <dir>...```  
创建```<dir>```目录。 如有必要，也可以创建父目录。 如果目录已存在，则将以静默方式忽略。   
* ```md5sum <file>...```  
以md5sum兼容格式创建文件的MD5校验和：  
```sh
351abe79cd3800b38cdfb25d45015a15  file1.txt
052f86c15bbde68af55c7f7b340ab639  file2.txt
```
* ```sha1sum <file>...```  
以sha1sum兼容格式创建文件的SHA1校验和：
```sh
4bb7932a29e6f73c97bb9272f2bdc393122f86e0  file1.txt
1df4c8f318665f9a5f2ed38f55adadb7ef9f559c  file2.txt
```
* ```sha224sum <file>...```  
以sha224sum兼容格式创建SHA224校验和文件
```sh  
b9b9346bc8437bbda630b0b7ddfc5ea9ca157546dbbf4c613192f930  file1.txt
6dfbe55f4d2edc5fe5c9197bca51ceaaf824e48eba0cc453088aee24  file2.txt
```
* ```sha256sum <file>...```  
以sha256sum兼容格式创建SHA256校验和文件：
```sh
76713b23615d31680afeb0e9efe94d47d3d4229191198bb46d7485f9cb191acc  file1.txt
15b682ead6c12dedb1baf91231e1e89cfc7974b3787c1e2e01b986bffadae0ea  file2.txt
```
* ```sha384sum <file>...```  
以sha384sum兼容格式创建SHA384校验和文件：
```sh
acc049fedc091a22f5f2ce39a43b9057fd93c910e9afd76a6411a28a8f2b8a12c73d7129e292f94fc0329c309df49434  file1.txt
668ddeb108710d271ee21c0f3acbd6a7517e2b78f9181c6a2ff3b8943af92b0195dcb7cce48aa3e17893173c0a39e23d  file2.txt
``` 
* ```sha512sum <file>...```  
以sha512sum兼容格式创建SHA512校验和文件：
```sh
2a78d7a6c5328cfb1467c63beac8ff21794213901eaadafd48e7800289afbc08e5fb3e86aa31116c945ee3d7bf2a6194489ec6101051083d1108defc8e1dba89  file1.txt
7a0b54896fe5e70cca6dd643ad6f672614b189bf26f8153061c4d219474b05dad08c4e729af9f4b009f1a1a280cb625454bf587c690f4617c27e3aebdf3b7a2d  file2.txt
``` 
* ```remove [-f] <file>...```  
删除文件。 如果任何列出的文件已不存在，则该命令将返回非零退出代码，但不会记录任何消息。 -f选项改变行为以在这种情况下返回零退出代码（即成功）。 删除不遵循符号链接。 这意味着它只删除符号链接而不删除它指向的文件。
* ```remove_directory <dir>...```  
删除```<dir>```目录及其内容。 如果目录不存在，它将被静默忽略。  
* ```rename <oldname> <newname>```  
重命名文件或目录（在一个卷上）。 如果已存在具有```<newname>```名称的文件，则将以静默方式替换该文件。 
* ```server```  
启动[cmake-server（7）](./cmake-server.7.md)模式。 
* ```sleep <number>...```  
睡眠给定的秒数。 
* ```tar [cxt][vf][zjJ] file.tar [<options>] [--] [<pathname>...]```  
创建或提取tar或zip存档。 选项包括：  
```c```  创建包含指定文件的新存档。 如果使用，```<pathname>``` ...参数是必需的。  
```x```  从存档中提取到磁盘。 ```<pathname> ```...参数可用于仅提取选定的文件或目录。 提取所选文件或目录时，必须提供其确切名称，包括路径（由列表（-t）打印）。  
```t```  列出存档内容。 ```<pathname>``` ...参数可用于仅列出选定的文件或目录。  
```v```  产生详细输出。  
```z```  使用gzip压缩生成的存档。  
```j```  使用bzip2压缩生成的存档。  
```J```  使用XZ压缩生成的存档。  
```--zstd```  使用Zstandard压缩生成的存档。  
```--files-from=<file>```  从给定文件中读取文件名，每行一个。 空行被忽略。 行可能无法启动 - 除了--add-file = ```<name>```以添加名称以 - 开头的文件。  
```--format=<format>```  指定要创建的存档的格式。 支持的格式有：7zip，gnutar，pax，paxr（受限制的pax，默认）和zip。  
```--mtime=<date>```  指定tarball条目中记录的修改时间。  
```--```  停止解释选项并将所有剩余参数视为文件名，即使它们以 - 开头。  

* ```time <command> [<args>...]```  
运行命令并显示已用时间。   
* ```touch <file>...```  
如果文件不存在，则创建```<file>```。 如果```<file>```存在，则它正在更改```<file>```访问和修改时间。  
* ```touch_nocreate <file>...```  
修改文件（如果存在）但不创建它。 如果文件不存在，则会以静默方式忽略。   
* ```create_symlink <old> <new>```  
创建符号链接```<new>```命名```<old>```。 
> 创建```<new>```符号链接的路径必须事先存在。
## <h2 id = "Windows_specific_Command_Line_Tools">windows特定工具 </h2>
以下cmake -E命令仅在Windows上可用：
* ```delete_regv <key>```  
删除Windows注册表值。    
* ```env_vs8_wince <sdkname>```  
显示批处理文件，该文件为VS2005中安装的Windows CE SDK设置环境。    
* ```env_vs9_wince <sdkname>```  
显示批处理文件，该文件为VS2008中安装的Windows CE SDK设置环境。  
* ```write_regv <key> <value>```  
写Windows注册表值。  

## <h2 id = "Run_the_Find_Package_Tool">运行findPackage工具 </h2>
CMake为基于Makefile的项目提供了一个类似pkg-config的帮助程序：
```sh
cmake --find-package [<options>]
```
它使用[find_package（）](../command/find_package.md)搜索包，并将生成的标志打印到stdout。 可以使用它来代替pkg-config来查找基于Makefile的纯项目或基于autoconf的项目中的已安装库（通过share/aclocal/cmake.m4）。
> 由于某些技术限制，他的模式得不到很好的支持。 它保持兼容性，但不应在新项目中使用。
## <h2 id = "View_Help">help </h2>
要从CMake文档打印帮助
```sh
cmake --help[-<topic>]
```
可用选项：
* ```--help,-help,-usage,-h,-H,/?```   
打印帮助信息并退出。  
用法描述了基本的命令行界面及其选项。  
* ```--version,-version,/V [<f>]```   
显示程序名称/版本标题并退出。  
如果指定了文件，则会将版本写入其中。 如果指定输出路径，帮助将打印到命名的```<f>``` ile。  
* ```--help-full [<f>]```   
打印所有帮助手册并退出。  
所有手册均以可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>``` ile。 
* ```--help-manual <man> [<f>]```   
打印一份帮助手册并退出。  
指定的手册以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>``` ile。 
* ```--help-manual-list [<f>]```   
列出帮助手册并退出。  
该列表包含所有可通过使用--help-manual选项后跟手册名称获取帮助的手册。 如果指定输出路径，帮助将打印到命名的```<f>``` ile。 
* ```--help-command <cmd> [<f>]```   
打印一个命令的帮助并退出。  
```<cmd>```的[cmake-commands（7）](./cmake-commands.7.md)手动输入以人类可读的文本格式打印。  如果指定输出路径，帮助将打印到命名的```<f>``` ile。  
* ```--help-commands [<f>]```   
打印cmake-commands手册并退出。
[cmake-commands（7）](./cmake-commands.7.md)手册以人类可读的文本格式打印。  如果指定输出路径，帮助将打印到命名的```<f>``` ile。 
* ```--help-module <mod> [<f>]```   
打印一个模块的帮助并退出。  
```<mod>```的[cmake-commands（7）](./cmake-commands.7.md)手动输入以人类可读的文本格式打印。如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-module-list [<f>]```   
列出提供帮助的模块并退出。  
该列表包含可以使用--help-module选项后跟模块名称获取帮助的所有模块。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-modules [<f>]```   
打印cmake-modules手册并退出。
[cmake-commands（7）](./cmake-commands.7.md)手册以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-policy <cmp> [<f>]```   
打印一个策略的帮助并退出。
```<cmp>```的[cmake-policies（7）](./cmake-policies.7.md)手册条目以人类可读的文本格式打印。如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-policy-list [<f>]```   
列出可获得帮助的政策并退出。
该列表包含可以使用--help-policy选项后跟策略名称获取帮助的所有策略。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-policies [<f>]```   
打印cmake-policies手册并退出。
[cmake-policies（7）](./cmake-policies.7.md)手册以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-property <prop> [<f>]```   
打印一个属性的帮助并退出。
```<prop>```的[cmake-properties（7）](./cmake-properties.7.md)手册条目以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-property-list [<f>]```   
列出可用帮助的属性并退出。
该列表包含可以使用--help-property选项后跟属性名称获取帮助的所有属性。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-properties [<f>]```   
打印cmake-properties手册并退出。  
[cmake-properties（7）](./cmake-properties.7.md)手册以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-variable <var> [<f>]```   
打印一个变量的帮助并退出。
```<var>```的[cmake-variables（7）](./cmake-variables.7.md)手动条目以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。  
* ```--help-variable-list [<f>]```   
列出变量并提供帮助并退出。  
该列表包含可以通过使用--help-variable选项后跟变量名称获得帮助的所有变量。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。   
* ```--help-variables [<f>]```   
打印cmake-variables手动并退出。
[cmake-variables（7）](./cmake-variables.7.md)手册以人类可读的文本格式打印。 如果指定输出路径，帮助将打印到命名的```<f>`` ile。   
## <h2 id = "See_Also">See Also</h2>

以下资源可用于使用CMake获取帮助：  
* Home Page  
https://cmake.org  
了解CMake的主要出发点。
* Online Documentation and Community Resources  
https://cmake.org/documentation  
可在此网页上找到可用文档和社区资源的链接。
* Mailing List  
https://cmake.org/mailing-lists  
有关使用CMake的帮助和讨论，请发送电子邮件至cmake@cmake.org。 该列表仅限会员，但可以在CMake网页上注册。 在将问题发布到列表之前，请先阅读https://cmake.org上的完整文档。