  

# ASM```<DIALECT>```  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Preferred executable for compiling a specific dialect of assembly language
files. ASM```<DIALECT>``` can be ASM, ASM_NASM (Netwide Assembler),
ASM_MASM (Microsoft Assembler) or ASM-ATT (Assembler AT&T).
Will only be used by CMake on the first configuration to determine
ASM```<DIALECT>``` compiler, after which the value for ASM```<DIALECT>``` is stored
in the cache as
CMAKE_ASM```<DIALECT>```_COMPILER. For subsequent
configuration runs, the environment variable will be ignored in favor of
CMAKE_ASM```<DIALECT>```_COMPILER.  

