from __future__ import print_function
from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_INTR
from linux_kernels.x86_32.kernel_functions import linux_kernel_2_6
mu=Uc(UC_ARCH_X86, UC_MODE_32)
mu.mem_map(0, 4*1024)
mu.hook_add(UC_HOOK_INTR, linux_kernel_2_6)
INT_0x80=b'\xCD\x80'

def scanf(format_, *va_list): # va_list gets treated like a pointer.
  def getkey():
    import termios, sys, os
    term=open("/dev/tty", "r")
    fd = term.fileno()
    old = termios.tcgetattr(fd)
    new = termios.tcgetattr(fd)
    new[3] &= ~termios.ICANON & termios.ECHO
    termios.tcsetattr(fd, termios.TCSANOW, new)
    c = None
    try:
      c = os.read(fd, 1)
    finally:
      termios.tcsetattr(fd, termios.TCSAFLUSH, old)
      term.close()
    d=c.decode('ascii')+'\n'
    del c
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
  return

def printf(format_, *va_list):
  X86_CODE32,ZB_Array=b'',b'\0'*3
  for a in format_:
    X86_CODE32+=b'\xBA\1'+ZB_Array+b'\xB9'+eval(f"b'{chr(92)+hex(a)[1:]}'")+ZB_Array+b'\xBB\1'+ZB_Array+b'\xB8\4'+ZB_Array+INT_0x80
    del a
  mu.mem_write(0, X86_CODE32)
  mu.emu_start(0, len(X86_CODE32))
  mu.emu_stop()
  for b in va_list:
    print(b.decode('ascii'), end='')
    del b
  del ZB_Array,X86_CODE32
  return
