  

# CPackIFW  
The documentation for the CPack IFW generator has moved here: CPack IFW Generator  

This module looks for the location of the command line utilities supplied
with the Qt Installer Framework (QtIFW).  

The module also defines several commands to control the behavior of the
CPack IFW generator.  


Commands
The module defines the following commands:


cpack_ifw_configure_component
Sets the arguments specific to the CPack IFW generator.
cpack_ifw_configure_component(```<compname>``` [COMMON] [ESSENTIAL] [VIRTUAL]
                    [FORCED_INSTALLATION] [REQUIRES_ADMIN_RIGHTS]
                    [NAME ```<name>```]
                    [DISPLAY_NAME ```<display_name>```] # Note: Internationalization supported
                    [DESCRIPTION ```<description>```] # Note: Internationalization supported
                    [UPDATE_TEXT ```<update_text>```]
                    [VERSION ```<version>```]
                    [RELEASE_DATE ```<release_date>```]
                    [SCRIPT ```<script>```]
                    [PRIORITY|SORTING_PRIORITY ```<sorting_priority>```] # Note: PRIORITY is deprecated
                    [DEPENDS|DEPENDENCIES ```<com_id>``` ...]
                    [AUTO_DEPEND_ON ```<comp_id>``` ...]
                    [LICENSES ```<display_name>``` ```<file_path>``` ...]
                    [DEFAULT ```<value>```]
                    [USER_INTERFACES ```<file_path>``` ```<file_path>``` ...]
                    [TRANSLATIONS ```<file_path>``` ```<file_path>``` ...]
                    [REPLACES ```<comp_id>``` ...]
                    [CHECKABLE ```<value>```])


This command should be called after cpack_add_component() command.

COMMON
if set, then the component will be packaged and installed as part
of a group to which it belongs.
ESSENTIAL
if set, then the package manager stays disabled until that
component is updated.
VIRTUAL
if set, then the component will be hidden from the installer.
It is a equivalent of the HIDDEN option from the
cpack_add_component() command.
FORCED_INSTALLATION
if set, then the component must always be installed.
It is a equivalent of the REQUARED option from the
cpack_add_component() command.
REQUIRES_ADMIN_RIGHTS
set it if the component needs to be installed with elevated permissions.
NAME
is used to create domain-like identification for this component.
By default used origin component name.
DISPLAY_NAME
set to rewrite original name configured by
cpack_add_component() command.
DESCRIPTION
set to rewrite original description configured by
cpack_add_component() command.
UPDATE_TEXT
will be added to the component description if this is an update to
the component.
VERSION
is version of component.
By default used CPACK_PACKAGE_VERSION.
RELEASE_DATE
keep empty to auto generate.
SCRIPT
is a relative or absolute path to operations script
for this component.
PRIORITY | SORTING_PRIORITY
is priority of the component in the tree.
The PRIORITY option is deprecated and will be removed in a future
version of CMake. Please use SORTING_PRIORITY option instead.
DEPENDS | DEPENDENCIES
list of dependency component or component group identifiers in
QtIFW style.
AUTO_DEPEND_ON
list of identifiers of component or component group in QtIFW style
that this component has an automatic dependency on.
LICENSES
pair of ```<display_name>``` and ```<file_path>``` of license text for this
component. You can specify more then one license.
DEFAULT
Possible values are: TRUE, FALSE, and SCRIPT.
Set to FALSE to disable the component in the installer or to SCRIPT
to resolved during runtime (don¡¯t forget add the file of the script
as a value of the SCRIPT option).
USER_INTERFACES
is a list of ```<file_path>``` (¡®.ui¡¯ files) representing pages to load.
TRANSLATIONS
is a list of ```<file_path>``` (¡®.qm¡¯ files) representing translations to load.
REPLACES
list of identifiers of component or component group to replace.
CHECKABLE
Possible values are: TRUE, FALSE.
Set to FALSE if you want to hide the checkbox for an item.
This is useful when only a few subcomponents should be selected
instead of all.




