  

# FindRTI  
Try to find M&S HLA RTI libraries  

This module finds if any HLA RTI is installed and locates the standard
RTI include files and libraries.  

RTI is a simulation infrastructure standardized by IEEE and SISO.  It
has a well defined C++ API that assures that simulation applications
are independent on a particular RTI implementation.  

http://en.wikipedia.org/wiki/Run-Time_Infrastructure_(simulation)

  

This code sets the following variables:  

RTI_INCLUDE_DIR = the directory where RTI includes file are found
RTI_LIBRARIES = The libraries to link against to use RTI
RTI_DEFINITIONS = -DRTI_USES_STD_FSTREAM
RTI_FOUND = Set to FALSE if any HLA RTI was not found

  

Report problems to ```<certi-devel@nongnu.org>```  

