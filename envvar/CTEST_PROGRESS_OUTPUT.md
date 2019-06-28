  

# CTEST_PROGRESS_OUTPUT  
This is a CMake Environment Variable. Its initial value is taken from
the calling process environment.  

Boolean environment variable that affects how ctest
command output reports overall progress.  When set to 1, TRUE, ON or anything
else that evaluates to boolean true, progress is reported by repeatedly
updating the same line.  This greatly reduces the overall verbosity, but is
only supported when output is sent directly to a terminal.  If the environment
variable is not set or has a value that evaluates to false, output is reported
normally with each test having its own start and end lines logged to the
output.  

The --progress option to ctest overrides this
environment variable if both are given.  
