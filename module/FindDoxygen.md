  

# FindDoxygen  
Doxygen is a documentation generation tool (see http://www.doxygen.org).
This module looks for Doxygen and some optional tools it supports. These
tools are enabled as components in the find_package() command:  


dot
Graphviz dot utility used to render various
graphs.
mscgen
Message Chart Generator utility used
by Doxygen¡¯s \msc and \mscfile commands.
dia
Dia the diagram editor used by Doxygen¡¯s
\diafile command.
  

Examples:  

# Require dot, treat the other components as optional
find_package(Doxygen
             REQUIRED dot
             OPTIONAL_COMPONENTS mscgen dia)

  

The following variables are defined by this module:  



DOXYGEN_FOUND
True if the doxygen executable was found.
  



DOXYGEN_VERSION
The version reported by doxygen --version.
  

The module defines IMPORTED targets for Doxygen and each component found.
These can be used as part of custom commands, etc. and should be preferred over
old-style (and now deprecated) variables like DOXYGEN_EXECUTABLE. The
following import targets are defined if their corresponding executable could be
found (the component import targets will only be defined if that component was
requested):  

Doxygen::doxygen
Doxygen::dot
Doxygen::mscgen
Doxygen::dia

  


Functions


doxygen_add_docs
This function is intended as a convenience for adding a target for generating
documentation with Doxygen. It aims to provide sensible defaults so that
projects can generally just provide the input files and directories and that
will be sufficient to give sensible results. The function supports the
ability to customize the Doxygen configuration used to build the
documentation.
doxygen_add_docs(targetName
    [filesOrDirs...]
    [ALL]
    [WORKING_DIRECTORY dir]
    [COMMENT comment])


The function constructs a Doxyfile and defines a custom target that runs
Doxygen on that generated file. The listed files and directories are used as
the INPUT of the generated Doxyfile and they can contain wildcards.
Any files that are listed explicitly will also be added as SOURCES of the
custom target so they will show up in an IDE project¡¯s source list.
So that relative input paths work as expected, by default the working
directory of the Doxygen command will be the current source directory (i.e.
CMAKE_CURRENT_SOURCE_DIR). This can be overridden with the
WORKING_DIRECTORY option to change the directory used as the relative
base point. Note also that Doxygen¡¯s default behavior is to strip the working
directory from relative paths in the generated documentation (see the
STRIP_FROM_PATH Doxygen config option for details).
If provided, the optional comment will be passed as the COMMENT for
the add_custom_target() command used to create the custom target
internally.
If ALL is set, the target will be added to the default build target.
The contents of the generated Doxyfile can be customized by setting CMake
variables before calling doxygen_add_docs(). Any variable with a name of
the form DOXYGEN_```<tag>``` will have its value substituted for the
corresponding ```<tag>``` configuration option in the Doxyfile. See the
Doxygen documentation for the
full list of supported configuration options.
Some of Doxygen¡¯s defaults are overridden to provide more appropriate
behavior for a CMake project. Each of the following will be explicitly set
unless the variable already has a value before doxygen_add_docs() is
called (with some exceptions noted):


DOXYGEN_HAVE_DOT
Set to YES if the dot component was requested and it was found,
NO otherwise. Any existing value of DOXYGEN_HAVE_DOT is ignored.



DOXYGEN_DOT_MULTI_TARGETS
Set to YES by this module (note that this requires a dot version
newer than 1.8.10). This option is only meaningful if DOXYGEN_HAVE_DOT
is also set to YES.



DOXYGEN_GENERATE_LATEX
Set to NO by this module.



DOXYGEN_WARN_FORMAT
For Visual Studio based generators, this is set to the form recognized by
the Visual Studio IDE: $file($line) : $text. For all other generators,
Doxygen¡¯s default value is not overridden.



DOXYGEN_PROJECT_NAME
Populated with the name of the current project (i.e.
PROJECT_NAME).



DOXYGEN_PROJECT_NUMBER
Populated with the version of the current project (i.e.
PROJECT_VERSION).



DOXYGEN_PROJECT_BRIEF
Populated with the description of the current project (i.e.
PROJECT_DESCRIPTION).



DOXYGEN_INPUT
Projects should not set this variable. It will be populated with the set of
files and directories passed to doxygen_add_docs(), thereby providing
consistent behavior with the other built-in commands like
add_executable(), add_library() and
add_custom_target(). If a variable named DOXYGEN_INPUT is set
by the project, it will be ignored and a warning will be issued.



DOXYGEN_RECURSIVE
Set to YES by this module.



DOXYGEN_EXCLUDE_PATTERNS
If the set of inputs includes directories, this variable will specify
patterns used to exclude files from them. The following patterns are added
by doxygen_add_docs() to ensure CMake-specific files and directories
are not included in the input. If the project sets
DOXYGEN_EXCLUDE_PATTERNS, those contents are merged with these
additional patterns rather than replacing them:
*/.git/*
*/.svn/*
*/.hg/*
*/CMakeFiles/*
*/_CPack_Packages/*
DartConfiguration.tcl
CMakeLists.txt
CMakeCache.txt





DOXYGEN_OUTPUT_DIRECTORY
Set to CMAKE_CURRENT_BINARY_DIR by this module. Note that if
the project provides its own value for this and it is a relative path, it
will be converted to an absolute path relative to the current binary
directory. This is necessary because doxygen will normally be run from a
directory within the source tree so that relative source paths work as
expected. If this directory does not exist, it will be recursively created
prior to executing the doxygen commands.


To change any of these defaults or override any other Doxygen config option,
set relevant variables before calling doxygen_add_docs(). For example:

set(DOXYGEN_GENERATE_HTML NO)
set(DOXYGEN_GENERATE_MAN YES)

doxygen_add_docs(
    doxygen
    ${PROJECT_SOURCE_DIR}
    COMMENT "Generate man pages"
)



A number of Doxygen config options accept lists of values, but Doxygen requires
them to be separated by whitespace. CMake variables hold lists as a string with
items separated by semi-colons, so a conversion needs to be performed. The
doxygen_add_docs() command specifically checks the following Doxygen config
options and will convert their associated CMake variable¡¯s contents into the
required form if set.
ABBREVIATE_BRIEF
ALIASES
CITE_BIB_FILES
DIAFILE_DIRS
DOTFILE_DIRS
DOT_FONTPATH
ENABLED_SECTIONS
EXAMPLE_PATH
EXAMPLE_PATTERNS
EXCLUDE
EXCLUDE_PATTERNS
EXCLUDE_SYMBOLS
EXPAND_AS_DEFINED
EXTENSION_MAPPING
EXTRA_PACKAGES
EXTRA_SEARCH_MAPPINGS
FILE_PATTERNS
FILTER_PATTERNS
FILTER_SOURCE_PATTERNS
HTML_EXTRA_FILES
HTML_EXTRA_STYLESHEET
IGNORE_PREFIX
IMAGE_PATH
INCLUDE_FILE_PATTERNS
INCLUDE_PATH
INPUT
LATEX_EXTRA_FILES
LATEX_EXTRA_STYLESHEET
MATHJAX_EXTENSIONS
MSCFILE_DIRS
PLANTUML_INCLUDE_PATH
PREDEFINED
QHP_CUST_FILTER_ATTRS
QHP_SECT_FILTER_ATTRS
STRIP_FROM_INC_PATH
STRIP_FROM_PATH
TAGFILES
TCL_SUBST


The following single value Doxygen options will be quoted automatically
if they contain at least one space:
CHM_FILE
DIA_PATH
DOCBOOK_OUTPUT
DOCSET_FEEDNAME
DOCSET_PUBLISHER_NAME
DOT_FONTNAME
DOT_PATH
EXTERNAL_SEARCH_ID
FILE_VERSION_FILTER
GENERATE_TAGFILE
HHC_LOCATION
HTML_FOOTER
HTML_HEADER
HTML_OUTPUT
HTML_STYLESHEET
INPUT_FILTER
LATEX_FOOTER
LATEX_HEADER
LATEX_OUTPUT
LAYOUT_FILE
MAN_OUTPUT
MAN_SUBDIR
MATHJAX_CODEFILE
MSCGEN_PATH
OUTPUT_DIRECTORY
PERL_PATH
PLANTUML_JAR_PATH
PROJECT_BRIEF
PROJECT_LOGO
PROJECT_NAME
QCH_FILE
QHG_LOCATION
QHP_CUST_FILTER_NAME
QHP_VIRTUAL_FOLDER
RTF_EXTENSIONS_FILE
RTF_OUTPUT
RTF_STYLESHEET_FILE
SEARCHDATA_FILE
USE_MDFILE_AS_MAINPAGE
WARN_FORMAT
WARN_LOGFILE
XML_OUTPUT


There are situations where it may be undesirable for a particular config option
to be automatically quoted by doxygen_add_docs(), such as ALIASES which
may need to include its own embedded quoting.  The DOXYGEN_VERBATIM_VARS
variable can be used to specify a list of Doxygen variables (including the
leading DOXYGEN_ prefix) which should not be quoted.  The project is then
responsible for ensuring that those variables¡¯ values make sense when placed
directly in the Doxygen input file.  In the case of list variables, list items
are still separated by spaces, it is only the automatic quoting that is
skipped.  For example, the following allows doxygen_add_docs() to apply
quoting to DOXYGEN_PROJECT_BRIEF, but not each item in the
DOXYGEN_ALIASES list (bracket syntax can also
be used to make working with embedded quotes easier):
set(DOXYGEN_PROJECT_BRIEF "String with spaces")
set(DOXYGEN_ALIASES
    [[somealias="@some_command param"]]
    "anotherAlias=@foobar"
)
set(DOXYGEN_VERBATIM_VARS DOXYGEN_ALIASES)


The resultant Doxyfile will contain the following lines:
PROJECT_BRIEF = "String with spaces"
ALIASES       = somealias="@some_command param" anotherAlias=@foobar


  


Deprecated Result Variables
For compatibility with previous versions of CMake, the following variables
are also defined but they are deprecated and should no longer be used:


DOXYGEN_EXECUTABLE
The path to the doxygen command. If projects need to refer to the
doxygen executable directly, they should use the Doxygen::doxygen
import target instead.



DOXYGEN_DOT_FOUND
True if the dot executable was found.



DOXYGEN_DOT_EXECUTABLE
The path to the dot command. If projects need to refer to the dot
executable directly, they should use the Doxygen::dot import target
instead.



DOXYGEN_DOT_PATH
The path to the directory containing the dot executable as reported in
DOXYGEN_DOT_EXECUTABLE. The path may have forward slashes even on Windows
and is not suitable for direct substitution into a Doxyfile.in template.
If you need this value, get the IMPORTED_LOCATION property of the
Doxygen::dot target and use get_filename_component() to extract
the directory part of that path. You may also want to consider using
file(TO_NATIVE_PATH) to prepare the path for a Doxygen
configuration file.

  


Deprecated Hint Variables


DOXYGEN_SKIP_DOT
This variable has no effect for the component form of find_package.
In backward compatibility mode (i.e. without components list) it prevents
the finder module from searching for Graphviz¡¯s dot utility.

  

