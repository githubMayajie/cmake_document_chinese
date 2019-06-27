  

# INTERFACE_AUTOUIC_OPTIONS  
List of interface options to pass to uic.  

Targets may populate this property to publish the options
required to use when invoking uic.  Consuming targets can add entries to their
own AUTOUIC_OPTIONS property such as
$```<TARGET_PROPERTY:foo,INTERFACE_AUTOUIC_OPTIONS>``` to use the uic options
specified in the interface of foo. This is done automatically by
the target_link_libraries() command.  

This property supports generator expressions.  See the
cmake-generator-expressions(7) manual for available expressions.  

