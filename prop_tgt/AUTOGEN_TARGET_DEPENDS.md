  

# AUTOGEN_TARGET_DEPENDS  
Additional target dependencies of the corresponding _autogen target.  

Targets which have their AUTOMOC or AUTOUIC property
ON have a corresponding _autogen target which generates
moc and uic files.  As this _autogen target is created at
generate-time, it is not possible to define dependencies of it using
e.g.  add_dependencies().  Instead the
AUTOGEN_TARGET_DEPENDS target property can be set to a
;-list of additional dependencies for the
_autogen target.  Dependencies can be target names or file names.  

In total the dependencies of the _autogen target are composed from  


forwarded origin target dependencies
(enabled by default via AUTOGEN_ORIGIN_DEPENDS)
additional user defined dependencies from AUTOGEN_TARGET_DEPENDS
  

See the cmake-qt(7) manual for more information on using CMake
with Qt.  


Use cases
If AUTOMOC or AUTOUIC depends on a file that is either

a GENERATED non C++ file (e.g. a GENERATED .json
or .ui file) or
a GENERATED C++ file that isn¡¯t recognized by AUTOMOC
and AUTOUIC because it¡¯s skipped by SKIP_AUTOMOC,
SKIP_AUTOUIC, SKIP_AUTOGEN or CMP0071 or
a file that isn¡¯t in the origin target¡¯s sources

it must added to AUTOGEN_TARGET_DEPENDS.
  

