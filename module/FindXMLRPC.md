  

# FindXMLRPC  
Find xmlrpc  

Find the native XMLRPC headers and libraries.  

XMLRPC_INCLUDE_DIRS      - where to find xmlrpc.h, etc.
XMLRPC_LIBRARIES         - List of libraries when using xmlrpc.
XMLRPC_FOUND             - True if xmlrpc found.

  

XMLRPC modules may be specified as components for this find module.
Modules may be listed by running ¡°xmlrpc-c-config¡±.  Modules include:  

c++            C++ wrapper code
libwww-client  libwww-based client
cgi-server     CGI-based server
abyss-server   ABYSS-based server

  

Typical usage:  

find_package(XMLRPC REQUIRED libwww-client)

  

