  

# UseEcos  
This module defines variables and macros required to build eCos application.  

This file contains the following macros:
ECOS_ADD_INCLUDE_DIRECTORIES() - add the eCos include dirs
ECOS_ADD_EXECUTABLE(name source1 бн  sourceN ) - create an eCos
executable ECOS_ADJUST_DIRECTORY(VAR source1 бн  sourceN ) - adjusts
the path of the source files and puts the result into VAR  

Macros for selecting the toolchain: ECOS_USE_ARM_ELF_TOOLS() - enable
the ARM ELF toolchain for the directory where it is called
ECOS_USE_I386_ELF_TOOLS() - enable the i386 ELF toolchain for the
directory where it is called ECOS_USE_PPC_EABI_TOOLS() - enable the
PowerPC toolchain for the directory where it is called  

It contains the following variables: ECOS_DEFINITIONS
ECOSCONFIG_EXECUTABLE ECOS_CONFIG_FILE - defaults to ecos.ecc, if your
eCos configuration file has a different name, adjust this variable for
internal use only:  

ECOS_ADD_TARGET_LIB

  

