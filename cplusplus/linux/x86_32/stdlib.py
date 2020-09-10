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

def calloc(num, size):
  return malloc(size)*num

def div(numerator,denominator):
  return int(numerator/denominator)

def free(ptr): # Cannot use with multiprocessing or
  ptr[0]=b''   #  multithreading: kicks back
  del ptr     # "fatal: morestack on gsignal" as an
                # error to stdout.

def malloc(size):
  return bytearray(bytes(size))
