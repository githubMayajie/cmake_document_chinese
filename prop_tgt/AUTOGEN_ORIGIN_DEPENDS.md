  

# AUTOGEN_ORIGIN_DEPENDS  
Switch for forwarding origin target dependencies to the corresponding
_autogen target.  

Targets which have their AUTOMOC or AUTOUIC property
ON have a corresponding _autogen target which generates
moc and uic files.  As this _autogen target is created at
generate-time, it is not possible to define dependencies of it using
e.g.  add_dependencies().  Instead the
AUTOGEN_ORIGIN_DEPENDS target property decides whether the origin
target dependencies should be forwarded to the _autogen target or not.  

By default AUTOGEN_ORIGIN_DEPENDS is initialized from
CMAKE_AUTOGEN_ORIGIN_DEPENDS which is ON by default.  

In total the dependencies of the _autogen target are composed from  


forwarded origin target dependencies
(enabled by default via AUTOGEN_ORIGIN_DEPENDS)
additional user defined dependencies from AUTOGEN_TARGET_DEPENDS
  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  


Note
Disabling AUTOGEN_ORIGIN_DEPENDS is useful to avoid building of
origin target dependencies when building the _autogen target only.
This is especially interesting when a
global autogen target is enabled.
When the _autogen target doesn¡¯t require all the origin target¡¯s
dependencies, and AUTOGEN_ORIGIN_DEPENDS is disabled, it might be
necessary to extend AUTOGEN_TARGET_DEPENDS to add missing
dependencies.
  

