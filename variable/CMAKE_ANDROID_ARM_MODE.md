  

# CMAKE_ANDROID_ARM_MODE  
When Cross Compiling for Android and CMAKE_ANDROID_ARCH_ABI
is set to one of the armeabi architectures, set CMAKE_ANDROID_ARM_MODE
to ON to target 32-bit ARM processors (-marm).  Otherwise, the
default is to target the 16-bit Thumb processors (-mthumb).  
