This repo is meant to address architectural differences, size, solve code caching issues, and to abstractly address applications with their own instance of the kernel, which has most of its functionality removed.

This means that most of the libraries that are written in c/c++ can be supported inside python encapsulation, then memoize the results to reduce the strain of execution, and size on disk, and size stored in memory.

Please report bugs/issues to this repo. The more info I am given about the bugs/issues and the situation it's applied to.
