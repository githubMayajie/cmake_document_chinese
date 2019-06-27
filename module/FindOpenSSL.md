  

# FindOpenSSL  
Find the OpenSSL encryption library.  


Optional COMPONENTS
This module supports two optional COMPONENTS: Crypto and SSL.  Both
components have associated imported targets, as described below.
  


Imported Targets
This module defines the following IMPORTED targets:

OpenSSL::SSL
The OpenSSL ssl library, if found.
OpenSSL::Crypto
The OpenSSL crypto library, if found.

  


Result Variables
This module will set the following variables in your project:

OPENSSL_FOUND
System has the OpenSSL library. If no components are requested it only
requires the crypto library.
OPENSSL_INCLUDE_DIR
The OpenSSL include directory.
OPENSSL_CRYPTO_LIBRARY
The OpenSSL crypto library.
OPENSSL_SSL_LIBRARY
The OpenSSL SSL library.
OPENSSL_LIBRARIES
All OpenSSL libraries.
OPENSSL_VERSION
This is set to $major.$minor.$revision$patch (e.g. 0.9.8s).

  


Hints
Set OPENSSL_ROOT_DIR to the root directory of an OpenSSL installation.
Set OPENSSL_USE_STATIC_LIBS to TRUE to look for static libraries.
Set OPENSSL_MSVC_STATIC_RT set TRUE to choose the MT version of the lib.
  

