  

# target_sources  
Add sources to a target.  

target_sources(```<target>```
  ```<INTERFACE|PUBLIC|PRIVATE>``` [items1...]
  [```<INTERFACE|PUBLIC|PRIVATE>``` [items2...] ...])

  

Specifies sources to use when compiling a given target.  Relative
source file paths are interpreted as being relative to the current
source directory (i.e. CMAKE_CURRENT_SOURCE_DIR).  The
named ```<target>``` must have been created by a command such as
add_executable() or add_library() and must not be an
ALIAS target.  

The INTERFACE, PUBLIC and PRIVATE keywords are required to
specify the scope of the following arguments.  PRIVATE and PUBLIC
items will populate the SOURCES property of
```<target>```.  PUBLIC and INTERFACE items will populate the
INTERFACE_SOURCES property of ```<target>```.
(IMPORTED targets only support INTERFACE items.)
The following arguments specify sources.  Repeated calls for the same
```<target>``` append items in the order called.  

Arguments to target_sources may use ˇ°generator expressionsˇ±
with the syntax $```<...>```. See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  

See also the CMP0076 policy for older behavior related to the
handling of relative source file paths.  

