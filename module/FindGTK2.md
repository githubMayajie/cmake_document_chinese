  

# FindGTK2  
Find the GTK2 widget libraries and several of its
other optional components like gtkmm, glade, and glademm.  

NOTE: If you intend to use version checking, CMake 2.6.2 or later is  

required.

  

Specify one or more of the following components as you call this find
module.  See example below.  

gtk
gtkmm
glade
glademm

  

The following variables will be defined for your use  

GTK2_FOUND - Were all of your specified components found?
GTK2_INCLUDE_DIRS - All include directories
GTK2_LIBRARIES - All libraries
GTK2_TARGETS - All imported targets
GTK2_DEFINITIONS - Additional compiler flags

  

GTK2_VERSION - The version of GTK2 found (x.y.z)
GTK2_MAJOR_VERSION - The major version of GTK2
GTK2_MINOR_VERSION - The minor version of GTK2
GTK2_PATCH_VERSION - The patch version of GTK2

  

Optional variables you can define prior to calling this module:  

GTK2_DEBUG - Enables verbose debugging of the module
GTK2_ADDITIONAL_SUFFIXES - Allows defining additional directories to
                           search for include files

  

================= Example Usage:  

Call find_package() once, here are some examples to pick from:

  

Require GTK 2.6 or later
    find_package(GTK2 2.6 REQUIRED gtk)

  

Require GTK 2.10 or later and Glade
    find_package(GTK2 2.10 REQUIRED gtk glade)

  

Search for GTK/GTKMM 2.8 or later
    find_package(GTK2 2.8 COMPONENTS gtk gtkmm)

  

if(GTK2_FOUND)
   include_directories(${GTK2_INCLUDE_DIRS})
   add_executable(mygui mygui.cc)
   target_link_libraries(mygui ${GTK2_LIBRARIES})
endif()

  

