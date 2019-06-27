  

# UseJava  
Use Module for Java  

This file provides functions for Java.  It is assumed that
FindJava has already been loaded.  See FindJava for
information on how to load Java into your CMake project.  


Creating And Installing JARs
add_jar(```<target_name>```
        [SOURCES] ```<source1>``` [```<source2>```...] [```<resource1>```...]
        [INCLUDE_JARS ```<jar1>``` [```<jar2>```...]]
        [ENTRY_POINT ```<entry>```]
        [VERSION ```<version>```]
        [OUTPUT_NAME ```<name>```]
        [OUTPUT_DIR ```<dir>```]
        [GENERATE_NATIVE_HEADERS ```<target>``` [DESTINATION ```<dir>```]]
        )


This command creates a ```<target_name>```.jar.  It compiles the given
```<source>``` files and adds the given ```<resource>``` files to
the jar file.  Source files can be java files or listing files
(prefixed by @).  If only resource files are given then just a jar file
is created.  The list of INCLUDE_JARS are added to the classpath when
compiling the java sources and also to the dependencies of the target.
INCLUDE_JARS also accepts other target names created by add_jar().
For backwards compatibility, jar files listed as sources are ignored (as
they have been since the first version of this module).
The default OUTPUT_DIR can also be changed by setting the variable
CMAKE_JAVA_TARGET_OUTPUT_DIR.
Optionally, using option GENERATE_NATIVE_HEADERS, native header files can
be generated for methods declared as native.  These files provide the
connective glue that allow your Java and C code to interact.  An INTERFACE
target will be created for an easy usage of generated files.  Sub-option
DESTINATION can be used to specify the output directory for generated
header files.
GENERATE_NATIVE_HEADERS option requires, at least, version 1.8 of the JDK.
The add_jar() function sets the following target properties on
```<target_name>```:

INSTALL_FILES
The files which should be installed.  This is used by install_jar().
JNI_SYMLINK
The JNI symlink which should be installed.  This is used by
install_jni_symlink().
JAR_FILE
The location of the jar file so that you can include it.
CLASSDIR
The directory where the class files can be found.  For example to use them
with javah.

install_jar(```<target_name>``` ```<destination>```)
install_jar(```<target_name>``` DESTINATION ```<destination>``` [COMPONENT ```<component>```])


This command installs the ```<target_name>``` files to the given
```<destination>```.  It should be called in the same scope as add_jar() or
it will fail.
The install_jar() function sets the INSTALL_DESTINATION target
property on jars so installed.  This property holds the ```<destination>``` as
described above, and is used by install_jar_exports().  You can get this
information with get_property() and the INSTALL_DESTINATION
property key.
install_jni_symlink(```<target_name>``` ```<destination>```)
install_jni_symlink(```<target_name>``` DESTINATION ```<destination>``` [COMPONENT ```<component>```])


This command installs the ```<target_name>``` JNI symlinks to the given
```<destination>```.  It should be called in the same scope as add_jar() or
it will fail.
install_jar_exports(TARGETS ```<jars>```...
                    [NAMESPACE ```<namespace>```]
                    FILE ```<filename>```
                    DESTINATION ```<destination>``` [COMPONENT ```<component>```])


This command installs a target export file ```<filename>``` for the named jar
targets to the given ```<destination>``` directory.  Its function is similar to
that of install(EXPORTS).
export_jars(TARGETS ```<jars>```...
            [NAMESPACE ```<namespace>```]
            FILE ```<filename>```)


This command writes a target export file ```<filename>``` for the named ```<jars>```
targets.  Its function is similar to that of export().

Examples
To add compile flags to the target you can set these flags with the following
variable:
set(CMAKE_JAVA_COMPILE_FLAGS -nowarn)


To add a path or a jar file to the class path you can do this with the
CMAKE_JAVA_INCLUDE_PATH variable.
set(CMAKE_JAVA_INCLUDE_PATH /usr/share/java/shibboleet.jar)


To use a different output name for the target you can set it with:
add_jar(foobar foobar.java OUTPUT_NAME shibboleet.jar)


To use a different output directory than CMAKE_CURRENT_BINARY_DIR you can
set it with:
add_jar(foobar foobar.java OUTPUT_DIR ${PROJECT_BINARY_DIR}/bin)


To define an entry point in your jar you can set it with the ENTRY_POINT
named argument:
add_jar(example ENTRY_POINT com/examples/MyProject/Main)


To define a custom manifest for the jar, you can set it with the MANIFEST
named argument:
add_jar(example MANIFEST /path/to/manifest)


To add a version to the target output name you can set it using the VERSION
named argument to add_jar().  The following example will create a jar file
with the name shibboleet-1.0.0.jar and will create a symlink
shibboleet.jar pointing to the jar with the version information.
add_jar(shibboleet shibbotleet.java VERSION 1.2.0)


If the target is a JNI library, utilize the following commands to
create a JNI symbolic link:
set(CMAKE_JNI_TARGET TRUE)
add_jar(shibboleet shibbotleet.java VERSION 1.2.0)
install_jar(shibboleet ${LIB_INSTALL_DIR}/shibboleet)
install_jni_symlink(shibboleet ${JAVA_LIB_INSTALL_DIR})


If a single target needs to produce more than one jar from its
java source code, to prevent the accumulation of duplicate class
files in subsequent jars, set/reset CMAKE_JAR_CLASSES_PREFIX prior
to calling the add_jar() function:
set(CMAKE_JAR_CLASSES_PREFIX com/redhat/foo)
add_jar(foo foo.java)

