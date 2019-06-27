  

# ProcessorCount  
ProcessorCount(var)  

Determine the number of processors/cores and save value in ${var}  

Sets the variable named ${var} to the number of physical cores
available on the machine if the information can be determined.
Otherwise it is set to 0.  Currently this functionality is implemented
for AIX, cygwin, FreeBSD, HPUX, Linux, macOS, QNX, Sun and
Windows.  

This function is guaranteed to return a positive integer (>```=1) if it
succeeds.  It returns 0 if there¡¯s a problem determining the processor
count.  

Example use, in a ctest -S dashboard script:  

include(ProcessorCount)
ProcessorCount(N)
if(NOT N EQUAL 0)
  set(CTEST_BUILD_FLAGS -j${N})
  set(ctest_test_args ${ctest_test_args} PARALLEL_LEVEL ${N})
endif()

  

This function is intended to offer an approximation of the value of
the number of compute cores available on the current machine, such
that you may use that value for parallel building and parallel
testing.  It is meant to help utilize as much of the machine as seems
reasonable.  Of course, knowledge of what else might be running on the
machine simultaneously should be used when deciding whether to request
a machine¡¯s full capacity all for yourself.  

