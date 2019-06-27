  

# FindProtobuf  
Locate and configure the Google Protocol Buffers library.  

The following variables can be set and are optional:  


Protobuf_SRC_ROOT_FOLDER
When compiling with MSVC, if this cache variable is set
the protobuf-default VS project build locations
(vsprojects/Debug and vsprojects/Release
or vsprojects/x64/Debug and vsprojects/x64/Release)
will be searched for libraries and binaries.
Protobuf_IMPORT_DIRS
List of additional directories to be searched for
imported .proto files.
Protobuf_DEBUG
Show debug messages.
Protobuf_USE_STATIC_LIBS
Set to ON to force the use of the static libraries.
Default is OFF.
  

Defines the following variables:  


Protobuf_FOUND
Found the Google Protocol Buffers library
(libprotobuf & header files)
Protobuf_VERSION
Version of package found.
Protobuf_INCLUDE_DIRS
Include directories for Google Protocol Buffers
Protobuf_LIBRARIES
The protobuf libraries
Protobuf_PROTOC_LIBRARIES
The protoc libraries
Protobuf_LITE_LIBRARIES
The protobuf-lite libraries
  

The following IMPORTED targets are also defined:  


protobuf::libprotobuf
The protobuf library.
protobuf::libprotobuf-lite
The protobuf lite library.
protobuf::libprotoc
The protoc library.
protobuf::protoc
The protoc compiler.
  

The following cache variables are also available to set or use:  


Protobuf_LIBRARY
The protobuf library
Protobuf_PROTOC_LIBRARY
The protoc library
Protobuf_INCLUDE_DIR
The include directory for protocol buffers
Protobuf_PROTOC_EXECUTABLE
The protoc compiler
Protobuf_LIBRARY_DEBUG
The protobuf library (debug)
Protobuf_PROTOC_LIBRARY_DEBUG
The protoc library (debug)
Protobuf_LITE_LIBRARY
The protobuf lite library
Protobuf_LITE_LIBRARY_DEBUG
The protobuf lite library (debug)
  

Example:  

find_package(Protobuf REQUIRED)
include_directories(${Protobuf_INCLUDE_DIRS})
include_directories(${CMAKE_CURRENT_BINARY_DIR})
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS foo.proto)
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS EXPORT_MACRO DLL_EXPORT foo.proto)
protobuf_generate_cpp(PROTO_SRCS PROTO_HDRS DESCRIPTORS PROTO_DESCS foo.proto)
protobuf_generate_python(PROTO_PY foo.proto)
add_executable(bar bar.cc ${PROTO_SRCS} ${PROTO_HDRS})
target_link_libraries(bar ${Protobuf_LIBRARIES})

  


Note
The protobuf_generate_cpp and protobuf_generate_python
functions and add_executable() or add_library()
calls only work properly within the same directory.
  



protobuf_generate_cpp
Add custom commands to process .proto files to C++:
protobuf_generate_cpp (```<SRCS>``` ```<HDRS>```
    [DESCRIPTORS ```<DESC>```] [EXPORT_MACRO ```<MACRO>```] [```<ARGN>```...])



SRCS
Variable to define with autogenerated source files
HDRS
Variable to define with autogenerated header files
DESCRIPTORS
Variable to define with autogenerated descriptor files, if requested.
EXPORT_MACRO
is a macro which should expand to __declspec(dllexport) or
__declspec(dllimport) depending on what is being compiled.
ARGN
.proto files

  



protobuf_generate_python
Add custom commands to process .proto files to Python:
protobuf_generate_python (```<PY>``` [```<ARGN>```...])



PY
Variable to define with autogenerated Python files
ARGN
.proto filess

  
