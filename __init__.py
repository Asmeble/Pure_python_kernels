"""
Welcome to the virtual linux kernel 2.6+ in python.
Most of it is written in python on top of unicorn-engine, python-ctypes & python-cython, precompiled subsections of assembly, python functions to handle kernel interrupt requests, python-requests, & as little code as possible.

"""

def sys_write(fd, buf, count):
  print(chr(buf),file={0:__import__("sys").stdin,1:__import__("sys").stdout,2:__import__("sys").stderr}.get(fd), end='', flush=True)