  

# FindBLAS  
Find Basic Linear Algebra Subprograms (BLAS) library  

This module finds an installed Fortran library that implements the
BLAS linear-algebra interface (see http://www.netlib.org/blas/).  The
list of libraries searched for is taken from the autoconf macro file,
acx_blas.m4 (distributed at
http://ac-archive.sourceforge.net/ac-archive/acx_blas.html).  


Input Variables
The following variables may be set to influence this module¡¯s behavior:

BLA_STATIC
if ON use static linkage
BLA_VENDOR
If set, checks only the specified vendor, if not set checks all the
possibilities.  List of vendors valid in this module:

Goto
OpenBLAS
FLAME
ATLAS PhiPACK
CXML
DXML
SunPerf
SCSL
SGIMATH
IBMESSL
Intel10_32 (intel mkl v10 32 bit)
Intel10_64lp (intel mkl v10+ 64 bit, threaded code, lp64 model)
Intel10_64lp_seq (intel mkl v10+ 64 bit, sequential code, lp64 model)
Intel10_64ilp (intel mkl v10+ 64 bit, threaded code, ilp64 model)
Intel10_64ilp_seq (intel mkl v10+ 64 bit, sequential code, ilp64 model)
Intel (obsolete versions of mkl 32 and 64 bit)
ACML
ACML_MP
ACML_GPU
Apple
NAS
Generic


BLA_F95
if ON tries to find the BLAS95 interfaces
BLA_PREFER_PKGCONFIG
if set pkg-config will be used to search for a BLAS library first
and if one is found that is preferred

  


Result Variables
This module defines the following variables:

BLAS_FOUND
library implementing the BLAS interface is found
BLAS_LINKER_FLAGS
uncached list of required linker flags (excluding -l and -L).
BLAS_LIBRARIES
uncached list of libraries (using full path name) to link against
to use BLAS (may be empty if compiler implicitly links BLAS)
BLAS95_LIBRARIES
uncached list of libraries (using full path name) to link against
to use BLAS95 interface
BLAS95_FOUND
library implementing the BLAS95 interface is found


Note
C or CXX must be enabled to use Intel Math Kernel Library (MKL)
For example, to use Intel MKL libraries and/or Intel compiler:
set(BLA_VENDOR Intel10_64lp)
find_package(BLAS)



  


Hints
Set MKLROOT environment variable to a directory that contains an MKL
installation.
  

