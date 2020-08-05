#from . import * ###
with __import__("github_import").Git_import(username="Asmeble", repo="The_wrecking_ball", branch="v-07.28.2020", path_to_module=x86_32_path+"L2_6.py") as __init__:
  __init__=__init__
  from __init__ import *
# This tells the interpreter to read __init__.py and pull all of the functionality needed based on the function 
#  lookup list. This means that the 

def linux_kernel_2_6(uc, intno, user_data):
  from unicorn.x86_const import UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
  if intno == 0x80:
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
    for a in open(__package__.replace(".","/")+"/"+"Linux2.6_kernel_functions.eax", 'r').readlines():
      function_lookup+=a
    try:
      eval(function_lookup).get(uc.reg_read(UC_X86_REG_EAX))(**args)
    except NameError:
      pass
    except OverflowError:
      print('', end='\n')
    finally:
      del arg, a, args, args_, function_lookup, UC_X86_REG_EAX, UC_X86_REG_ECX, UC_X86_REG_EDX, UC_X86_REG_ESI, UC_X86_REG_EDI, UC_X86_REG_EBX
      pass
