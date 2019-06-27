  

# CMAKE_EXPORT_PACKAGE_REGISTRY  
Enables the export(PACKAGE) command when CMP0090
is set to NEW.  

The export(PACKAGE) command does nothing by default.  In some cases
it is desirable to write to the user package registry, so the
CMAKE_EXPORT_PACKAGE_REGISTRY variable may be set to enable it.  

If CMP0090 is not set to NEW this variable does nothing, and
the CMAKE_EXPORT_NO_PACKAGE_REGISTRY variable controls the behavior
instead.  

See also Disabling the Package Registry.  

