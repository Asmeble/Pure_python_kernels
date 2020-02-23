from requests import get as wget

def Github_import(username, repo, branch, path_to_module):
  return wget("https://raw.githubusercontent.com/"+username+"/"+repo+"/"+branch+"/"+path_to_module).text

exec(repr(Github_import(username="Asmeble",repo="unicorn",branch="master", path_to_module="bindings/python/unicorn/unicorn.py")))

from unicorn.x86_const import UC_X86_REG_EAX,UC_X86_REG_EBX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI

def sys_write(fd, constbuf, count):
  print(chr(constbuf),file={0:__import__("sys").stdin,1:__import__("sys").stdout,2:__import__("sys").stderr}.get(fd), end='', flush=False)

def sys_restart_syscall(): pass
def sys_exit(status): pass
def sys_fork(): pass
def sys_read(fd, buf, count): pass
def sys_open(pathname, flags, mode): pass
def sys_close(fd): pass
def sys_waitpid(pid, wstatus, options): pass
def sys_creat(pathname, mode): pass
def sys_link(oldpath,  newpath): pass
def sys_unlink(pathname): pass
def sys_execve(pathname,  argv,  envp): pass
def sys_chdir(path): pass
def sys_time(tloc): pass
def sys_mknod(pathname, mode, dev): pass
def sys_chmod(pathname, mode): pass
def sys_lchown16(filename, user, group): pass
def sys_stat(pathname, statbuf): pass
def sys_lseek(fd, offset, whence): pass
def sys_getpid(): pass
def sys_mount(src, trgt, fs_type, mountflags, constdata): pass
def sys_oldumount(name): pass

def linux_kernel_2_6(uc, intno, user_data):
  if intno == 0x80:
    try:
      args,args_,function_lookup={
        u'ebx': uc.reg_read(UC_X86_REG_EBX),
        u'ecx': uc.reg_read(UC_X86_REG_ECX),
        u'edx': uc.reg_read(UC_X86_REG_EDX),
        u'esi': uc.reg_read(UC_X86_REG_ESI),
        u'edi': uc.reg_read(UC_X86_REG_EDI),
      },{},''
      for arg in args:
        if args[arg] != 0:
          args_[arg]=args[arg]
      args=args_
     except NameError:
      pass
    for a in open('linux_kernels/x86_32/function_lookup.txt', mode='r').readlines():
      function_lookup+=a
    eval(function_lookup).get(uc.reg_read(UC_X86_REG_EAX))(**args)
    del arg, a, args, args_, function_lookup
    return
  return
