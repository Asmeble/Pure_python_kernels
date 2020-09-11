global linux_kernel_2_6
def linux_kernel_2_6(uc, intno, user_data):
  global args_, args, Linux_kernel_functions_on_eax
  if intno == 0x80:
    try:
      from unicorn.x86_const import UC_X86_REG_EBX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI
      args={
        u'ebx': uc.reg_read(UC_X86_REG_EBX), 
        u'ecx': uc.reg_read(UC_X86_REG_ECX), 
        u'edx': uc.reg_read(UC_X86_REG_EDX),
        u'esi': uc.reg_read(UC_X86_REG_ESI),
        u'edi': uc.reg_read(UC_X86_REG_EDI)
      }
      list(map(lambda a, args=args: exec("del args[a]"), list(filter(lambda arg: args[arg] == 0, args))))
      from . import Linux_kernel_functions_on_eax
      Linux_kernel_functions_on_eax.func_list.get(uc.reg_read(__import__("unicorn").x86_const.UC_X86_REG_EAX))(**args)
    except OverflowError:
      print('', end='\n')
    finally:
      del intno, args, Linux_kernel_functions_on_eax, UC_X86_REG_EBX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI
      pass
    return
  return
__all__=["linux_kernel_2_6"]
