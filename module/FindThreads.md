  

# FindThreads  
This module determines the thread library of the system.  

The following variables are set  

CMAKE_THREAD_LIBS_INIT     - the thread library
CMAKE_USE_WIN32_THREADS_INIT - using WIN32 threads?
CMAKE_USE_PTHREADS_INIT    - are we using pthreads
CMAKE_HP_PTHREADS_INIT     - are we using hp pthreads

  

The following import target is created  

Threads::Threads

  

If the use of the -pthread compiler and linker flag is preferred then the
caller can set  

THREADS_PREFER_PTHREAD_FLAG

  

The compiler flag can only be used with the imported
target. Use of both the imported target as well as this switch is highly
recommended for new code.  

