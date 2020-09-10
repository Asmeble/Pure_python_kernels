Welcome.

This is a c/c++ emulator that comes with a linux kernel. The only requirement are {bootable OS, a copy of python installed, and a compiled version of unicorn-engine}.
This lets you use c/c++ types, functions and a python based linux kernel, all of which interfaces with unicorn-engine, which interfaces with python.

The project is compatible with Windows, linux, and Mac OS.


The way you use it is like this [python -c "from cplusplus.linux.x86_32.stdio import printf; printf(b'we will se shortly')"] and it should work. Because it is a
 python based kernel, unique errors can occur. Testing in and around the virtual kernel will help when debugging. The installation is wherever you put the code.

The current version is unde the tag "v-stable-09_10_2020".
