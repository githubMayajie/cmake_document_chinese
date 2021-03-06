  

# target_compile_definitions  
Add compile definitions to a target.  

target_compile_definitions(```<target>```
  ```<INTERFACE|PUBLIC|PRIVATE>``` [items1...]
  [```<INTERFACE|PUBLIC|PRIVATE>``` [items2...] ...])

  

Specifies compile definitions to use when compiling a given ```<target>```.  The
named ```<target>``` must have been created by a command such as
add_executable() or add_library() and must not be an
ALIAS target.  

The INTERFACE, PUBLIC and PRIVATE keywords are required to
specify the scope of the following arguments.  PRIVATE and PUBLIC
items will populate the COMPILE_DEFINITIONS property of
```<target>```. PUBLIC and INTERFACE items will populate the
INTERFACE_COMPILE_DEFINITIONS property of ```<target>```.
(IMPORTED targets only support INTERFACE items.)
The following arguments specify compile definitions.  Repeated calls for the
same ```<target>``` append items in the order called.  

Arguments to target_compile_definitions may use ˇ°generator expressionsˇ±
with the syntax $```<...>```.  See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  

Any leading -D on an item will be removed.  Empty items are ignored.
For example, the following are all equivalent:  

target_compile_definitions(foo PUBLIC FOO)
target_compile_definitions(foo PUBLIC -DFOO)  # -D removed
target_compile_definitions(foo PUBLIC "" FOO) # "" ignored
target_compile_definitions(foo PUBLIC -D FOO) # -D becomes "", then ignored

  

