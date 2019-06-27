  

# CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS  
This variable contains a list of env vars as a list of tokens with the
syntax var=value.  

Example:  

set(CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS
   "FOO=FOO1\;FOO2\;FOON"
   "BAR=BAR1\;BAR2\;BARN"
   "BAZ=BAZ1\;BAZ2\;BAZN"
   "FOOBAR=FOOBAR1\;FOOBAR2\;FOOBARN"
   "VALID="
   )

  

In case of malformed variables CMake will fail:  

set(CMAKE_SUBLIME_TEXT_2_ENV_SETTINGS
    "THIS_IS_NOT_VALID"
    )

  
