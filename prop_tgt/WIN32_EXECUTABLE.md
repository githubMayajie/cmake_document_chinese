  

# WIN32_EXECUTABLE  
Build an executable with a WinMain entry point on windows.  

When this property is set to true the executable when linked on
Windows will be created with a WinMain() entry point instead of just
main().  This makes it a GUI executable instead of a console application.
See the CMAKE_MFC_FLAG variable documentation to
configure use of the Microsoft Foundation Classes (MFC) for WinMain
executables.  This property is initialized by the value of the
CMAKE_WIN32_EXECUTABLE variable if it is set when
a target is created.  
