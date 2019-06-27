  

# ExternalData  

Contents

ExternalData
Introduction
Module Functions
Module Variables
Referencing Files
Referencing Single Files
Referencing File Series
Referencing Associated Files
Referencing Directories


Hash Algorithms
Custom Fetch Scripts



  

Manage data files stored outside source tree  


Introduction
Use this module to unambiguously reference data files stored outside
the source tree and fetch them at build time from arbitrary local and
remote content-addressed locations.  Functions provided by this module
recognize arguments with the syntax DATA{```<name>```} as references to
external data, replace them with full paths to local copies of those
data, and create build rules to fetch and update the local copies.
For example:
include(ExternalData)
set(ExternalData_URL_TEMPLATES "file:///local/%(algo)/%(hash)"
                               "file:////host/share/%(algo)/%(hash)"
                               "http://data.org/%(algo)/%(hash)")
ExternalData_Add_Test(MyData
  NAME MyTest
  COMMAND MyExe DATA{MyInput.png}
  )
ExternalData_Add_Target(MyData)


When test MyTest runs the DATA{MyInput.png} argument will be
replaced by the full path to a real instance of the data file
MyInput.png on disk.  If the source tree contains a content link
such as MyInput.png.md5 then the MyData target creates a real
MyInput.png in the build tree.
  


Module Functions


ExternalData_Expand_Arguments
The ExternalData_Expand_Arguments function evaluates DATA{}
references in its arguments and constructs a new list of arguments:
ExternalData_Expand_Arguments(
  ```<target>```   # Name of data management target
  ```<outVar>```   # Output variable
  [args...]  # Input arguments, DATA{} allowed
  )


It replaces each DATA{} reference in an argument with the full path of
a real data file on disk that will exist after the ```<target>``` builds.



ExternalData_Add_Test
The ExternalData_Add_Test function wraps around the CMake
add_test() command but supports DATA{} references in
its arguments:
ExternalData_Add_Test(
  ```<target>```   # Name of data management target
  ...        # Arguments of add_test(), DATA{} allowed
  )


It passes its arguments through ExternalData_Expand_Arguments and then
invokes the add_test() command using the results.



ExternalData_Add_Target
The ExternalData_Add_Target function creates a custom target to
manage local instances of data files stored externally:
ExternalData_Add_Target(
  ```<target>```   # Name of data management target
  )


It creates custom commands in the target as necessary to make data
files available for each DATA{} reference previously evaluated by
other functions provided by this module.
Data files may be fetched from one of the URL templates specified in
the ExternalData_URL_TEMPLATES variable, or may be found locally
in one of the paths specified in the ExternalData_OBJECT_STORES
variable.
Typically only one target is needed to manage all external data within
a project.  Call this function once at the end of configuration after
all data references have been processed.

  


Module Variables
The following variables configure behavior.  They should be set before
calling any of the functions provided by this module.


ExternalData_BINARY_ROOT
The ExternalData_BINARY_ROOT variable may be set to the directory to
hold the real data files named by expanded DATA{} references.  The
default is CMAKE_BINARY_DIR.  The directory layout will mirror that of
content links under ExternalData_SOURCE_ROOT.



ExternalData_CUSTOM_SCRIPT_```<key>```
Specify a full path to a .cmake custom fetch script identified by
```<key>``` in entries of the ExternalData_URL_TEMPLATES list.
See Custom Fetch Scripts.



ExternalData_LINK_CONTENT
The ExternalData_LINK_CONTENT variable may be set to the name of a
supported hash algorithm to enable automatic conversion of real data
files referenced by the DATA{} syntax into content links.  For each
such ```<file>``` a content link named ```<file>``````<ext>``` is created.  The
original file is renamed to the form .ExternalData_```<algo>```_```<hash>``` to
stage it for future transmission to one of the locations in the list
of URL templates (by means outside the scope of this module).  The
data fetch rule created for the content link will use the staged
object if it cannot be found using any URL template.



