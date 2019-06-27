  

# GNUInstallDirs  
Define GNU standard installation directories  

Provides install directory variables as defined by the
GNU Coding Standards.  


Result Variables
Inclusion of this module defines the following variables:
CMAKE_INSTALL_```<dir>```

Destination for files of a given type.  This value may be passed to
the DESTINATION options of install() commands for the
corresponding file type.
CMAKE_INSTALL_FULL_```<dir>```

The absolute path generated from the corresponding CMAKE_INSTALL_```<dir>```
value.  If the value is not already an absolute path, an absolute path
is constructed typically by prepending the value of the
CMAKE_INSTALL_PREFIX variable.  However, there are some
special cases as documented below.
where ```<dir>``` is one of:

BINDIR
user executables (bin)
SBINDIR
system admin executables (sbin)
LIBEXECDIR
program executables (libexec)
SYSCONFDIR
read-only single-machine data (etc)
SHAREDSTATEDIR
modifiable architecture-independent data (com)
LOCALSTATEDIR
modifiable single-machine data (var)
RUNSTATEDIR
run-time variable data (LOCALSTATEDIR/run)
LIBDIR
object code libraries (lib or lib64
or lib/```<multiarch-tuple>``` on Debian)
INCLUDEDIR
C header files (include)
OLDINCLUDEDIR
C header files for non-gcc (/usr/include)
DATAROOTDIR
read-only architecture-independent data root (share)
DATADIR
read-only architecture-independent data (DATAROOTDIR)
INFODIR
info documentation (DATAROOTDIR/info)
LOCALEDIR
locale-dependent data (DATAROOTDIR/locale)
MANDIR
man documentation (DATAROOTDIR/man)
DOCDIR
documentation root (DATAROOTDIR/doc/PROJECT_NAME)

If the includer does not define a value the above-shown default will be
used and the value will appear in the cache for editing by the user.
  


Special Cases
The following values of CMAKE_INSTALL_PREFIX are special:
/

For ```<dir>``` other than the SYSCONFDIR, LOCALSTATEDIR and
RUNSTATEDIR, the value of CMAKE_INSTALL_```<dir>``` is prefixed
with usr/ if it is not user-specified as an absolute path.
For example, the INCLUDEDIR value include becomes usr/include.
This is required by the GNU Coding Standards, which state:

When building the complete GNU system, the prefix will be empty
and /usr will be a symbolic link to /.

/usr

For ```<dir>``` equal to SYSCONFDIR, LOCALSTATEDIR or
RUNSTATEDIR, the CMAKE_INSTALL_FULL_```<dir>``` is computed by
prepending just / to the value of CMAKE_INSTALL_```<dir>```
if it is not user-specified as an absolute path.
For example, the SYSCONFDIR value etc becomes /etc.
This is required by the GNU Coding Standards.
/opt/...

For ```<dir>``` equal to SYSCONFDIR, LOCALSTATEDIR or
RUNSTATEDIR, the CMAKE_INSTALL_FULL_```<dir>``` is computed by
appending the prefix to the value of CMAKE_INSTALL_```<dir>```
if it is not user-specified as an absolute path.
For example, the SYSCONFDIR value etc becomes /etc/opt/....
This is defined by the Filesystem Hierarchy Standard.
  


Macros


GNUInstallDirs_get_absolute_install_dir
GNUInstallDirs_get_absolute_install_dir(absvar var)


Set the given variable absvar to the absolute path contained
within the variable var.  This is to allow the computation of an
absolute path, accounting for all the special cases documented
above.  While this macro is used to compute the various
CMAKE_INSTALL_FULL_```<dir>``` variables, it is exposed publicly to
allow users who create additional path variables to also compute
absolute paths where necessary, using the same logic.

  

