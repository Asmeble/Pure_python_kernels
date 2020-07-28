INT_0x80=b'\xCD\x80'
X86_CODE32=b''

from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_INTR
from kernels.linux.x86_32.d7_26_2020.L2_6 import linux_kernel_2_6

mu=Uc(UC_ARCH_X86, UC_MODE_32)
mu.mem_map(0, 4*1024)
mu.hook_add(UC_HOOK_INTR, linux_kernel_2_6)

def fclose(file):
  file.close()
def fflush(file):
  print(end='', file=file, flush=True)
def fgetc(file):
  return file.read(1)
def fgets(str_, num, stream):
  s_=''
  for a in range(num):
    s_+=fgetc(stream)
  str_[0]=s_
  del s_
def fopen(filename, mode):
  return open(filename, mode)
def fprintf(stream, format_, *va_list):
  print(format_ % va_list, end='', file=stream)
def fputc(character, stream):
  stream.write(character)
def fputs(str_, stream):
  fputc(str_, stream)
def fread(ptr, size, count, stream):
  from .stdlib import malloc; ptr_=''
  for a in stream.readlines():
    ptr_+=a; del a
  ptr_+=malloc(__import__('ctypes').sizeof(size)*count).decode('ascii')
  ptr[0]=ptr_[:__import__('ctypes').sizeof(size)+count-1:]; del ptr_, malloc
def ftell(stream):
  return stream.tell()
def fwrite(ptr, size, count, stream):
  from .stdlib import malloc; ptr_=''
  for a in ptr[0]:
    ptr_+=a; del a
  ptr_+=malloc(__import__('ctypes').sizeof(size)*count).decode('ascii')
  stream.write(ptr_[:__import__('ctypes').sizeof(size)+count-1:]); del ptr_, malloc
def getc(file):
  return file.read(1)
def getchar():
  return open('/dev/tty','r').read(1)
def perror(string_to_print):
  print(string_to_print)
def rewind(stream):
  #stream.__str__().split()[1][::][::]
  if stream.mode.count('w', 1, 2) == True:
    stream=open(stream.__str__().split()[1][::][::], 'r')
  if stream.mode.count('r', 1, 2) == True:
    stream=open(stream.__str__().split()[1][::][::], 'w')
  pass
def rename(oldname, newname):
  __import__('os').system("mv "+str(oldname)+" "+str(newname))
def scanf(format_, *va_list): # va_list gets treated like a pointer.
  def getkey():
    from termios import tcgetattr, tcsetattr, ICANON, ECHO,TCSANOW , TCSAFLUSH
    term=fopen("/dev/tty", "r")
    fd = term.fileno()
    old = tcgetattr(fd)
    new = tcgetattr(fd)
    new[3] &= ~ICANON & ECHO
    tcsetattr(fd, TCSANOW, new)
    c = None
    try:
      c=fgetc(term)
    finally:
      tcsetattr(fd, TCSAFLUSH, old)
      fclose(term)
    d=c+'\n'
    del c, tcgetattr, tcsetattr, ICANON, ECHO, TCSANOW , TCSAFLUSH
    return d
  pos_=0
  if len(format_.decode('ascii').split()[0].split('-' or '+')) == 2:
    pos_+=1
  s_0=''
  for a in range(eval(format_.decode('ascii').split()[0][1+pos_:-1])):
    s_0+=getkey().replace('\n','')
    del a
  va_list[0][0]=s_0.encode('ascii')
  del getkey, pos_, s_0

def printf(chars_, *va_list):
  global mu, INT_0x80, X86_CODE32
  with __import__("multiprocessing").Pool(len(va_list) if len(va_list) != 0 else 1):
    for a in chars_ % va_list:
      X86_CODE32+=b'\xBA\x01'+b'\x00\x00\x00'+b'\xB9'+eval(f"b'{chr(a) if hex(a) != '0xa' else ''}'")+b'\0'*3+b'\xBB\1'+b'\x00\x00\x00'+b'\xB8\4'+b'\x00\x00\x00'+INT_0x80
  mu.mem_write(0, X86_CODE32)
  mu.emu_start(0, len(X86_CODE32))
  mu.emu_stop()
  mu.mem_write(0, b''*len(X86_CODE32))
  X86_CODE32=b''
