from unicorn.x86_const import UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
from .__init__ import * #### Git_import=__import__("github_import").Git_import
sys_write=sys_write; # Perform sanity checks of functions ahead of time.....   #### sys_write=Git_import("Asmeble", "Pure_python_kernels", "v-stable-09_10_2020", "kernels/linux/x86_32/"+"__init__.py").__enter__().sys_write 
UC_X86_REG_EAX=UC_X86_REG_EAX; UC_X86_REG_ECX=UC_X86_REG_ECX; UC_X86_REG_EDX=UC_X86_REG_EDX; UC_X86_REG_ESI=UC_X86_REG_ESI; UC_X86_REG_EDI=UC_X86_REG_EDI; UC_X86_REG_EBX=UC_X86_REG_EBX
def linux_kernel_2_6(uc, intno, user_data):
  global UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
  if intno == 0x80:
    args,args_,function_lookup={u'ebx': uc.reg_read(UC_X86_REG_EBX), u'ecx': uc.reg_read(UC_X86_REG_ECX), u'edx': uc.reg_read(UC_X86_REG_EDX), u'esi': uc.reg_read(UC_X86_REG_ESI), u'edi': uc.reg_read(UC_X86_REG_EDI)},{},''
    for arg in args:
      if args[arg] != 0:
        args_[arg]=args[arg]
    args=args_
    from kernels.linux.x86_32 import Linux_kernel_functions_on_eax
    try:
      Linux_kernel_functions_on_eax.func_list.get(uc.reg_read(UC_X86_REG_EAX))(**args)
    except NameError:
      pass
    except OverflowError:
      print('', end='\n')
    finally:
      del arg, args, args_, Linux_kernel_functions_on_eax
      pass
