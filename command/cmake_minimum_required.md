# cmake_minimum_required  
需要运行所需要最低版本的cmake。 

```cmake
cmake_minimum_required(VERSION <min>[...<max>] [FATAL_ERROR])
```
设置项目的cmake所需的最低版本。并且更新策略设置，如下所述。  

```<min>```和可选的```<max>```是每个CMake版本的major.minor[.patch[.tweak]]格式而来，而...是字面量。

如果运行版本的CMake低于```<min>```所需版本，它将停止处理项目并报告错误。 可选的```<max>```版本（如果已指定）必须至少为```<min>```版本，并影响策略设置，如下所述。 如果运行版本的CMake早于3.12，则额外的...点将被视为版本组件分隔符，从而导致... ```<max>```部分被忽略并保留基于```<min>```的策略的3.12之前的行为。

FATAL_ERROR选项被CMake 2.6及更高版本忽略。 应该指定CMake版本2.4及更低版本失败并出现错误而不仅仅是警告。

>在调用[project()](project.md)命令之前，在顶级CMakeLists.txt文件的开头调用cmake_minimum_required()命令。 在调用可能影响其行为的其他命令之前，建立版本和策略设置非常重要。 另见策略[CMP0000](../policy/CMP0000.md)。   
>在[函数()](function.md)内调用cmake_minimum_required()会在调用时限制对函数作用域的一些影响。 这种用法不应该旨在是为了产生全局影响。

# 策略设置
cmake_minimum_required(VERSION)命令隐式调用[cmake_policy(VERSION)](cmake_policy.md)命令以指定为给定范围的CMake版本编写当前项目代码。 运行版本的CMake在```<min>```（或```<max>```，如果指定）版本或更早版本中引入的所有策略都将设置为使用NEW行为。 超过运行cmake版本的策略都不会被设置。 这有效地请求了设置CMake运行版本的首选版本，并告诉较新的CMake版本警告他们的新策略。  

当指定高于2.4的```<min>```版本时，该命令隐式调用
```cmake
cmake_policy(VERSION <min>[...<max>])
```
根据指定的版本范围设置CMake策略。 当给出```<min>``` 2.4或更低版本时，该命令会隐式调用  
```cmake
cmake_policy(VERSION 2.4[...<max>])
```
它为CMake 2.4及更低版本提供了兼容性功能。

