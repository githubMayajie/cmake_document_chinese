  

# FindKDE3  
Find the KDE3 include and library dirs, KDE preprocessors and define a some macros  

This module defines the following variables:  


KDE3_DEFINITIONS
compiler definitions required for compiling KDE software
KDE3_INCLUDE_DIR
the KDE include directory
KDE3_INCLUDE_DIRS
the KDE and the Qt include directory, for use with include_directories()
KDE3_LIB_DIR
the directory where the KDE libraries are installed, for use with link_directories()
QT_AND_KDECORE_LIBS
this contains both the Qt and the kdecore library
KDE3_DCOPIDL_EXECUTABLE
the dcopidl executable
KDE3_DCOPIDL2CPP_EXECUTABLE
the dcopidl2cpp executable
KDE3_KCFGC_EXECUTABLE
the kconfig_compiler executable
KDE3_FOUND
set to TRUE if all of the above has been found
  

The following user adjustable options are provided:  


KDE3_BUILD_TESTS
enable this to build KDE testcases
  

It also adds the following macros (from KDE3Macros.cmake) SRCS_VAR is
always the variable which contains the list of source files for your
application or library.  

KDE3_AUTOMOC(file1 бн  fileN)  

Call this if you want to have automatic moc file handling.
This means if you include "foo.moc" in the source file foo.cpp
a moc file for the header foo.h will be created automatically.
You can set the property SKIP_AUTOMAKE using set_source_files_properties()
to exclude some files in the list from being processed.

  

KDE3_ADD_MOC_FILES(SRCS_VAR file1 бн  fileN )  

If you don't use the KDE3_AUTOMOC() macro, for the files
listed here moc files will be created (named "foo.moc.cpp")

  

KDE3_ADD_DCOP_SKELS(SRCS_VAR header1.h бн  headerN.h )  

Use this to generate DCOP skeletions from the listed headers.

  

KDE3_ADD_DCOP_STUBS(SRCS_VAR header1.h бн  headerN.h )  

Use this to generate DCOP stubs from the listed headers.

  

KDE3_ADD_UI_FILES(SRCS_VAR file1.ui бн  fileN.ui )  

Use this to add the Qt designer ui files to your application/library.

  

KDE3_ADD_KCFG_FILES(SRCS_VAR file1.kcfgc бн  fileN.kcfgc )  

Use this to add KDE kconfig compiler files to your application/library.

  

KDE3_INSTALL_LIBTOOL_FILE(target)  

This will create and install a simple libtool file for the given target.

  

KDE3_ADD_EXECUTABLE(name file1 бн  fileN )  

Currently identical to add_executable(), may provide some advanced
features in the future.

  

KDE3_ADD_KPART(name [WITH_PREFIX] file1 бн  fileN )  

Create a KDE plugin (KPart, kioslave, etc.) from the given source files.
If WITH_PREFIX is given, the resulting plugin will have the prefix "lib",
otherwise it won't.
It creates and installs an appropriate libtool la-file.

  

KDE3_ADD_KDEINIT_EXECUTABLE(name file1 бн  fileN )  

Create a KDE application in the form of a module loadable via kdeinit.
A library named kdeinit_```<name>``` will be created and a small executable
which links to it.

  

The option KDE3_ENABLE_FINAL to enable all-in-one compilation is no
longer supported.  

Author: Alexander Neundorf ```<neundorf@kde.org>```  

