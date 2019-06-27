  

# FindICU  
Find the International Components for Unicode (ICU) libraries and
programs.  

This module supports multiple components.
Components can include any of: data, i18n, io, le,
lx, test, tu and uc.  

Note that on Windows data is named dt and i18n is named
in; any of the names may be used, and the appropriate
platform-specific library name will be automatically selected.  

This module reports information about the ICU installation in
several variables.  General variables:  

ICU_VERSION - ICU release version
ICU_FOUND - true if the main programs and libraries were found
ICU_LIBRARIES - component libraries to be linked
ICU_INCLUDE_DIRS - the directories containing the ICU headers

  

Imported targets:  

ICU::```<C>```

  

Where ```<C>``` is the name of an ICU component, for example
ICU::i18n.  

ICU programs are reported in:  

ICU_GENCNVAL_EXECUTABLE - path to gencnval executable
ICU_ICUINFO_EXECUTABLE - path to icuinfo executable
ICU_GENBRK_EXECUTABLE - path to genbrk executable
ICU_ICU-CONFIG_EXECUTABLE - path to icu-config executable
ICU_GENRB_EXECUTABLE - path to genrb executable
ICU_GENDICT_EXECUTABLE - path to gendict executable
ICU_DERB_EXECUTABLE - path to derb executable
ICU_PKGDATA_EXECUTABLE - path to pkgdata executable
ICU_UCONV_EXECUTABLE - path to uconv executable
ICU_GENCFU_EXECUTABLE - path to gencfu executable
ICU_MAKECONV_EXECUTABLE - path to makeconv executable
ICU_GENNORM2_EXECUTABLE - path to gennorm2 executable
ICU_GENCCODE_EXECUTABLE - path to genccode executable
ICU_GENSPREP_EXECUTABLE - path to gensprep executable
ICU_ICUPKG_EXECUTABLE - path to icupkg executable
ICU_GENCMN_EXECUTABLE - path to gencmn executable

  

ICU component libraries are reported in:  

ICU_```<C>```_FOUND - ON if component was found
ICU_```<C>```_LIBRARIES - libraries for component

  

ICU datafiles are reported in:  

ICU_MAKEFILE_INC - Makefile.inc
ICU_PKGDATA_INC - pkgdata.inc

  

Note that ```<C>``` is the uppercased name of the component.  

This module reads hints about search results from:  

ICU_ROOT - the root of the ICU installation

  

The environment variable ICU_ROOT may also be used; the
ICU_ROOT variable takes precedence.  

The following cache variables may also be set:  

ICU_```<P>```_EXECUTABLE - the path to executable ```<P>```
ICU_INCLUDE_DIR - the directory containing the ICU headers
ICU_```<C>```_LIBRARY - the library for component ```<C>```

  


Note
In most cases none of the above variables will require setting,
unless multiple ICU versions are available and a specific version
is required.
  

Other variables one may set to control this module are:  

ICU_DEBUG - Set to ON to enable debug output from FindICU.

  

