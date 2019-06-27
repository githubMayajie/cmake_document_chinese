  

# FindQt  
Searches for all installed versions of Qt3 or Qt4.  

This module cannot handle Qt5 or any later versions.
For those, see cmake-qt(7).  

This module exists for the find_package() command only if
policy CMP0084 is not set to NEW.  

This module should only be used if your project can work with multiple
versions of Qt.  If not, you should just directly use FindQt4 or
FindQt3.  If multiple versions of Qt are found on the machine, then
The user must set the option DESIRED_QT_VERSION to the version they
want to use.  If only one version of qt is found on the machine, then
the DESIRED_QT_VERSION is set to that version and the matching FindQt3
or FindQt4 module is included.  Once the user sets DESIRED_QT_VERSION,
then the FindQt3 or FindQt4 module is included.  

QT_REQUIRED if this is set to TRUE then if CMake can
            not find Qt4 or Qt3 an error is raised
            and a message is sent to the user.

  

DESIRED_QT_VERSION OPTION is created
QT4_INSTALLED is set to TRUE if qt4 is found.
QT3_INSTALLED is set to TRUE if qt3 is found.

  

