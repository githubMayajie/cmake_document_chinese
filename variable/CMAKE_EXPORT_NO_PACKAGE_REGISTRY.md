  

# CMAKE_EXPORT_NO_PACKAGE_REGISTRY  
Disable the export(PACKAGE) command when CMP0090
is not set to NEW.  

In some cases, for example for packaging and for system wide
installations, it is not desirable to write the user package registry.
If the CMAKE_EXPORT_NO_PACKAGE_REGISTRY variable is enabled,
the export(PACKAGE) command will do nothing.  

If CMP0090 is set to NEW this variable does nothing, and the
CMAKE_EXPORT_PACKAGE_REGISTRY variable controls the behavior
instead.  

See also Disabling the Package Registry.  

