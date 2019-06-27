  

# FindHg  
Extract information from a mercurial working copy.  

The module defines the following variables:  

HG_EXECUTABLE - path to mercurial command line client (hg)
HG_FOUND - true if the command line client was found
HG_VERSION_STRING - the version of mercurial found

  

If the command line client executable is found the following macro is defined:  

HG_WC_INFO(```<dir>``` ```<var-prefix>```)

  

Hg_WC_INFO extracts information of a mercurial working copy
at a given location.  This macro defines the following variables:  

```<var-prefix>```_WC_CHANGESET - current changeset
```<var-prefix>```_WC_REVISION - current revision

  

Example usage:  

find_package(Hg)
if(HG_FOUND)
  message("hg found: ${HG_EXECUTABLE}")
  HG_WC_INFO(${PROJECT_SOURCE_DIR} Project)
  message("Current revision is ${Project_WC_REVISION}")
  message("Current changeset is ${Project_WC_CHANGESET}")
endif()

  