cpack_ifw_configure_component_group
Sets the arguments specific to the CPack IFW generator.
cpack_ifw_configure_component_group(```<groupname>``` [VIRTUAL]
                    [FORCED_INSTALLATION] [REQUIRES_ADMIN_RIGHTS]
                    [NAME ```<name>```]
                    [DISPLAY_NAME ```<display_name>```] # Note: Internationalization supported
                    [DESCRIPTION ```<description>```] # Note: Internationalization supported
                    [UPDATE_TEXT ```<update_text>```]
                    [VERSION ```<version>```]
                    [RELEASE_DATE ```<release_date>```]
                    [SCRIPT ```<script>```]
                    [PRIORITY|SORTING_PRIORITY ```<sorting_priority>```] # Note: PRIORITY is deprecated
                    [DEPENDS|DEPENDENCIES ```<com_id>``` ...]
                    [AUTO_DEPEND_ON ```<comp_id>``` ...]
                    [LICENSES ```<display_name>``` ```<file_path>``` ...]
                    [DEFAULT ```<value>```]
                    [USER_INTERFACES ```<file_path>``` ```<file_path>``` ...]
                    [TRANSLATIONS ```<file_path>``` ```<file_path>``` ...]
                    [REPLACES ```<comp_id>``` ...]
                    [CHECKABLE ```<value>```])


This command should be called after cpack_add_component_group()
command.

VIRTUAL
if set, then the group will be hidden from the installer.
Note that setting this on a root component does not work.
FORCED_INSTALLATION
if set, then the group must always be installed.
REQUIRES_ADMIN_RIGHTS
set it if the component group needs to be installed with elevated
permissions.
NAME
is used to create domain-like identification for this component group.
By default used origin component group name.
DISPLAY_NAME
set to rewrite original name configured by
cpack_add_component_group() command.
DESCRIPTION
set to rewrite original description configured by
cpack_add_component_group() command.
UPDATE_TEXT
will be added to the component group description if this is an update to
the component group.
VERSION
is version of component group.
By default used CPACK_PACKAGE_VERSION.
RELEASE_DATE
keep empty to auto generate.
SCRIPT
is a relative or absolute path to operations script
for this component group.
PRIORITY | SORTING_PRIORITY
is priority of the component group in the tree.
The PRIORITY option is deprecated and will be removed in a future
version of CMake. Please use SORTING_PRIORITY option instead.
DEPENDS | DEPENDENCIES
list of dependency component or component group identifiers in
QtIFW style.
AUTO_DEPEND_ON
list of identifiers of component or component group in QtIFW style
that this component group has an automatic dependency on.
LICENSES
pair of ```<display_name>``` and ```<file_path>``` of license text for this
component group. You can specify more then one license.
DEFAULT
Possible values are: TRUE, FALSE, and SCRIPT.
Set to TRUE to preselect the group in the installer
(this takes effect only on groups that have no visible child components)
or to SCRIPT to resolved during runtime (don¡¯t forget add the file of
the script as a value of the SCRIPT option).
USER_INTERFACES
is a list of ```<file_path>``` (¡®.ui¡¯ files) representing pages to load.
TRANSLATIONS
is a list of ```<file_path>``` (¡®.qm¡¯ files) representing translations to load.
REPLACES
list of identifiers of component or component group to replace.
CHECKABLE
Possible values are: TRUE, FALSE.
Set to FALSE if you want to hide the checkbox for an item.
This is useful when only a few subcomponents should be selected
instead of all.




cpack_ifw_add_repository
Add QtIFW specific remote repository to binary installer.
cpack_ifw_add_repository(```<reponame>``` [DISABLED]
                    URL ```<url>```
                    [USERNAME ```<username>```]
                    [PASSWORD ```<password>```]
                    [DISPLAY_NAME ```<display_name>```])


This command will also add the ```<reponame>``` repository
to a variable CPACK_IFW_REPOSITORIES_ALL.

DISABLED
if set, then the repository will be disabled by default.
URL
is points to a list of available components.
USERNAME
is used as user on a protected repository.
PASSWORD
is password to use on a protected repository.
DISPLAY_NAME
is string to display instead of the URL.




cpack_ifw_update_repository
Update QtIFW specific repository from remote repository.
cpack_ifw_update_repository(```<reponame>```
                    [[ADD|REMOVE] URL ```<url>```]|
                     [REPLACE OLD_URL ```<old_url>``` NEW_URL ```<new_url>```]]
                    [USERNAME ```<username>```]
                    [PASSWORD ```<password>```]
                    [DISPLAY_NAME ```<display_name>```])


This command will also add the ```<reponame>``` repository
to a variable CPACK_IFW_REPOSITORIES_ALL.

URL
is points to a list of available components.
OLD_URL
is points to a list that will replaced.
NEW_URL
is points to a list that will replace to.
USERNAME
is used as user on a protected repository.
PASSWORD
is password to use on a protected repository.
DISPLAY_NAME
is string to display instead of the URL.




cpack_ifw_add_package_resources
Add additional resources in the installer binary.
cpack_ifw_add_package_resources(```<file_path>``` ```<file_path>``` ...)


This command will also add the specified files
to a variable CPACK_IFW_PACKAGE_RESOURCES.

  

