  

# CMAKE_CROSSCOMPILING_EMULATOR  
This variable is only used when CMAKE_CROSSCOMPILING is on. It
should point to a command on the host system that can run executable built
for the target system.  

If this variable contains a semicolon-separated list, then the first value is the command and remaining values are its
arguments.  

The command will be used to run try_run() generated executables,
which avoids manual population of the TryRunResults.cmake file.  

It is also used as the default value for the
CROSSCOMPILING_EMULATOR target property of executables.  

