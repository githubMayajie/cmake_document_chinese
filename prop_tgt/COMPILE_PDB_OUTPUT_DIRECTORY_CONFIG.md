  

# COMPILE_PDB_OUTPUT_DIRECTORY_```<CONFIG>```  
Per-configuration output directory for the MS debug symbol .pdb file
generated by the compiler while building source files.  

This is a per-configuration version of
COMPILE_PDB_OUTPUT_DIRECTORY,
but multi-configuration generators (Visual Studio, Xcode) do NOT append a
per-configuration subdirectory to the specified directory.  This
property is initialized by the value of the
CMAKE_COMPILE_PDB_OUTPUT_DIRECTORY_```<CONFIG>``` variable
if it is set when a target is created.  


Note
The compiler-generated program database files are specified by the
/Fd compiler flag and are not the same as linker-generated
program database files specified by the /pdb linker flag.
Use the PDB_OUTPUT_DIRECTORY_```<CONFIG>``` property to specify the latter.
  

