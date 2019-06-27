  

# CMakeGraphVizOptions  
The builtin graphviz support of CMake.  


Variables specific to the graphviz support
CMake
can generate graphviz files, showing the dependencies between the
targets in a project and also external libraries which are linked
against.  When CMake is run with the --graphviz=foo.dot option, it will
produce:

a foo.dot file showing all dependencies in the project
a foo.dot.```<target>``` file for each target, file showing on which other targets the respective target depends
a foo.dot.```<target>```.dependers file, showing which other targets depend on the respective target

The different dependency types PUBLIC, PRIVATE and INTERFACE
are represented as solid, dashed and dotted edges.
This can result in huge graphs.  Using the file
CMakeGraphVizOptions.cmake the look and content of the generated
graphs can be influenced.  This file is searched first in
CMAKE_BINARY_DIR and then in CMAKE_SOURCE_DIR.  If found, it is
read and the variables set in it are used to adjust options for the
generated graphviz files.


GRAPHVIZ_GRAPH_TYPE
The graph type.

Mandatory : NO
Default   : ¡°digraph¡±

Valid graph types are:

¡°graph¡± : Nodes are joined with lines
¡°digraph¡± : Nodes are joined with arrows showing direction
¡°strict graph¡± : Like ¡°graph¡± but max one line between each node
¡°strict digraph¡± : Like ¡°graph¡± but max one line between each node in each direction




GRAPHVIZ_GRAPH_NAME
The graph name.

Mandatory : NO
Default   : ¡°GG¡±




GRAPHVIZ_GRAPH_HEADER
The header written at the top of the graphviz file.

Mandatory : NO
Default   : ¡°node [n  fontsize = ¡°12¡±];¡±




GRAPHVIZ_NODE_PREFIX
The prefix for each node in the graphviz file.

Mandatory : NO
Default   : ¡°node¡±




GRAPHVIZ_EXECUTABLES
Set this to FALSE to exclude executables from the generated graphs.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_STATIC_LIBS
Set this to FALSE to exclude static libraries from the generated graphs.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_SHARED_LIBS
Set this to FALSE to exclude shared libraries from the generated graphs.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_MODULE_LIBS
Set this to FALSE to exclude module libraries from the generated graphs.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_EXTERNAL_LIBS
Set this to FALSE to exclude external libraries from the generated graphs.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_IGNORE_TARGETS
A list of regular expressions for ignoring targets.

Mandatory : NO
Default   : empty




GRAPHVIZ_GENERATE_PER_TARGET
Set this to FALSE to exclude per target graphs foo.dot.```<target>```.

Mandatory : NO
Default   : TRUE




GRAPHVIZ_GENERATE_DEPENDERS
Set this to FALSE to exclude depender graphs foo.dot.```<target>```.dependers.

Mandatory : NO
Default   : TRUE


  

