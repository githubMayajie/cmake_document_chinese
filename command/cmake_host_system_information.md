# cmake_host_system_information  

查询系统特定信息。

```cmake
cmake_host_system_information(RESULT <variable> QUERY <key> ...)
```

  
查询运行cmake的系统的系统信息。可以提供一个或多个```<key>```来选择信息查询。 查询值列表存储在```<variable>```中。

```<key>``` 可以为以下值:  
Key 					|                    Description
--- | ---
NUMBER_OF_LOGICAL_CORES 			|		逻辑核心数  
NUMBER_OF_PHYSICAL_CORES 			|		物理核心数  
HOSTNAME 					        |        主机名
FQDN 					            |        完全合格的域名
TOTAL_VIRTUAL_MEMORY 				|	    虚拟内存总量 in MiB [1]
AVAILABLE_VIRTUAL_MEMORY 			|		可用的虚拟内存 in MiB [1]
TOTAL_PHYSICAL_MEMORY 				|	    物理内存总量 in MiB [1]
AVAILABLE_PHYSICAL_MEMORY 			|		可用的物理内存 in MiB [1]
IS_64BIT 					        |        处理器是64位
HAS_FPU 					        |        处理器有浮点单元
HAS_MMX 					        |        处理器支持MMX指令
HAS_MMX_PLUS 					    |        处理器支持Ext. MMX指令
HAS_SSE 					        |        处理器支持SSE指令
HAS_SSE2 					        |        处理器支持SSE2指令
HAS_SSE_FP 					        |        处理器支持SSE FP指令
HAS_SSE_MMX 					    |        处理器支持SSE MMX指令
HAS_AMD_3DNOW 					    |        处理器支持3DNOW指令
HAS_AMD_3DNOW_PLUS 					|        处理器支持3DNOW|指令
HAS_IA64 					        |        IA64处理器模拟x86
HAS_SERIAL_NUMBER 					|        处理器有序列号
PROCESSOR_SERIAL_NUMBER 			|		处理器序列号
PROCESSOR_NAME 					    |        人类可读处理器名称
PROCESSOR_DESCRIPTION 				|	    人类可读的完整处理器描述
OS_NAME 					        |        查看[CMAKE_HOST_SYSTEM_NAME](../variable/CMAKE_HOST_SYSTEM_NAME.md)
OS_RELEASE 					        |        OS子类型，例如 在Windows Professional上
OS_VERSION 					        |        操作系统Build ID
OS_PLATFORM 					    +        查看[CMAKE_HOST_SYSTEM_PROCESSOR](../variable/CMAKE_HOST_SYSTEM_PROCESSOR.md)


Footnotes  
[1](1, 2, 3, 4) 1 MiB (mebibyte) 等于 1024x1024 bytes.

  

