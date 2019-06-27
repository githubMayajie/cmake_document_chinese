  

# FindJava  
Find Java  

This module finds if Java is installed and determines where the
include files and libraries are.  The caller may set variable JAVA_HOME
to specify a Java installation prefix explicitly.  

See also the FindJNI module to find Java Native Interface (JNI).  

Specify one or more of the following components as you call this find module. See example below.  

Runtime     = Java Runtime Environment used to execute Java byte-compiled applications
Development = Development tools (java, javac, javah, jar and javadoc), includes Runtime component
IdlJ        = Interface Description Language (IDL) to Java compiler
JarSigner   = Signer and verifier tool for Java Archive (JAR) files

  

This module sets the following result variables:  

Java_JAVA_EXECUTABLE      = the full path to the Java runtime
Java_JAVAC_EXECUTABLE     = the full path to the Java compiler
Java_JAVAH_EXECUTABLE     = the full path to the Java header generator
Java_JAVADOC_EXECUTABLE   = the full path to the Java documentation generator
Java_IDLJ_EXECUTABLE      = the full path to the Java idl compiler
Java_JAR_EXECUTABLE       = the full path to the Java archiver
Java_JARSIGNER_EXECUTABLE = the full path to the Java jar signer
Java_VERSION_STRING       = Version of java found, eg. 1.6.0_12
Java_VERSION_MAJOR        = The major version of the package found.
Java_VERSION_MINOR        = The minor version of the package found.
Java_VERSION_PATCH        = The patch version of the package found.
Java_VERSION_TWEAK        = The tweak version of the package found (after '_')
Java_VERSION              = This is set to: $major[.$minor[.$patch[.$tweak]]]

  

The minimum required version of Java can be specified using the
find_package() syntax, e.g.  

find_package(Java 1.8)

  

NOTE: ${Java_VERSION} and ${Java_VERSION_STRING} are not guaranteed to
be identical.  For example some java version may return:
Java_VERSION_STRING = 1.8.0_17 and Java_VERSION = 1.8.0.17  

another example is the Java OEM, with: Java_VERSION_STRING = 1.8.0-oem
and Java_VERSION = 1.8.0  

For these components the following variables are set:  

Java_FOUND                    - TRUE if all components are found.
Java_```<component>```_FOUND        - TRUE if ```<component>``` is found.

  

Example Usages:  

find_package(Java)
find_package(Java 1.8 REQUIRED)
find_package(Java COMPONENTS Runtime)
find_package(Java COMPONENTS Development)

  

