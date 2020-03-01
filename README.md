This repo is meant to address architectural differences, size, solve code caching issues, and to abstractly address applications with their own instance of the kernel, which has most of its functionality removed.

This means that most of the libraries that are written in c/c++ can be supported inside python encapsulation, then memoize the results to reduce the strain of execution, and size on disk, and size stored in memory.

Please report bugs/issues to this repo. The more info I am given about the bugs/issues and the situation it's applied to. This reduces the issue of a system getting kernel exploited and leaves them in an unfamilar pocket of execution always outside of actual kernel memory and leaves them in userpace. This means that while they could attempt to corrupt the instance and demand that it break encapsulation, the tools for such are only valid if python has "__builtins__" loaded; meaning you could let them "hack in", but they'd be stuck in a honey-pot where all that's happening is the "hacker" is left with another useless rootkit.( :D ) 

This project's designed to make it harder to "hack" through encapsulation, as you would easily remove that piece of execution from runtime that would give them (the "hacker") leverage of the system from outside it( :D ); even it they bruteforce the runtime of your host-system, they would have too many points to look at in memory to attempt to isolate for "the kernel", as "the kernel" would be run by multiple instances; The "kernel"-instances would be indistinguishable from root-processes, as it would be breafly loaded, and would yeild a encapsulated deadzone that gives them nothing to exploit.( :D ) Distinction between virtual memory and real memory, as well as cpu, so attempting to drill into the hardware from those points in execution and device control will prove to be "imposebru" and kick a flag-up in their head that their attempt was meager, and a useless endeavor. ( :D )

"Oops! My bad!"
###################################
To use the code from any branch from this github as if it were installed locally; you can copy and use the "github_import" function to load it, and use the "exec" python statement to use and link it into the runtime. It should put "Pip" or "poetry" out of the equation for package {install and run} builds. Just write and load once, and publish the update under a new branch. Come on man, make it easier for the developers.

This also is useful for the python built "kernel" and "kernel" functions that work with a web-linked copy of unicorn-engine.
Due note that it is possible to import local to your runtime and override or patch a broken function locally, even in your browser with "brython.js" inside the browser.
###################################

As I update this repository, the master branch will be updated with a change log; the next update will include what changed.

https://unicorn-scaled-and-scanned-the-globe.dylaneliot.repl.run/ is an example showing it install a package and them running my code from the branch I was testing with, and continue to test with.

















