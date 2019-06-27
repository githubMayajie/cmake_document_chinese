  

# CMakePushCheckState  
This module defines three macros: CMAKE_PUSH_CHECK_STATE()
CMAKE_POP_CHECK_STATE() and CMAKE_RESET_CHECK_STATE() These macros can
be used to save, restore and reset (i.e., clear contents) the state of
the variables CMAKE_REQUIRED_FLAGS, CMAKE_REQUIRED_DEFINITIONS,
CMAKE_REQUIRED_LINK_OPTIONS, CMAKE_REQUIRED_LIBRARIES,
CMAKE_REQUIRED_INCLUDES and CMAKE_EXTRA_INCLUDE_FILES used by the
various Check-files coming with CMake, like e.g. check_function_exists()
etc.
The variable contents are pushed on a stack, pushing multiple times is
supported.  This is useful e.g.  when executing such tests in a Find-module,
where they have to be set, but after the Find-module has been executed they
should have the same value as they had before.  

CMAKE_PUSH_CHECK_STATE() macro receives optional argument RESET.
Whether it¡¯s specified, CMAKE_PUSH_CHECK_STATE() will set all
CMAKE_REQUIRED_* variables to empty values, same as
CMAKE_RESET_CHECK_STATE() call will do.  

Usage:  

cmake_push_check_state(RESET)
set(CMAKE_REQUIRED_DEFINITIONS -DSOME_MORE_DEF)
check_function_exists(...)
cmake_reset_check_state()
set(CMAKE_REQUIRED_DEFINITIONS -DANOTHER_DEF)
check_function_exists(...)
cmake_pop_check_state()

  

