Welcome.

This is a c/c++ emulator that comes with a linux kernel. The only requirement are {bootable OS, a copy of python installed, and a compiled version of unicorn-engine}. This lets you use c/c++ types, functions and a python based linux kernel, all of which interfaces with unicorn-engine, which interfaces with python.

The project is compatible with Windows, linux, and Mac OS.
The way you use it is like this [python -c "from cplusplus.linux.x86_32.stdio import printf; printf(b'we will see shortly\n')"] and it should work. Because it is a python based kernel, unique errors can occur.
Testing in and around the virtual kernel will help when debugging. The installation is wherever you put the code.

The current version is under the tag "v-stable-09-11-2020".
recommended cloning by branch can be done like so:
 "git clone --branch <branch_to_checkout> <url to repository with '.git' extension>"
This project is tested so that it is compatible with docker, cygwin, windows, and standard linux distrobutions.
To use with docker, install python and then install unicorn-engine inside the container, then make an export.
After exporting, import the image with a tag associated with the prebuilt unicorn-engine binary. After that, wherever the repo was cloned inside the container is where it will run from, installwise.
