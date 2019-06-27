  

# FindCURL  
Find the native CURL headers and libraries.  

This module accept optional COMPONENTS to check supported features and
protocols:  

PROTOCOLS: ICT FILE FTP FTPS GOPHER HTTP HTTPS IMAP IMAPS LDAP LDAPS POP3
           POP3S RTMP RTSP SCP SFTP SMB SMBS SMTP SMTPS TELNET TFTP
FEATURES:  SSL IPv6 UnixSockets libz AsynchDNS IDN GSS-API PSL SPNEGO
           Kerberos NTLM NTLM_WB TLS-SRP HTTP2 HTTPS-proxy

  


IMPORTED Targets
This module defines IMPORTED target CURL::libcurl, if
curl has been found.
  


Result Variables
This module defines the following variables:

CURL_FOUND
¡°True¡± if curl found.
CURL_INCLUDE_DIRS
where to find curl/curl.h, etc.
CURL_LIBRARIES
List of libraries when using curl.
CURL_VERSION_STRING
The version of curl found.

  

