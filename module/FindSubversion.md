  

# FindSubversion  
Extract information from a subversion working copy  

The module defines the following variables:  

Subversion_SVN_EXECUTABLE - path to svn command line client
Subversion_VERSION_SVN - version of svn command line client
Subversion_FOUND - true if the command line client was found
SUBVERSION_FOUND - same as Subversion_FOUND, set for compatibility reasons

  

The minimum required version of Subversion can be specified using the
standard syntax, e.g. find_package(Subversion 1.4).  

If the command line client executable is found two macros are defined:  

Subversion_WC_INFO(```<dir>``` ```<var-prefix>``` [IGNORE_SVN_FAILURE])
Subversion_WC_LOG(```<dir>``` ```<var-prefix>```)

  

Subversion_WC_INFO extracts information of a subversion working copy at a
given location.  This macro defines the following variables if running
Subversion¡¯s info command on ```<dir>``` succeeds; otherwise a
SEND_ERROR message is generated. The error can be ignored by providing the
IGNORE_SVN_FAILURE option, which causes these variables to remain
undefined.  

```<var-prefix>```_WC_URL - url of the repository (at ```<dir>```)
```<var-prefix>```_WC_ROOT - root url of the repository
```<var-prefix>```_WC_REVISION - current revision
```<var-prefix>```_WC_LAST_CHANGED_AUTHOR - author of last commit
```<var-prefix>```_WC_LAST_CHANGED_DATE - date of last commit
```<var-prefix>```_WC_LAST_CHANGED_REV - revision of last commit
```<var-prefix>```_WC_INFO - output of command `svn info ```<dir>```'

  

Subversion_WC_LOG retrieves the log message of the base revision of a
subversion working copy at a given location.  This macro defines the variable:  

```<var-prefix>```_LAST_CHANGED_LOG - last log of base revision

  

Example usage:  

find_package(Subversion)
if(SUBVERSION_FOUND)
  Subversion_WC_INFO(${PROJECT_SOURCE_DIR} Project)
  message("Current revision is ${Project_WC_REVISION}")
  Subversion_WC_LOG(${PROJECT_SOURCE_DIR} Project)
  message("Last changed log is ${Project_LAST_CHANGED_LOG}")
endif()

  

