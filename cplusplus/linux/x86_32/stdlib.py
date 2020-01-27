#modelled after [stdlib.h]

from __builtins__ import abs

def atexit(void_type):
  return void_type()

def atof(str_):
  return float(str_)

def atoi(str_):
  return int(str_)

def atol(str_):
  return atoi(str_)

def atoll(str_):
  return atol(str_)

def malloc(size):
  return bytearray(bytes(size))
