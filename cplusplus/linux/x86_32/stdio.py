INT_0x80 = b'\xCD\x80'
X86_CODE32 = b''
trip0 = b'\0' * 3
from unicorn import Uc, UC_ARCH_X86, UC_MODE_32, UC_HOOK_INTR

from github_import import Git_import

from kernels.linux.x86_32.L2_6 import linux_kernel_2_6

mu = Uc(UC_ARCH_X86, UC_MODE_32)  # <-------|
#                                           |
Mem_size = 4 * 1024  #<--------------------------------- These are specific to the functionality surrounding assembly parsing and execution.
mu.mem_map(0, Mem_size)  #                        | In this case, the kernel is emulated, the assembly pushs data onto a syscall that calls the kernel to
mu.hook_add(UC_HOOK_INTR, linux_kernel_2_6)  #<---| then call the kernel function with the data and parameters passed to syscall at the assembly level.

def printf(chars_, *va_list):
  global mu,INT_0x80,trip0,linux_kernel_2_6
  entry_point=0x0a00
  for a in chars_% va_list:
    l=b'\xBA\1'+trip0+b'\xB9'+eval(f"b'{chr(a)if hex(a)!='0xa'else''}'")+trip0+b'\xBB\1'+trip0+b'\xB8\4'+trip0+INT_0x80;mu.mem_write(entry_point,l); mu.emu_start(entry_point,entry_point+len(l)); del l


#del [list(map(lambda a: print(chr(a), end=''), chars_ % va_list)).pop()][0] # <-- This version of 'printf' is for when you don't need a kernel during runtime. Plus, it deletes itself after structuring and executing based on size of scope that needed to be addressed.


__all__ = ["scanf", 'printf']
lru_cache=__import__("functools").lru_cache
@lru_cache(maxsize=1000)
def scanf(format, s=None, collapseWhitespace=True):
  if s is None:
    s = __import__("sys").stdin
  if hasattr(s, "readline"):
    s = s.readline()
  format_pat = ""
  cast_list = []
  i = 0
  length = len(format)
  while i < length:
    found = None
    for token,pattern,cast in[(__import__("re").compile(_token),_pattern,_cast)for _token,_pattern,_cast in[("%c","(.)", lambda x:x),("%\*c","(?:.)",None),("%(\d)c","(.{%s})",lambda x:x),("%\*(\d)c","(?:.{%s})",None),("%(\d)[di]","([+-]?\d{%s})",int),("%\*(\d)[di]","(?:[+-]?\d{%s})",None),("%[di]","([+-]?\d+)",int), ("%\*[di]","(?:[+-]?\d+)",None),("%u","(\d+)",int),("%\*u","(?:\d+)",None),("%[fgeE]","([-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)",float),("%\*[fgeE]","(?:[-+]?(?:\d+(?:\.\d*)?|\.\d+)(?:[eE][-+]?\d+)?)",None),("%s","(\S+)",lambda x:x),("%\*s","(?:\S+)",None),("%([xX])","(0%s[\dA-Za-f]+)",lambda x: int(x, 16)),("%\*([xX])","(?:0%s[\dA-Za-f]+)",None),("%o","(0[0-7]*)",lambda x:int(x, 8)),("%\*o", "(?:0[0-7]*)",None)]]:
      found = token.match(format, i)
      if found:
        if cast:
          cast_list.append(cast)
        groups = found.groupdict() or found.groups()
        if groups:
          pattern = pattern % groups
        format_pat += pattern
        i = found.end()
        break
    if not found:
      char = format[i]
      if char in "|^$()[]-.+*?{}<>\\":
        format_pat += "\\"
      format_pat += char
      i += 1
  if collapseWhitespace:
    format_pat = __import__("re").sub(r'\s+', r'\\s+', format_pat)
  format_re = __import__("re").compile(format_pat)
  format_re, casts = format_re, cast_list
  found = format_re.search(s)
  if found:
    groups = found.groups()
    return tuple([casts[i](groups[i]) for i in range(len(groups))])

del lru_cache


"""
https://github.com/joshburnett/scanf
http://code.activestate.com/recipes/502213-simple-scanf-implementation/
"""
