  

# FindLAPACK  
Find Linear Algebra PACKage (LAPACK) library  

This module finds an installed fortran library that implements the
LAPACK linear-algebra interface (see http://www.netlib.org/lapack/).  

The approach follows that taken for the autoconf macro file,
acx_lapack.m4 (distributed at
http://ac-archive.sourceforge.net/ac-archive/acx_lapack.html).  


Input Variables
The following variables may be set to influence this module¡¯s behavior:

BLA_STATIC
if ON use static linkage
BLA_VENDOR
If set, checks only the specified vendor, if not set checks all the
possibilities.  List of vendors valid in this module:

Intel10_32 (intel mkl v10 32 bit)
Intel10_64lp (intel mkl v10+ 64 bit, threaded code, lp64 model)
Intel10_64lp_seq (intel mkl v10+ 64 bit, sequential code, lp64 model)
Intel10_64ilp (intel mkl v10+ 64 bit, threaded code, ilp64 model)
Intel10_64ilp_seq (intel mkl v10+ 64 bit, sequential code, ilp64 model)
Intel (obsolete versions of mkl 32 and 64 bit)
OpenBLAS
FLAME
ACML
Apple
NAS
Generic


BLA_F95
if ON tries to find BLAS95/LAPACK95

  


Result Variables
This module defines the following variables:

LAPACK_FOUND
library implementing the LAPACK interface is found
LAPACK_LINKER_FLAGS
uncached list of required linker flags (excluding -l and -L).
LAPACK_LIBRARIES
uncached list of libraries (using full path name) to link against
to use LAPACK
LAPACK95_LIBRARIES
uncached list of libraries (using full path name) to link against
to use LAPACK95
LAPACK95_FOUND
library implementing the LAPACK95 interface is found


Note
C or CXX must be enabled to use Intel MKL
For example, to use Intel MKL libraries and/or Intel compiler:
set(BLA_VENDOR Intel10_64lp)
find_package(LAPACK)



  

