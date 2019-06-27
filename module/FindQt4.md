  

# FindQt4  

Finding and Using Qt4
This module can be used to find Qt4.  The most important issue is that
the Qt4 qmake is available via the system path.  This qmake is then
used to detect basically everything else.  This module defines a
number of IMPORTED targets, macros and variables.
Typical usage could be something like:
set(CMAKE_AUTOMOC ON)
set(CMAKE_INCLUDE_CURRENT_DIR ON)
find_package(Qt4 4.4.3 REQUIRED QtGui QtXml)
add_executable(myexe main.cpp)
target_link_libraries(myexe Qt4::QtGui Qt4::QtXml)



Note
When using IMPORTED targets, the qtmain.lib static library is
automatically linked on Windows for WIN32
executables. To disable that globally, set the
QT4_NO_LINK_QTMAIN variable before finding Qt4. To disable that
for a particular executable, set the QT4_NO_LINK_QTMAIN target
property to TRUE on the executable.

  


Qt Build Tools
Qt relies on some bundled tools for code generation, such as moc for
meta-object code generation,``uic`` for widget layout and population,
and rcc for virtual filesystem content generation.  These tools may be
automatically invoked by cmake(1) if the appropriate conditions
are met.  See cmake-qt(7) for more.
  


Qt Macros
In some cases it can be necessary or useful to invoke the Qt build tools in a
more-manual way. Several macros are available to add targets for such uses.
macro QT4_WRAP_CPP(outfiles inputfile ... [TARGET tgt] OPTIONS ...)
      create moc code from a list of files containing Qt class with
      the Q_OBJECT declaration.  Per-directory preprocessor definitions
      are also added.  If the ```<tgt>``` is specified, the
      INTERFACE_INCLUDE_DIRECTORIES and INTERFACE_COMPILE_DEFINITIONS from
      the ```<tgt>``` are passed to moc.  Options may be given to moc, such as
      those found when executing "moc -help".


macro QT4_WRAP_UI(outfiles inputfile ... OPTIONS ...)
      create code from a list of Qt designer ui files.
      Options may be given to uic, such as those found
      when executing "uic -help"


macro QT4_ADD_RESOURCES(outfiles inputfile ... OPTIONS ...)
      create code from a list of Qt resource files.
      Options may be given to rcc, such as those found
      when executing "rcc -help"


macro QT4_GENERATE_MOC(inputfile outputfile [TARGET tgt])
      creates a rule to run moc on infile and create outfile.
      Use this if for some reason QT4_WRAP_CPP() isn't appropriate, e.g.
      because you need a custom filename for the moc file or something
      similar.  If the ```<tgt>``` is specified, the
      INTERFACE_INCLUDE_DIRECTORIES and INTERFACE_COMPILE_DEFINITIONS from
      the ```<tgt>``` are passed to moc.


macro QT4_ADD_DBUS_INTERFACE(outfiles interface basename)
      Create the interface header and implementation files with the
      given basename from the given interface xml file and add it to
      the list of sources.

      You can pass additional parameters to the qdbusxml2cpp call by setting
      properties on the input file:

      INCLUDE the given file will be included in the generate interface header

      CLASSNAME the generated class is named accordingly

      NO_NAMESPACE the generated class is not wrapped in a namespace


macro QT4_ADD_DBUS_INTERFACES(outfiles inputfile ... )
      Create the interface header and implementation files
      for all listed interface xml files.
      The basename will be automatically determined from the name
      of the xml file.

      The source file properties described for
      QT4_ADD_DBUS_INTERFACE also apply here.


macro QT4_ADD_DBUS_ADAPTOR(outfiles xmlfile parentheader parentclassname
                           [basename] [classname])
      create a dbus adaptor (header and implementation file) from the xml file
      describing the interface, and add it to the list of sources. The adaptor
      forwards the calls to a parent class, defined in parentheader and named
      parentclassname. The name of the generated files will be
      ```<basename>```adaptor.{cpp,h} where basename defaults to the basename of the
      xml file.
      If ```<classname>``` is provided, then it will be used as the classname of the
      adaptor itself.


macro QT4_GENERATE_DBUS_INTERFACE( header [interfacename] OPTIONS ...)
      generate the xml interface file from the given header.
      If the optional argument interfacename is omitted, the name of the
      interface file is constructed from the basename of the header with
      the suffix .xml appended.
      Options may be given to qdbuscpp2xml, such as those found when
      executing "qdbuscpp2xml --help"


macro QT4_CREATE_TRANSLATION( qm_files directories ... sources ...
                              ts_files ... OPTIONS ...)
      out: qm_files
      in:  directories sources ts_files
      options: flags to pass to lupdate, such as -extensions to specify
      extensions for a directory scan.
      generates commands to create .ts (vie lupdate) and .qm
      (via lrelease) - files from directories and/or sources. The ts files are
      created and/or updated in the source tree (unless given with full paths).
      The qm files are generated in the build tree.
      Updating the translations can be done by adding the qm_files
      to the source list of your library/executable, so they are
      always updated, or by adding a custom target to control when
      they get updated/generated.


