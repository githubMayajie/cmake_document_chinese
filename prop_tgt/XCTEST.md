  

# XCTEST  
This target is a XCTest CFBundle on the Mac.  

This property will usually get set via the xctest_add_bundle()
macro in FindXCTest module.  

If a module library target has this property set to true it will be
built as a CFBundle when built on the Mac.  It will have the directory
structure required for a CFBundle.  

This property depends on BUNDLE to be effective.  