ExternalData_NO_SYMLINKS
The real data files named by expanded DATA{} references may be made
available under ExternalData_BINARY_ROOT using symbolic links on
some platforms.  The ExternalData_NO_SYMLINKS variable may be set
to disable use of symbolic links and enable use of copies instead.



ExternalData_OBJECT_STORES
The ExternalData_OBJECT_STORES variable may be set to a list of local
directories that store objects using the layout ```<dir>```/%(algo)/%(hash).
These directories will be searched first for a needed object.  If the
object is not available in any store then it will be fetched remotely
using the URL templates and added to the first local store listed.  If
no stores are specified the default is a location inside the build
tree.



ExternalData_SERIES_PARSE

ExternalData_SERIES_PARSE_PREFIX

ExternalData_SERIES_PARSE_NUMBER

ExternalData_SERIES_PARSE_SUFFIX

ExternalData_SERIES_MATCH
See Referencing File Series.



ExternalData_SOURCE_ROOT
The ExternalData_SOURCE_ROOT variable may be set to the highest source
directory containing any path named by a DATA{} reference.  The
default is CMAKE_SOURCE_DIR.  ExternalData_SOURCE_ROOT and
CMAKE_SOURCE_DIR must refer to directories within a single source
distribution (e.g.  they come together in one tarball).



ExternalData_TIMEOUT_ABSOLUTE
The ExternalData_TIMEOUT_ABSOLUTE variable sets the download
absolute timeout, in seconds, with a default of 300 seconds.
Set to 0 to disable enforcement.



ExternalData_TIMEOUT_INACTIVITY
The ExternalData_TIMEOUT_INACTIVITY variable sets the download
inactivity timeout, in seconds, with a default of 60 seconds.
Set to 0 to disable enforcement.



ExternalData_URL_ALGO_```<algo>```_```<key>```
Specify a custom URL component to be substituted for URL template
placeholders of the form %(algo:```<key>```), where ```<key>``` is a
valid C identifier, when fetching an object referenced via hash
algorithm ```<algo>```.  If not defined, the default URL component
is just ```<algo>``` for any ```<key>```.



ExternalData_URL_TEMPLATES
The ExternalData_URL_TEMPLATES may be set to provide a list of
of URL templates using the placeholders %(algo) and %(hash)
in each template.  Data fetch rules try each URL template in order
by substituting the hash algorithm name for %(algo) and the hash
value for %(hash).  Alternatively one may use %(algo:```<key>```)
with ExternalData_URL_ALGO_```<algo>```_```<key>``` variables to gain more
flexibility in remote URLs.

  


Referencing Files

Referencing Single Files
The DATA{} syntax is literal and the ```<name>``` is a full or relative path
within the source tree.  The source tree must contain either a real
data file at ```<name>``` or a ¡°content link¡± at ```<name>``````<ext>``` containing a
hash of the real file using a hash algorithm corresponding to ```<ext>```.
For example, the argument DATA{img.png} may be satisfied by either a
real img.png file in the current source directory or a img.png.md5
file containing its MD5 sum.
Multiple content links of the same name with different hash algorithms
are supported (e.g. img.png.sha256 and img.png.sha1) so long as
they all correspond to the same real file.  This allows objects to be
fetched from sources indexed by different hash algorithms.


Referencing File Series
The DATA{} syntax can be told to fetch a file series using the form
DATA{```<name>```,:}, where the : is literal.  If the source tree
contains a group of files or content links named like a series then a
reference to one member adds rules to fetch all of them.  Although all
members of a series are fetched, only the file originally named by the
DATA{} argument is substituted for it.  The default configuration
recognizes file series names ending with #.ext, _#.ext, .#.ext,
or -#.ext where # is a sequence of decimal digits and .ext is
any single extension.  Configure it with a regex that parses ```<number>```
and ```<suffix>``` parts from the end of ```<name>```:
ExternalData_SERIES_PARSE = regex of the form (```<number>```)(```<suffix>```)$


