  

# CPackIFWConfigureFile  
The module defines configure_file() similar command to
configure file templates prepared in QtIFW/SDK/Creator style.  


Commands
The module defines the following commands:


cpack_ifw_configure_file
Copy a file to another location and modify its contents.
cpack_ifw_configure_file(```<input>``` ```<output>```)


Copies an ```<input>``` file to an ```<output>``` file and substitutes variable
values referenced as %{VAR} or %VAR% in the input file content.
Each variable reference will be replaced with the current value of the
variable, or the empty string if the variable is not defined.

  

