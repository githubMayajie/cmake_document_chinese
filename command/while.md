  

# while  
Evaluate a group of commands while a condition is true  

while(```<condition>```)
  ```<commands>```
endwhile()

  

All commands between while and the matching endwhile() are recorded
without being invoked.  Once the endwhile() is evaluated, the
recorded list of commands is invoked as long as the ```<condition>``` is true.  

The ```<condition>``` has the same syntax and is evaluated using the same logic
as described at length for the if() command.  

The commands break() and continue() provide means to
escape from the normal control flow.  

Per legacy, the endwhile() command admits
an optional ```<condition>``` argument.
If used, it must be a verbatim repeat of the argument of the opening
while command.  

