  

# ANDROID_NATIVE_LIB_DIRECTORIES  
Set the Android property that specifies directories to search for the .so
libraries.  

This a string property that contains the directory paths separated
by semicolons.  

This property is initialized by the value of the
CMAKE_ANDROID_NATIVE_LIB_DIRECTORIES variable if it is set when a
target is created.  

Contents of ANDROID_NATIVE_LIB_DIRECTORIES may use ˇ°generator expressionsˇ±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  