set(CMAKE_JAR_CLASSES_PREFIX com/redhat/bar)
add_jar(bar bar.java)


For an optimum usage of option GENERATE_NATIVE_HEADERS, it is recommended to
include module JNI before any call to add_jar(). The produced target for
native headers can then be used to compile C/C++ sources with the
target_link_libraries() command.
find_package(JNI)
add_jar(foo foo.java GENERATE_NATIVE_HEADERS foo-native)
add_library(bar bar.cpp)
target_link_libraries(bar PRIVATE foo-native)



  


Finding JARs
find_jar(```<VAR>```
         ```<name>``` | NAMES ```<name1>``` [```<name2>```...]
         [PATHS ```<path1>``` [```<path2>```... ENV ```<var>```]]
         [VERSIONS ```<version1>``` [```<version2>```]]
         [DOC "cache documentation string"]
        )


This command is used to find a full path to the named jar.  A cache
entry named by ```<VAR>``` is created to store the result of this command.
If the full path to a jar is found the result is stored in the
variable and the search will not repeated unless the variable is
cleared.  If nothing is found, the result will be ```<VAR>```-NOTFOUND, and
the search will be attempted again next time find_jar() is invoked with
the same variable.  The name of the full path to a file that is
searched for is specified by the names listed after NAMES argument.
Additional search locations can be specified after the PATHS argument.
If you require special a version of a jar file you can specify it with
the VERSIONS argument.  The argument after DOC will be used for the
documentation string in the cache.
  


Javadoc
The create_javadoc() command can be used to create java documentation
based on files or packages.  For more details please read the javadoc manpage.
There are two main signatures for create_javadoc().  The first signature
works with package names on a path with source files.
create_javadoc(```<VAR>```
               PACKAGES ```<pkg1>``` [```<pkg2>```...]
               [SOURCEPATH ```<sourcepath>```]
               [CLASSPATH ```<classpath>```]
               [INSTALLPATH ```<install path>```]
               [DOCTITLE "the documentation title"]
               [WINDOWTITLE "the title of the document"]
               [AUTHOR TRUE|FALSE]
               [USE TRUE|FALSE]
               [VERSION TRUE|FALSE]
               )


For example:
create_javadoc(my_example_doc
  PACKAGES com.example.foo com.example.bar
  SOURCEPATH "${CMAKE_CURRENT_SOURCE_DIR}"
  CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
  WINDOWTITLE "My example"
  DOCTITLE "```<h1>```My example```</h1>```"
  AUTHOR TRUE
  USE TRUE
  VERSION TRUE
)


The second signature for create_javadoc() works on a given list of
files.
create_javadoc(```<VAR>```
               FILES ```<file1>``` [```<file2>```...]
               [CLASSPATH ```<classpath>```]
               [INSTALLPATH ```<install path>```]
               [DOCTITLE "the documentation title"]
               [WINDOWTITLE "the title of the document"]
               [AUTHOR TRUE|FALSE]
               [USE TRUE|FALSE]
               [VERSION TRUE|FALSE]
              )


For example:
create_javadoc(my_example_doc
  FILES ${example_SRCS}
  CLASSPATH ${CMAKE_JAVA_INCLUDE_PATH}
  WINDOWTITLE "My example"
  DOCTITLE "```<h1>```My example```</h1>```"
  AUTHOR TRUE
  USE TRUE
  VERSION TRUE
)


Both signatures share most of the options.  These options are the same
as what you can find in the javadoc manpage.  Please look at the
manpage for CLASSPATH, DOCTITLE, WINDOWTITLE, AUTHOR, USE
and VERSION.
If you don¡¯t set the INSTALLPATH, then by default the documentation will
be installed to :
${CMAKE_INSTALL_PREFIX}/share/javadoc/```<VAR>```


  


Header Generation
create_javah(TARGET ```<target>``` | GENERATED_FILES ```<VAR>```
             CLASSES ```<class>```...
             [CLASSPATH ```<classpath>```...]
             [DEPENDS ```<depend>```...]
             [OUTPUT_NAME ```<path>```|OUTPUT_DIR ```<path>```]
             )


Create C header files from java classes. These files provide the connective glue
that allow your Java and C code to interact.

Deprecated since version 3.11.


Note
This command will no longer be supported starting with version 10 of the JDK
due to the suppression of javah tool.
The add_jar(GENERATE_NATIVE_HEADERS) command should be used instead.

There are two main signatures for create_javah().  The first signature
returns generated files through variable specified by the GENERATED_FILES
option.  For example:
create_javah(GENERATED_FILES files_headers
  CLASSES org.cmake.HelloWorld
  CLASSPATH hello.jar
)


The second signature for create_javah() creates a target which encapsulates
header files generation. E.g.
create_javah(TARGET target_headers
  CLASSES org.cmake.HelloWorld
  CLASSPATH hello.jar
)


Both signatures share same options.

CLASSES ```<class>```...
Specifies Java classes used to generate headers.
CLASSPATH ```<classpath>```...
Specifies various paths to look up classes. Here .class files, jar files or
targets created by command add_jar can be used.
DEPENDS ```<depend>```...
Targets on which the javah target depends.
OUTPUT_NAME ```<path>```
Concatenates the resulting header files for all the classes listed by option
CLASSES into ```<path>```.  Same behavior as option -o of javah tool.
OUTPUT_DIR ```<path>```
Sets the directory where the header files will be generated.  Same behavior
as option -d of javah tool.  If not specified,
CMAKE_CURRENT_BINARY_DIR is used as the output directory.

  

