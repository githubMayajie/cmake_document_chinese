  

# set_target_properties  
Targets can have properties that affect how they are built.  

set_target_properties(target1 target2 ...
                      PROPERTIES prop1 value1
                      prop2 value2 ...)

  

Sets properties on targets.  The syntax for the command is to list all
the targets you want to change, and then provide the values you want to
set next.  You can use any prop value pair you want and extract it
later with the get_property() or get_target_property()
command.  

See also the set_property(TARGET) command.  

See Properties on Targets for the list of properties known to CMake.  

