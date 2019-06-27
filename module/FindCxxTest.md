  

# FindCxxTest  
Find CxxTest unit testing framework.  

Find the CxxTest suite and declare a helper macro for creating unit
tests and integrating them with CTest.  For more details on CxxTest
see http://cxxtest.tigris.org  

INPUT Variables  

CXXTEST_USE_PYTHON [deprecated since 1.3]
    Only used in the case both Python & Perl
    are detected on the system to control
    which CxxTest code generator is used.
    Valid only for CxxTest version 3.

  

NOTE: In older versions of this Find Module,
this variable controlled if the Python test
generator was used instead of the Perl one,
regardless of which scripting language the
user had installed.

  

CXXTEST_TESTGEN_ARGS (since CMake 2.8.3)
    Specify a list of options to pass to the CxxTest code
    generator.  If not defined, --error-printer is
    passed.

  

OUTPUT Variables  

CXXTEST_FOUND
    True if the CxxTest framework was found
CXXTEST_INCLUDE_DIRS
    Where to find the CxxTest include directory
CXXTEST_PERL_TESTGEN_EXECUTABLE
    The perl-based test generator
CXXTEST_PYTHON_TESTGEN_EXECUTABLE
    The python-based test generator
CXXTEST_TESTGEN_EXECUTABLE (since CMake 2.8.3)
    The test generator that is actually used (chosen using user preferences
    and interpreters found in the system)
CXXTEST_TESTGEN_INTERPRETER (since CMake 2.8.3)
    The full path to the Perl or Python executable on the system, on
    platforms where the script cannot be executed using its shebang line.

  

MACROS for optional use by CMake users:  

CXXTEST_ADD_TEST(```<test_name>``` ```<gen_source_file>``` ```<input_files_to_testgen...>```)
   Creates a CxxTest runner and adds it to the CTest testing suite
   Parameters:
       test_name               The name of the test
       gen_source_file         The generated source filename to be
                               generated by CxxTest
       input_files_to_testgen  The list of header files containing the
                               CxxTest::TestSuite's to be included in
                               this runner

  

#==============
Example Usage:

  

find_package(CxxTest)
if(CXXTEST_FOUND)
    include_directories(${CXXTEST_INCLUDE_DIR})
    enable_testing()

  

    CXXTEST_ADD_TEST(unittest_foo foo_test.cc
                      ${CMAKE_CURRENT_SOURCE_DIR}/foo_test.h)
    target_link_libraries(unittest_foo foo) # as needed
endif()

  

This will (if CxxTest is found):
1. Invoke the testgen executable to autogenerate foo_test.cc in the
   binary tree from "foo_test.h" in the current source directory.
2. Create an executable and test called unittest_foo.

  

#=============
Example foo_test.h:

  

#include ```<cxxtest/TestSuite.h>```

  

class MyTestSuite : public CxxTest::TestSuite
{
public:
   void testAddition( void )
   {
      TS_ASSERT( 1 + 1 >``` 1 );
      TS_ASSERT_EQUALS( 1 + 1, 2 );
   }
};

  
