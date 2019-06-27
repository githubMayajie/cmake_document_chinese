  

# DeployQt4  
Functions to help assemble a standalone Qt4 executable.  

A collection of CMake utility functions useful for deploying Qt4
executables.  

The following functions are provided by this module:  

write_qt4_conf
resolve_qt4_paths
fixup_qt4_executable
install_qt4_plugin_path
install_qt4_plugin
install_qt4_executable

  

Requires CMake 2.6 or greater because it uses function and
PARENT_SCOPE.  Also depends on BundleUtilities.cmake.  

write_qt4_conf(```<qt_conf_dir>``` ```<qt_conf_contents>```)

  

Writes a qt.conf file with the ```<qt_conf_contents>``` into ```<qt_conf_dir>```.  

resolve_qt4_paths(```<paths_var>``` [```<executable_path>```])

  

Loop through ```<paths_var>``` list and if any don¡¯t exist resolve them
relative to the ```<executable_path>``` (if supplied) or the
CMAKE_INSTALL_PREFIX.  

fixup_qt4_executable(```<executable>```
  [```<qtplugins>``` ```<libs>``` ```<dirs>``` ```<plugins_dir>``` ```<request_qt_conf>```])

  

Copies Qt plugins, writes a Qt configuration file (if needed) and
fixes up a Qt4 executable using BundleUtilities so it is standalone
and can be drag-and-drop copied to another machine as long as all of
the system libraries are compatible.  

```<executable>``` should point to the executable to be fixed-up.  

```<qtplugins>``` should contain a list of the names or paths of any Qt
plugins to be installed.  

```<libs>``` will be passed to BundleUtilities and should be a list of any
already installed plugins, libraries or executables to also be
fixed-up.  

```<dirs>``` will be passed to BundleUtilities and should contain and
directories to be searched to find library dependencies.  

```<plugins_dir>``` allows an custom plugins directory to be used.  

```<request_qt_conf>``` will force a qt.conf file to be written even if not
needed.  

install_qt4_plugin_path(plugin executable copy installed_plugin_path_var
                        ```<plugins_dir>``` ```<component>``` ```<configurations>```)

  

Install (or copy) a resolved ```<plugin>``` to the default plugins directory
(or ```<plugins_dir>```) relative to ```<executable>``` and store the result in
```<installed_plugin_path_var>```.  

If ```<copy>``` is set to TRUE then the plugins will be copied rather than
installed.  This is to allow this module to be used at CMake time
rather than install time.  

If ```<component>``` is set then anything installed will use this COMPONENT.  

install_qt4_plugin(plugin executable copy installed_plugin_path_var
                   ```<plugins_dir>``` ```<component>```)

  

Install (or copy) an unresolved ```<plugin>``` to the default plugins
directory (or ```<plugins_dir>```) relative to ```<executable>``` and store the
result in ```<installed_plugin_path_var>```.  See documentation of
INSTALL_QT4_PLUGIN_PATH.  

install_qt4_executable(```<executable>```
  [```<qtplugins>``` ```<libs>``` ```<dirs>``` ```<plugins_dir>``` ```<request_qt_conf>``` ```<component>```])

  

Installs Qt plugins, writes a Qt configuration file (if needed) and
fixes up a Qt4 executable using BundleUtilities so it is standalone
and can be drag-and-drop copied to another machine as long as all of
the system libraries are compatible.  The executable will be fixed-up
at install time.  ```<component>``` is the COMPONENT used for bundle fixup
and plugin installation.  See documentation of FIXUP_QT4_BUNDLE.  

