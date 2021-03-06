  

# try_compile  

Contents

try_compile
Try Compiling Whole Projects
Try Compiling Source Files
Other Behavior Settings



  

Try building some code.  


Try Compiling Whole Projects
try_compile(```<resultVar>``` ```<bindir>``` ```<srcdir>```
            ```<projectName>``` [```<targetName>```] [CMAKE_FLAGS ```<flags>```...]
            [OUTPUT_VARIABLE ```<var>```])


Try building a project.  The success or failure of the try_compile,
i.e. TRUE or FALSE respectively, is returned in ```<resultVar>```.
In this form, ```<srcdir>``` should contain a complete CMake project with a
CMakeLists.txt file and all sources.  The ```<bindir>``` and ```<srcdir>```
will not be deleted after this command is run.  Specify ```<targetName>``` to
build a specific target instead of the all or ALL_BUILD target.  See
below for the meaning of other options.
  


Try Compiling Source Files
try_compile(```<resultVar>``` ```<bindir>``` ```<srcfile|SOURCES srcfile...>```
            [CMAKE_FLAGS ```<flags>```...]
            [COMPILE_DEFINITIONS ```<defs>```...]
            [LINK_OPTIONS ```<options>```...]
            [LINK_LIBRARIES ```<libs>```...]
            [OUTPUT_VARIABLE ```<var>```]
            [COPY_FILE ```<fileName>``` [COPY_FILE_ERROR ```<var>```]]
            [```<LANG>```_STANDARD ```<std>```]
            [```<LANG>```_STANDARD_REQUIRED ```<bool>```]
            [```<LANG>```_EXTENSIONS ```<bool>```]
            )


Try building an executable or static library from one or more source files
(which one is determined by the CMAKE_TRY_COMPILE_TARGET_TYPE
variable).  The success or failure of the try_compile, i.e. TRUE or
FALSE respectively, is returned in ```<resultVar>```.
In this form, one or more source files must be provided.  If
CMAKE_TRY_COMPILE_TARGET_TYPE is unset or is set to EXECUTABLE,
the sources must include a definition for main and CMake will create a
CMakeLists.txt file to build the source(s) as an executable.
If CMAKE_TRY_COMPILE_TARGET_TYPE is set to STATIC_LIBRARY,
a static library will be built instead and no definition for main is
required.  For an executable, the generated CMakeLists.txt file would
contain something like the following:
add_definitions(```<expanded COMPILE_DEFINITIONS from caller>```)
include_directories(${INCLUDE_DIRECTORIES})
link_directories(${LINK_DIRECTORIES})
add_executable(cmTryCompileExec ```<srcfile>```...)
target_link_options(cmTryCompileExec PRIVATE ```<LINK_OPTIONS from caller>```)
target_link_libraries(cmTryCompileExec ${LINK_LIBRARIES})


The options are:

CMAKE_FLAGS ```<flags>```...
Specify flags of the form -DVAR:TYPE=VALUE to be passed to
the cmake command-line used to drive the test build.
The above example shows how values for variables
INCLUDE_DIRECTORIES, LINK_DIRECTORIES, and LINK_LIBRARIES
are used.
COMPILE_DEFINITIONS ```<defs>```...
Specify -Ddefinition arguments to pass to add_definitions()
in the generated test project.
COPY_FILE ```<fileName>```
Copy the built executable or static library to the given ```<fileName>```.
COPY_FILE_ERROR ```<var>```
Use after COPY_FILE to capture into variable ```<var>``` any error
message encountered while trying to copy the file.
LINK_LIBRARIES ```<libs>```...
Specify libraries to be linked in the generated project.
The list of libraries may refer to system libraries and to
Imported Targets from the calling project.
If this option is specified, any -DLINK_LIBRARIES=... value
given to the CMAKE_FLAGS option will be ignored.

LINK_OPTIONS ```<options>```...
Specify link step options to pass to target_link_options() or to
set the STATIC_LIBRARY_OPTIONS target property in the generated
project, depending on the CMAKE_TRY_COMPILE_TARGET_TYPE variable.
OUTPUT_VARIABLE ```<var>```
Store the output from the build process in the given variable.
```<LANG>```_STANDARD ```<std>```
Specify the C_STANDARD, CXX_STANDARD,
or CUDA_STANDARD target property of the generated project.
```<LANG>```_STANDARD_REQUIRED ```<bool>```
Specify the C_STANDARD_REQUIRED,
CXX_STANDARD_REQUIRED, or CUDA_STANDARD_REQUIRED
target property of the generated project.
```<LANG>```_EXTENSIONS ```<bool>```
Specify the C_EXTENSIONS, CXX_EXTENSIONS,
or CUDA_EXTENSIONS target property of the generated project.

In this version all files in ```<bindir>```/CMakeFiles/CMakeTmp will be
cleaned automatically.  For debugging, --debug-trycompile can be
passed to cmake to avoid this clean.  However, multiple sequential
try_compile operations reuse this single output directory.  If you use
--debug-trycompile, you can only debug one try_compile call at a time.
The recommended procedure is to protect all try_compile calls in your
project by if(NOT DEFINED ```<resultVar>```) logic, configure with cmake
all the way through once, then delete the cache entry associated with
the try_compile call of interest, and then re-run cmake again with
--debug-trycompile.
  


Other Behavior Settings
If set, the following variables are passed in to the generated
try_compile CMakeLists.txt to initialize compile target properties with
default values:

CMAKE_ENABLE_EXPORTS
CMAKE_LINK_SEARCH_START_STATIC
CMAKE_LINK_SEARCH_END_STATIC
CMAKE_MSVC_RUNTIME_LIBRARY
CMAKE_POSITION_INDEPENDENT_CODE

If CMP0056 is set to NEW, then
CMAKE_EXE_LINKER_FLAGS is passed in as well.
If CMP0083 is set to NEW, then in order to obtain correct
behavior at link time, the check_pie_supported() command from the
CheckPIESupported module must be called before using the
try_compile() command.
The current settings of CMP0065 and CMP0083 are propagated
through to the generated test project.
Set the CMAKE_TRY_COMPILE_CONFIGURATION variable to choose
a build configuration.
Set the CMAKE_TRY_COMPILE_TARGET_TYPE variable to specify
the type of target used for the source file signature.
Set the CMAKE_TRY_COMPILE_PLATFORM_VARIABLES variable to specify
variables that must be propagated into the test project.  This variable is
meant for use only in toolchain files and is only honored by the
try_compile() command for the source files form, not when given a whole
project.
If CMP0067 is set to NEW, or any of the ```<LANG>```_STANDARD,
```<LANG>```_STANDARD_REQUIRED, or ```<LANG>```_EXTENSIONS options are used,
then the language standard variables are honored:

CMAKE_C_STANDARD
CMAKE_C_STANDARD_REQUIRED
CMAKE_C_EXTENSIONS
CMAKE_CXX_STANDARD
CMAKE_CXX_STANDARD_REQUIRED
CMAKE_CXX_EXTENSIONS
CMAKE_CUDA_STANDARD
CMAKE_CUDA_STANDARD_REQUIRED
CMAKE_CUDA_EXTENSIONS

Their values are used to set the corresponding target properties in
the generated project (unless overridden by an explicit option).
For the Green Hills MULTI generator the GHS toolset and target
system customization cache variables are also propagated into the test project.
  

