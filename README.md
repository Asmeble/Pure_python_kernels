This is the latest version may be found under tags. The code runs like C/C++ compiled functions without being compiled code.

This project is meant to provide a linux or Mac OS like virtual kernel inside userspace execution (where programs are normally run). It demonstrates the implementation of python functionality to support kernel emulation to support C/C++ functions without having to compile, and the same is true for using the kernel functions. Do note that the c/c++ functions do link against a kernel and their is an effective if not efficient when it responds to kernel interrupts.

The overall work required knowing a [fuck-ton] of information about IO, kernel development, more than an in depth understanding of {assembly, C/C++, compilers & linkers in general}, and compiled {application, drivers, & library code}. Most of it is cached and optimizing at runtime to match the scope of the data that must be handled or operated on. Currently, only two C/C++ libraries have a few functions that function on python objects without the issue of IO violations or runtime violations. NameErrors & OverFlowErrors are exception handled such that is should stunt runtime collisions with local code.

The way to use the kernel is to replicate the project and modify the code by hand. The code here is meant to be a thing templated off of to emulate C/C++ without having to compile to C/C++ code for another system, as instead you can use python and interface two platforms, (your operating system & python).

For Windows:
  1) Download & run the cygwin-setup, have it install python3 & python3-pip & bash & sh & wget & curl & git.
  2) Clone the repository and copy "linux_kernels" subdirectory to the location of your choice.
  3) Use python3-pip to install unicorn-engine, requests, and their dependencies.
  4) Use "github_import.py" to copy each "c/c++ library & their c/c++ functions" from "github.com/Asmeble/The_wrecking_ball/tree/{ latest version by branch name }/cplusplus"
       into the runtime with as many functions as you need copied. If you need to use just one, I recommend using ".__enter__()" to link the function into your local python
      instance.

 For Linux:
  1) Fnstall python3, python3-pip, bash, sh, wget, curl & git if they aren't already....
  2) Follow instructions 2-4 as written under "For Windows".

 For Mac:
  1) Follow instructions as written under "For Linux".
