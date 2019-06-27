  

# CMAKE_ANDROID_ARCH  
When Cross Compiling for Android with NVIDIA Nsight Tegra Visual Studio Edition, this variable may be set to specify the default value for the
ANDROID_ARCH target property.  See that target property for
additional information.  

Otherwise, when Cross Compiling for Android, this variable provides
the name of the Android architecture corresponding to the value of the
CMAKE_ANDROID_ARCH_ABI variable.  The architecture name
may be one of:  


arm
arm64
mips
mips64
x86
x86_64
  

