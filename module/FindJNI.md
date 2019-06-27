  

# FindJNI  
Find Java Native Interface (JNI) libraries.  

JNI enables Java code running in a Java Virtual Machine (JVM) to call
and be called by native applications and libraries written in other
languages such as C, C++.  

This module finds if Java is installed and determines where the
include files and libraries are.  It also determines what the name of
the library is.  The caller may set variable JAVA_HOME to specify a
Java installation prefix explicitly.  


Result Variables
This module sets the following result variables:

JNI_INCLUDE_DIRS
the include dirs to use
JNI_LIBRARIES
the libraries to use (JAWT and JVM)
JNI_FOUND
TRUE if JNI headers and libraries were found.

  


Cache Variables
The following cache variables are also available to set or use:

JAVA_AWT_LIBRARY
the path to the Java AWT Native Interface (JAWT) library
JAVA_JVM_LIBRARY
the path to the Java Virtual Machine (JVM) library
JAVA_INCLUDE_PATH
the include path to jni.h
JAVA_INCLUDE_PATH2
the include path to jni_md.h and jniport.h
JAVA_AWT_INCLUDE_PATH
the include path to jawt.h

  

