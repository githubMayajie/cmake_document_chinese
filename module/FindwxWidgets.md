  

# FindwxWidgets  
Find a wxWidgets (a.k.a., wxWindows) installation.  

This module finds if wxWidgets is installed and selects a default
configuration to use.  wxWidgets is a modular library.  To specify the
modules that you will use, you need to name them as components to the
package:  

find_package(wxWidgets COMPONENTS core base бн OPTIONAL_COMPONENTS net бн)  

There are two search branches: a windows style and a unix style.  For
windows, the following variables are searched for and set to defaults
in case of multiple choices.  Change them if the defaults are not
desired (i.e., these are the only variables you should change to
select a configuration):  

wxWidgets_ROOT_DIR      - Base wxWidgets directory
                          (e.g., C:/wxWidgets-2.6.3).
wxWidgets_LIB_DIR       - Path to wxWidgets libraries
                          (e.g., C:/wxWidgets-2.6.3/lib/vc_lib).
wxWidgets_CONFIGURATION - Configuration to use
                          (e.g., msw, mswd, mswu, mswunivud, etc.)
wxWidgets_EXCLUDE_COMMON_LIBRARIES
                        - Set to TRUE to exclude linking of
                          commonly required libs (e.g., png tiff
                          jpeg zlib regex expat).

  

For unix style it uses the wx-config utility.  You can select between
debug/release, unicode/ansi, universal/non-universal, and
static/shared in the QtDialog or ccmake interfaces by turning ON/OFF
the following variables:  

wxWidgets_USE_DEBUG
wxWidgets_USE_UNICODE
wxWidgets_USE_UNIVERSAL
wxWidgets_USE_STATIC

  

There is also a wxWidgets_CONFIG_OPTIONS variable for all other
options that need to be passed to the wx-config utility.  For example,
to use the base toolkit found in the /usr/local path, set the variable
(before calling the FIND_PACKAGE command) as such:  

set(wxWidgets_CONFIG_OPTIONS --toolkit=base --prefix=/usr)

  

The following are set after the configuration is done for both windows
and unix style:  

wxWidgets_FOUND            - Set to TRUE if wxWidgets was found.
wxWidgets_INCLUDE_DIRS     - Include directories for WIN32
                             i.e., where to find "wx/wx.h" and
                             "wx/setup.h"; possibly empty for unices.
wxWidgets_LIBRARIES        - Path to the wxWidgets libraries.
wxWidgets_LIBRARY_DIRS     - compile time link dirs, useful for
                             rpath on UNIX. Typically an empty string
                             in WIN32 environment.
wxWidgets_DEFINITIONS      - Contains defines required to compile/link
                             against WX, e.g. WXUSINGDLL
wxWidgets_DEFINITIONS_DEBUG- Contains defines required to compile/link
                             against WX debug builds, e.g. __WXDEBUG__
wxWidgets_CXX_FLAGS        - Include dirs and compiler flags for
                             unices, empty on WIN32. Essentially
                             "`wx-config --cxxflags`".
wxWidgets_USE_FILE         - Convenience include file.

  

Sample usage:  

# Note that for MinGW users the order of libs is important!
find_package(wxWidgets COMPONENTS gl core base OPTIONAL_COMPONENTS net)
if(wxWidgets_FOUND)
  include(${wxWidgets_USE_FILE})
  # and for each of your dependent executable/library targets:
  target_link_libraries(```<YourTarget>``` ${wxWidgets_LIBRARIES})
endif()

  

If wxWidgets is required (i.e., not an optional part):  

find_package(wxWidgets REQUIRED gl core base OPTIONAL_COMPONENTS net)
include(${wxWidgets_USE_FILE})
# and for each of your dependent executable/library targets:
target_link_libraries(```<YourTarget>``` ${wxWidgets_LIBRARIES})

  