For more complicated cases set:
ExternalData_SERIES_PARSE = regex with at least two () groups
ExternalData_SERIES_PARSE_PREFIX = ```<prefix>``` regex group number, if any
ExternalData_SERIES_PARSE_NUMBER = ```<number>``` regex group number
ExternalData_SERIES_PARSE_SUFFIX = ```<suffix>``` regex group number


Configure series number matching with a regex that matches the
```<number>``` part of series members named ```<prefix>``````<number>``````<suffix>```:
ExternalData_SERIES_MATCH = regex matching ```<number>``` in all series members


Note that the ```<suffix>``` of a series does not include a hash-algorithm
extension.


Referencing Associated Files
The DATA{} syntax can alternatively match files associated with the
named file and contained in the same directory.  Associated files may
be specified by options using the syntax
DATA{```<name>```,```<opt1>```,```<opt2>```,...}.  Each option may specify one file by
name or specify a regular expression to match file names using the
syntax REGEX:```<regex>```.  For example, the arguments:
DATA{MyData/MyInput.mhd,MyInput.img}                   # File pair
DATA{MyData/MyFrames00.png,REGEX:MyFrames[0-9]+\\.png} # Series


will pass MyInput.mha and MyFrames00.png on the command line but
ensure that the associated files are present next to them.


Referencing Directories
The DATA{} syntax may reference a directory using a trailing slash and
a list of associated files.  The form DATA{```<name>```/,```<opt1>```,```<opt2>```,...}
adds rules to fetch any files in the directory that match one of the
associated file options.  For example, the argument
DATA{MyDataDir/,REGEX:.*} will pass the full path to a MyDataDir
directory on the command line and ensure that the directory contains
files corresponding to every file or content link in the MyDataDir
source directory.  In order to match associated files in subdirectories,
specify a RECURSE: option, e.g. DATA{MyDataDir/,RECURSE:,REGEX:.*}.

  


Hash Algorithms
The following hash algorithms are supported:
%(algo)     ```<ext>```     Description
-------     -----     -----------
MD5         .md5      Message-Digest Algorithm 5, RFC 1321
SHA1        .sha1     US Secure Hash Algorithm 1, RFC 3174
SHA224      .sha224   US Secure Hash Algorithms, RFC 4634
SHA256      .sha256   US Secure Hash Algorithms, RFC 4634
SHA384      .sha384   US Secure Hash Algorithms, RFC 4634
SHA512      .sha512   US Secure Hash Algorithms, RFC 4634
SHA3_224    .sha3-224 Keccak SHA-3
SHA3_256    .sha3-256 Keccak SHA-3
SHA3_384    .sha3-384 Keccak SHA-3
SHA3_512    .sha3-512 Keccak SHA-3


Note that the hashes are used only for unique data identification and
download verification.
  


Custom Fetch Scripts
When a data file must be fetched from one of the URL templates
specified in the ExternalData_URL_TEMPLATES variable, it is
normally downloaded using the file(DOWNLOAD) command.
One may specify usage of a custom fetch script by using a URL
template of the form ExternalDataCustomScript://```<key>```/```<loc>```.
The ```<key>``` must be a C identifier, and the ```<loc>``` must
contain the %(algo) and %(hash) placeholders.
A variable corresponding to the key, ExternalData_CUSTOM_SCRIPT_```<key>```,
must be set to the full path to a .cmake script file.  The script
will be included to perform the actual fetch, and provided with
the following variables:


ExternalData_CUSTOM_LOCATION
When a custom fetch script is loaded, this variable is set to the
location part of the URL, which will contain the substituted hash
algorithm name and content hash value.



ExternalData_CUSTOM_FILE
When a custom fetch script is loaded, this variable is set to the
full path to a file in which the script must store the fetched
content.  The name of the file is unspecified and should not be
interpreted in any way.

The custom fetch script is expected to store fetched content in the
file or set a variable:


ExternalData_CUSTOM_ERROR
When a custom fetch script fails to fetch the requested content,
it must set this variable to a short one-line message describing
the reason for failure.

  

