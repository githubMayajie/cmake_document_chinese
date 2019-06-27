  

# CROSSCOMPILING_EMULATOR  
Use the given emulator to run executables created when crosscompiling.
This command will be added as a prefix to add_test(),
add_custom_command(), and add_custom_target() commands
for built target system executables.  

If this property contains a semicolon-separated list, then the first value is the command and remaining values are its
arguments.  

This property is initialized by the value of the
CMAKE_CROSSCOMPILING_EMULATOR variable if it is set when a target
is created.  

