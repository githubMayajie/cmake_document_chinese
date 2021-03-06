  

# target_link_directories  
Add link directories to a target.  

target_link_directories(```<target>``` [BEFORE]
  ```<INTERFACE|PUBLIC|PRIVATE>``` [items1...]
  [```<INTERFACE|PUBLIC|PRIVATE>``` [items2...] ...])

  

Specifies the paths in which the linker should search for libraries when
linking a given target.  Each item can be an absolute or relative path,
with the latter being interpreted as relative to the current source
directory.  These items will be added to the link command.  

The named ```<target>``` must have been created by a command such as
add_executable() or add_library() and must not be an
ALIAS target.  

The INTERFACE, PUBLIC and PRIVATE keywords are required to
specify the scope of the items that follow them.  PRIVATE and
PUBLIC items will populate the LINK_DIRECTORIES property
of ```<target>```.  PUBLIC and INTERFACE items will populate the
INTERFACE_LINK_DIRECTORIES property of ```<target>```
(IMPORTED targets only support INTERFACE items).
Each item specifies a link directory and will be converted to an absolute
path if necessary before adding it to the relevant property.  Repeated
calls for the same ```<target>``` append items in the order called.  

If BEFORE is specified, the content will be prepended to the relevant
property instead of being appended.  

Arguments to target_link_directories may use ˇ°generator expressionsˇ±
with the syntax $```<...>```. See the cmake-generator-expressions(7)
manual for available expressions.  See the cmake-buildsystem(7)
manual for more on defining buildsystem properties.  


Note
This command is rarely necessary and should be avoided where there are
other choices.  Prefer to pass full absolute paths to libraries where
possible, since this ensures the correct library will always be linked.
The find_library() command provides the full path, which can
generally be used directly in calls to target_link_libraries().
Situations where a library search path may be needed include:

Project generators like Xcode where the user can switch target
architecture at build time, but a full path to a library cannot
be used because it only provides one architecture (i.e. it is not
a universal binary).
Libraries may themselves have other private library dependencies
that expect to be found via RPATH mechanisms, but some linkers
are not able to fully decode those paths (e.g. due to the presence
of things like $ORIGIN).

  

