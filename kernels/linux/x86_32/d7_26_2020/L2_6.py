from unicorn.x86_const import UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
from .__init__ import *
sys_write=sys_write; # Perform sanity checks of functions ahead of time.....
UC_X86_REG_EAX=UC_X86_REG_EAX; UC_X86_REG_ECX=UC_X86_REG_ECX; UC_X86_REG_EDX=UC_X86_REG_EDX; UC_X86_REG_ESI=UC_X86_REG_ESI; UC_X86_REG_EDI=UC_X86_REG_EDI; UC_X86_REG_EBX=UC_X86_REG_EBX
def linux_kernel_2_6(uc, intno, user_data):
  global UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
  if intno == 0x80:
    args,args_,function_lookup={u'ebx': uc.reg_read(UC_X86_REG_EBX), u'ecx': uc.reg_read(UC_X86_REG_ECX), u'edx': uc.reg_read(UC_X86_REG_EDX), u'esi': uc.reg_read(UC_X86_REG_ESI), u'edi': uc.reg_read(UC_X86_REG_EDI)},{},''
    for arg in args:
      if args[arg] != 0:
        args_[arg]=args[arg]
    args=args_
    from kernels.linux.x86_32.d7_26_2020 import Linux_kernel_functions_on_eax
    x=Linux_kernel_functions_on_eax.func_list
    try:
      x.get(uc.reg_read(UC_X86_REG_EAX))(**args)
    except NameError as e:
      pass
    except OverflowError:
      print('', end='\n')
    finally:
      del arg, args, args_
      pass
