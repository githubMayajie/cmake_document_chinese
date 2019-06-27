  

# FindGettext  
Find GNU gettext tools  

This module looks for the GNU gettext tools.  This module defines the
following values:  

GETTEXT_MSGMERGE_EXECUTABLE: the full path to the msgmerge tool.
GETTEXT_MSGFMT_EXECUTABLE: the full path to the msgfmt tool.
GETTEXT_FOUND: True if gettext has been found.
GETTEXT_VERSION_STRING: the version of gettext found (since CMake 2.8.8)

  

Additionally it provides the following macros:  

GETTEXT_CREATE_TRANSLATIONS ( outputFile [ALL] file1 бн  fileN )  

This will create a target "translations" which will convert the
given input po files into the binary output mo file. If the
ALL option is used, the translations will also be created when
building the default target.

  

GETTEXT_PROCESS_POT_FILE( ```<potfile>``` [ALL] [INSTALL_DESTINATION ```<destdir>```]
LANGUAGES ```<lang1>``` ```<lang2>``` бн  )  

Process the given pot file to mo files.
If INSTALL_DESTINATION is given then automatically install rules will
be created, the language subdirectory will be taken into account
(by default use share/locale/).
If ALL is specified, the pot file is processed when building the all traget.
It creates a custom target "potfile".

  

GETTEXT_PROCESS_PO_FILES( ```<lang>``` [ALL] [INSTALL_DESTINATION ```<dir>```]
PO_FILES ```<po1>``` ```<po2>``` бн  )  

Process the given po files to mo files for the given language.
If INSTALL_DESTINATION is given then automatically install rules will
be created, the language subdirectory will be taken into account
(by default use share/locale/).
If ALL is specified, the po files are processed when building the all traget.
It creates a custom target "pofiles".

  


Note
If you wish to use the Gettext library (libintl), use FindIntl.
  