macro QT4_ADD_TRANSLATION( qm_files ts_files ... )
      out: qm_files
      in:  ts_files
      generates commands to create .qm from .ts - files. The generated
      filenames can be found in qm_files. The ts_files
      must exist and are not updated in any way.


macro QT4_AUTOMOC(sourcefile1 sourcefile2 ... [TARGET tgt])
      The qt4_automoc macro is obsolete.  Use the CMAKE_AUTOMOC feature instead.
      This macro is still experimental.
      It can be used to have moc automatically handled.
      So if you have the files foo.h and foo.cpp, and in foo.h a
      a class uses the Q_OBJECT macro, moc has to run on it. If you don't
      want to use QT4_WRAP_CPP() (which is reliable and mature), you can insert
      #include "foo.moc"
      in foo.cpp and then give foo.cpp as argument to QT4_AUTOMOC(). This will
      scan all listed files at cmake-time for such included moc files and if it
      finds them cause a rule to be generated to run moc at build time on the
      accompanying header file foo.h.
      If a source file has the SKIP_AUTOMOC property set it will be ignored by
      this macro.
      If the ```<tgt>``` is specified, the INTERFACE_INCLUDE_DIRECTORIES and
      INTERFACE_COMPILE_DEFINITIONS from the ```<tgt>``` are passed to moc.


function QT4_USE_MODULES( target [link_type] modules...)
       This function is obsolete. Use target_link_libraries with IMPORTED targets
       instead.
       Make ```<target>``` use the ```<modules>``` from Qt. Using a Qt module means
       to link to the library, add the relevant include directories for the
       module, and add the relevant compiler defines for using the module.
       Modules are roughly equivalent to components of Qt4, so usage would be
       something like:
        qt4_use_modules(myexe Core Gui Declarative)
       to use QtCore, QtGui and QtDeclarative. The optional ```<link_type>``` argument
       can be specified as either LINK_PUBLIC or LINK_PRIVATE to specify the
       same argument to the target_link_libraries call.


  


IMPORTED Targets
A particular Qt library may be used by using the corresponding
IMPORTED target with the target_link_libraries()
command:
target_link_libraries(myexe Qt4::QtGui Qt4::QtXml)


Using a target in this way causes :cmake(1)` to use the appropriate include
directories and compile definitions for the target when compiling myexe.
Targets are aware of their dependencies, so for example it is not necessary
to list Qt4::QtCore if another Qt library is listed, and it is not
necessary to list Qt4::QtGui if Qt4::QtDeclarative is listed.
Targets may be tested for existence in the usual way with the
if(TARGET) command.
The Qt toolkit may contain both debug and release libraries.
cmake(1) will choose the appropriate version based on the build
configuration.

Qt4::QtCore
The QtCore target
Qt4::QtGui
The QtGui target
Qt4::Qt3Support
The Qt3Support target
Qt4::QtAssistant
The QtAssistant target
Qt4::QtAssistantClient
The QtAssistantClient target
Qt4::QAxContainer
The QAxContainer target (Windows only)
Qt4::QAxServer
The QAxServer target (Windows only)
Qt4::QtDBus
The QtDBus target
Qt4::QtDeclarative
The QtDeclarative target
Qt4::QtDesigner
The QtDesigner target
Qt4::QtDesignerComponents
The QtDesignerComponents target
Qt4::QtHelp
The QtHelp target
Qt4::QtMotif
The QtMotif target
Qt4::QtMultimedia
The QtMultimedia target
Qt4::QtNetwork
The QtNetwork target
Qt4::QtNsPLugin
The QtNsPLugin target
Qt4::QtOpenGL
The QtOpenGL target
Qt4::QtScript
The QtScript target
Qt4::QtScriptTools
The QtScriptTools target
Qt4::QtSql
The QtSql target
Qt4::QtSvg
The QtSvg target
Qt4::QtTest
The QtTest target
Qt4::QtUiTools
The QtUiTools target
Qt4::QtWebKit
The QtWebKit target
Qt4::QtXml
The QtXml target
Qt4::QtXmlPatterns
The QtXmlPatterns target
Qt4::phonon
The phonon target

  


Result Variables

Below is a detailed list of variables that FindQt4.cmake sets.

Qt4_FOUND
If false, don¡¯t try to use Qt 4.
QT_FOUND
If false, don¡¯t try to use Qt. This variable is for compatibility only.
QT4_FOUND
If false, don¡¯t try to use Qt 4. This variable is for compatibility only.
QT_VERSION_MAJOR
The major version of Qt found.
QT_VERSION_MINOR
The minor version of Qt found.
QT_VERSION_PATCH
The patch version of Qt found.

  

