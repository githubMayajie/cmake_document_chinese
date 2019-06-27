  

# RULE_LAUNCH_LINK  
Specify a launcher for link rules.  

Makefile Generators and the Ninja generator prefix
link and archive commands with the given launcher command line.
This is intended to allow launchers to intercept build problems
with high granularity.  Other generators ignore this property
because their underlying build systems provide no hook to wrap
individual commands with a launcher.  

