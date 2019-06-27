  

# ANDROID_JAR_DIRECTORIES  
Set the Android property that specifies directories to search for
the JAR libraries.  

This a string property that contains the directory paths separated by
semicolons. This property is initialized by the value of the
CMAKE_ANDROID_JAR_DIRECTORIES variable if it is set when
a target is created.  

Contents of ANDROID_JAR_DIRECTORIES may use ¡°generator expressions¡±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  

