  

# add_library  

Contents

add_library
Normal Libraries
Imported Libraries
Object Libraries
Alias Libraries
Interface Libraries



  

Add a library to the project using the specified source files.  


Normal Libraries
add_library(```<name>``` [STATIC | SHARED | MODULE]
            [EXCLUDE_FROM_ALL]
            [source1] [source2 ...])


Adds a library target called ```<name>``` to be built from the source files
listed in the command invocation.  (The source files can be omitted here
if they are added later using target_sources().)  The ```<name>```
corresponds to the logical target name and must be globally unique within
a project.  The actual file name of the library built is constructed based
on conventions of the native platform (such as lib```<name>```.a or
```<name>```.lib).
STATIC, SHARED, or MODULE may be given to specify the type of
library to be created.  STATIC libraries are archives of object files
for use when linking other targets.  SHARED libraries are linked
dynamically and loaded at runtime.  MODULE libraries are plugins that
are not linked into other targets but may be loaded dynamically at runtime
using dlopen-like functionality.  If no type is given explicitly the
type is STATIC or SHARED based on whether the current value of the
variable BUILD_SHARED_LIBS is ON.  For SHARED and
MODULE libraries the POSITION_INDEPENDENT_CODE target
property is set to ON automatically.
A SHARED or STATIC library may be marked with the FRAMEWORK
target property to create an macOS Framework.
If a library does not export any symbols, it must not be declared as a
SHARED library.  For example, a Windows resource DLL or a managed C++/CLI
DLL that exports no unmanaged symbols would need to be a MODULE library.
This is because CMake expects a SHARED library to always have an
associated import library on Windows.
By default the library file will be created in the build tree directory
corresponding to the source tree directory in which the command was
invoked.  See documentation of the ARCHIVE_OUTPUT_DIRECTORY,
LIBRARY_OUTPUT_DIRECTORY, and
RUNTIME_OUTPUT_DIRECTORY target properties to change this
location.  See documentation of the OUTPUT_NAME target
property to change the ```<name>``` part of the final file name.
If EXCLUDE_FROM_ALL is given the corresponding property will be set on
the created target.  See documentation of the EXCLUDE_FROM_ALL
target property for details.
Source arguments to add_library may use ��generator expressions�� with
the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.
See also HEADER_FILE_ONLY on what to do if some sources are
pre-processed, and you want to have the original sources reachable from
within IDE.
  


Imported Libraries
add_library(```<name>``` ```<SHARED|STATIC|MODULE|OBJECT|UNKNOWN>``` IMPORTED
            [GLOBAL])


An IMPORTED library target references a library
file located outside the project.  No rules are generated to build it, and
the IMPORTED target property is True.  The target name has
scope in the directory in which it is created and below, but the GLOBAL
option extends visibility.  It may be referenced like any target built
within the project.  IMPORTED libraries are useful for convenient
reference from commands like target_link_libraries().  Details
about the imported library are specified by setting properties whose names
begin in IMPORTED_ and INTERFACE_.
The most important properties are:

IMPORTED_LOCATION (and its per-configuration
variant IMPORTED_LOCATION_```<CONFIG>```) which specifies the
location of the main library file on disk.
IMPORTED_OBJECTS (and IMPORTED_OBJECTS_```<CONFIG>```)
for object libraries, specifies the locations of object files on disk.
PUBLIC_HEADER files to be installed during install() invocation

See documentation of the IMPORTED_* and INTERFACE_* properties
for more information.
An UNKNOWN library type is typically only used in the implementation of
Find Modules.  It allows the path to an imported library (often found
using the find_library() command) to be used without having to know
what type of library it is.  This is especially useful on Windows where a
static library and a DLL��s import library both have the same file extension.
  


Object Libraries
add_library(```<name>``` OBJECT ```<src>```...)


Creates an Object Library.  An object library
compiles source files but does not archive or link their object files into a
library.  Instead other targets created by add_library() or
add_executable() may reference the objects using an expression of the
form $```<TARGET_OBJECTS:objlib>``` as a source, where objlib is the
object library name.  For example:
add_library(... $```<TARGET_OBJECTS:objlib>``` ...)
add_executable(... $```<TARGET_OBJECTS:objlib>``` ...)


will include objlib��s object files in a library and an executable
along with those compiled from their own sources.  Object libraries
may contain only sources that compile, header files, and other files
that would not affect linking of a normal library (e.g. .txt).
They may contain custom commands generating such sources, but not
PRE_BUILD, PRE_LINK, or POST_BUILD commands.  Some native build
systems (such as Xcode) may not like targets that have only object files, so
consider adding at least one real source file to any target that references
$```<TARGET_OBJECTS:objlib>```.
  


Alias Libraries
add_library(```<name>``` ALIAS ```<target>```)


Creates an Alias Target, such that ```<name>``` can be
used to refer to ```<target>``` in subsequent commands.  The ```<name>``` does
not appear in the generated buildsystem as a make target.  The ```<target>```
may not be a non-GLOBAL Imported Target or an
ALIAS.
ALIAS targets can be used as linkable targets and as targets to
read properties from.  They can also be tested for existence with the
regular if(TARGET) subcommand.  The ```<name>``` may not be used
to modify properties of ```<target>```, that is, it may not be used as the
operand of set_property(), set_target_properties(),
target_link_libraries() etc.  An ALIAS target may not be
installed or exported.
  


Interface Libraries
add_library(```<name>``` INTERFACE [IMPORTED [GLOBAL]])


Creates an Interface Library.  An INTERFACE
library target does not directly create build output, though it may
have properties set on it and it may be installed, exported and
imported. Typically the INTERFACE_* properties are populated on
the interface target using the commands:

set_property(),
target_link_libraries(INTERFACE),
target_link_options(INTERFACE),
target_include_directories(INTERFACE),
target_compile_options(INTERFACE),
target_compile_definitions(INTERFACE), and
target_sources(INTERFACE),

and then it is used as an argument to target_link_libraries()
like any other target.
An INTERFACE Imported Target may also be
created with this signature.  An IMPORTED library target references a
library defined outside the project.  The target name has scope in the
directory in which it is created and below, but the GLOBAL option
extends visibility.  It may be referenced like any target built within
the project.  IMPORTED libraries are useful for convenient reference
from commands like target_link_libraries().
  

