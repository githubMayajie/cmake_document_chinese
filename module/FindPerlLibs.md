  

# FindPerlLibs  
Find Perl libraries  

This module finds if PERL is installed and determines where the
include files and libraries are.  It also determines what the name of
the library is.  This code sets the following variables:  

PERLLIBS_FOUND    = True if perl.h & libperl were found
PERL_INCLUDE_PATH = path to where perl.h is found
PERL_LIBRARY      = path to libperl
PERL_EXECUTABLE   = full path to the perl binary

  

The minimum required version of Perl can be specified using the
standard syntax, e.g.  find_package(PerlLibs 6.0)  

The following variables are also available if needed
(introduced after CMake 2.6.4)

  

PERL_SITESEARCH     = path to the sitesearch install dir (-V:installsitesearch)
PERL_SITEARCH       = path to the sitelib install directory (-V:installsitearch)
PERL_SITELIB        = path to the sitelib install directory (-V:installsitelib)
PERL_VENDORARCH     = path to the vendor arch install directory (-V:installvendorarch)
PERL_VENDORLIB      = path to the vendor lib install directory (-V:installvendorlib)
PERL_ARCHLIB        = path to the core arch lib install directory (-V:archlib)
PERL_PRIVLIB        = path to the core priv lib install directory (-V:privlib)
PERL_UPDATE_ARCHLIB = path to the update arch lib install directory (-V:installarchlib)
PERL_UPDATE_PRIVLIB = path to the update priv lib install directory (-V:installprivlib)
PERL_EXTRA_C_FLAGS = Compilation flags used to build perl

  

