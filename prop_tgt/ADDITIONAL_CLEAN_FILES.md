  

# ADDITIONAL_CLEAN_FILES  
A ;-list of files or directories that will be
removed as a part of the global clean target.  It is useful for
specifying generated files or directories that are used by multiple targets
or by CMake itself, or that are generated in ways which cannot be captured as
outputs or byproducts of custom commands.  

If an additional clean file is specific to a single target only, then the
ADDITIONAL_CLEAN_FILES target property would usually be a better
choice than this directory property.  

Relative paths are allowed and are interpreted relative to the
current binary directory.  

Contents of ADDITIONAL_CLEAN_FILES may use
generator expressions.  

This property only works for the Ninja and the Makefile
generators.  It is ignored by other generators.  

