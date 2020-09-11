from .__init__ import *


func_list={
  0x00:  lambda:                          sys_restart_syscall(),
  0x01:  lambda ebx:                      sys_exit(status=ebx),
  0x02:  lambda:                          sys_fork(),
  0x03:  lambda ebx, ecx, edx:            sys_read(fd=ebx, buf=ecx, count=edx),
  0x04:  lambda ebx, ecx, edx:            sys_write(fd=ebx, buf=ecx, count=edx),
  0x05:  lambda ebx, ecx, edx:            sys_open(pathname=ebx, flags=ecx, mode=edx),
  0x06:  lambda ebx:                      sys_close(fd=ebx),
  0x07:  lambda ebx, ecx, edx:            sys_waitpid(pid=ebx, wstatus=ecx, options=edx),
  0x08:  lambda ebx, ecx:                 sys_creat(pathname=ebx, mode=ecx),
  0x09:  lambda ebx, ecx:                 sys_link(oldpath=ebx,  newpath=ecx),
  0x0a:  lambda ebx:                      None,
  0x0b:  lambda ebx, ecx, edx:            None,
  0x0c:  lambda ebx:                      None,
  0x0d:  lambda ebx:                      None,
  0x0e:  lambda ebx, ecx, edx:            None,
  0x0f:  lambda ebx, ecx:                 None,
  0x10:  lambda ebx, ecx, edx:            None,
  0x12:  lambda ebx, ecx:                 None,
  0x13:  lambda ebx, ecx, edx:            None,
  0x14:  lambda:                          None,
  0x15:  lambda ebx, ecx, edx, esi, edi:  None,
  0x16:  lambda ebx:                      None,
  0x17:  lambda:                          None,
  0x18:  lambda:                          None,
  0x19:  lambda ebx:                      None,
  0x1a:  lambda ebx, ecx, edx, esi:       None,
  0x1b:  lambda ebx:                      None,
  0x1c:  lambda ebx, ecx:                 None,
  0x1d:  lambda:                          None,
  0x1e:  lambda ebx, ecx:                 None,
  0x21:  lambda ebx, ecx:                 None,
  0x22:  lambda ebx:                      None,
  0x24:  lambda:                          None,
  0x25:  lambda ebx, ecx:                 None,
  0x26:  lambda ebx, ecx:                 None,
  0x27:  lambda ebx, ecx:                 None,
  0x28:  lambda ebx:                      None,
  0x29:  lambda ebx:                      None,
  0x2a:  lambda ebx:                      None,
  0x2b:  lambda ebx:                      None,
  0x2d:  lambda ebx:                      None,
  0x2e:  lambda ebx:                      None,
  0x2f:  lambda:                          None,
  0x30:  lambda ebx, ecx:                 None,
  0x31:  lambda:                          None,
  0x32:  lambda:                          None,                                  
  0x33:  lambda ebx:                      None,
  0x34:  lambda ebx, ecx:                 None,
  0x36:  lambda ebx, ecx, edx:            None,
  0x37:  lambda ebx, ecx, edx:            None,
  0x39:  lambda ebx, ecx:                 None,
  0x3b:  lambda ebx:                      None,
  0x3c:  lambda ebx:                      None,
  0x3d:  lambda ebx:                      None,
  0x3e:  lambda ebx, ecx:                 None,
  0x3f:  lambda ebx, ecx:                 None,
  0x40:  lambda:                          None,
  0x41:  lambda:                          None,
  0x42:  lambda:                          None,
  0x43:  lambda ebx, ecx, edx:            None,
  0x44:  lambda:                          None,
  0x45:  lambda ebx:                      None,
  0x46:  lambda:                          None, # sys_setreuid16
  0x47:  lambda:                          None, # sys_setregid16
  0x48:  lambda ebx, ecx, edx:            None, 
  0x49:  lambda ebx:                      None,
  0x4a:  lambda ebx, ecx:                 None, 
  0x4b:  lambda ebx, ecx:                 None, 
  0x4c:  lambda ebx, ecx:                 None,
  0x4d:  lambda ebx, ecx:                 None, 
  0x4e:  lambda ebx, ecx:                 None,
  0x4f:  lambda ebx, ecx:                 None,
  0x50:  lambda ebx, ecx:                 None,
  0x51:  lambda ebx, ecx:                 None,
  0x52:  lambda ebx:                      None, # sys_old_select
  0x53:  lambda ebx, ecx:                 None, # sys_symlink
  0x54:  lambda:                          None, # sys_lstat
  0x55:  lambda:                          None, # sys_readlink
  0x56:  lambda:                          None, # sys_uselib
  0x57:  lambda:                          None, # sys_swapon
  0x58:  lambda:                          None, # sys_reboot
  0x59:  lambda:                          None, # sys_old_readdir
  0x5a:  lambda:                          None, # sys_old_mmap
  0x5b:  lambda:                          None, # sys_munmap
  0x5c:  lambda:                          None, # sys_truncate
  0x5d:  lambda:                          None, # sys_ftruncate
  0x5e:  lambda:                          None, # sys_fchmod
  0x5f:  lambda:                          None, # sys_fchown16
  0x60:  lambda:                          None, # sys_getpriority
  0x61:  lambda:                          None, # sys_setpriority
  0x63:  lambda:                          None, # sys_statfs
  0x64:  lambda:                          None, # sys_fstatfs
  0x65:  lambda:                          None, # sys_ioperm
  0x66:  lambda:                          None, # sys_socketcall
  0x67:  lambda:                          None, # sys_syslog
  0x68:  lambda:                          None, # sys_setitimer
  0x69:  lambda:                          None, # sys_getitimer
  0x6a:  lambda:                          None, # sys_newstat
  0x6b:  lambda:                          None, # sys_newlstat
  0x6c:  lambda:                          None, # sys_newfstat
  0x6d:  lambda:                          None, # sys_uname
  0x6e:  lambda:                          None, # sys_iopl
  0x6f:  lambda:                          None, # sys_vhangup
  0x71:  lambda:                          None, # sys_vm86old
  0x72:  lambda:                          None, # sys_wait4
  0x73:  lambda:                          None, # sys_swapoff
  0x74:  lambda:                          None, # sys_sysinfo
  0x75:  lambda:                          None, # sys_ipc
  0x76:  lambda:                          None, # sys_fsync
  0x77:  lambda:                          None, # sys_sigreturn
  0x78:  lambda:                          None, # sys_clone
  0x79:  lambda:                          None, # sys_setdomainname
  0x7a:  lambda:                          None, # sys_newuname
  0x7b:  lambda:                          None, # sys_modify_ldt
  0x7c:  lambda:                          None, # sys_adjtimex
  0x7d:  lambda:                          None, # sys_mprotect
  0x7e:  lambda:                          None, # sys_sigprocmask
  0x80:  lambda:                          None, # sys_init_module
  0x81:  lambda:                          None, # sys_delete_module
  0x83:  lambda:                          None, # sys_quotactl
  0x84:  lambda:                          None, # sys_getpgid
  0x85:  lambda:                          None, # sys_fchdir
  0x86:  lambda:                          None, # sys_bdflush
  0x87:  lambda:                          None, # sys_sysfs
  0x88:  lambda:                          None, # sys_personality
  0x8a:  lambda:                          None, # sys_setfsuid16
  0x8b:  lambda:                          None, # sys_setfsgid16
  0x8c:  lambda:                          None, # sys_llseek
  0x8d:  lambda:                          None, # sys_getdents
  0x8e:  lambda:                          None, # sys_select
  0x8f:  lambda:                          None, # sys_flock
  0x90:  lambda:                          None, # sys_msync
  0x91:  lambda:                          None, # sys_readv
  0x92:  lambda:                          None, # sys_writev
  0x93:  lambda:                          None, # sys_getsid
  0x94:  lambda:                          None, # sys_fdatasync
  0x95:  lambda:                          None, # sys_sysctl
  0x96:  lambda:                          None, # sys_mlock
  0x97:  lambda:                          None, # sys_munlock
  0x98:  lambda:                          None, # sys_mlockall
  0x99:  lambda:                          None, # sys_munlockall
  0x9a:  lambda:                          None, # sys_sched_setparam
  0x9b:  lambda:                          None, # sys_sched_getparam
  0x9c:  lambda:                          None, # sys_sched_setscheduler
  0x9d:  lambda:                          None, # sys_sched_getscheduler
  0x9e:  lambda:                          None, # sys_sched_yield
  0x9f:  lambda:                          None, # sys_sched_get_priority_max
  0xa0:  lambda:                          None, # sys_sched_get_priority_min
  0xa1:  lambda:                          None, # sys_sched_rr_get_interval
  0xa2:  lambda:                          None, # sys_nanosleep
  0xa3:  lambda:                          None, # sys_mremap
  0xa4:  lambda:                          None, # sys_setresuid16
  0xa5:  lambda:                          None, # sys_getresuid16
  0xa6:  lambda:                          None, # sys_vm86
  0xa8:  lambda:                          None, # sys_poll
  0xa9:  lambda:                          None, # sys_nfsservctl
  0xaa:  lambda:                          None, # sys_setresgid16
  0xab:  lambda:                          None, # sys_getresgid16
  0xac:  lambda:                          None, # sys_prctl
  0xad:  lambda:                          None, # sys_rt_sigreturn
  0xae:  lambda:                          None, # sys_rt_sigaction
  0xaf:  lambda:                          None, # sys_rt_sigprocmask
  0xb0:  lambda:                          None, # sys_rt_sigpending
  0xb1:  lambda:                          None, # sys_rt_sigtimedwait
  0xb2:  lambda:                          None, # sys_rt_sigqueueinfo
  0xb3:  lambda:                          None, # sys_rt_sigsuspend
  0xb4:  lambda:                          None, # sys_pread64
  0xb5:  lambda:                          None, # sys_pwrite64
  0xb6:  lambda:                          None, # sys_chown16
  0xb7:  lambda:                          None, # sys_getcwd
  0xb8:  lambda:                          None, # sys_capget
  0xb9:  lambda:                          None, # sys_capset
  0xba:  lambda:                          None, # sys_sigaltstack
  0xbb:  lambda:                          None, # sys_sendfile
  0xbe:  lambda:                          None, # sys_vfork
  0xbf:  lambda:                          None, # sys_getrlimit
  0xc0:  lambda:                          None, # sys_mmap_pgoff
  0xc1:  lambda:                          None, # sys_truncate64
  0xc2:  lambda:                          None, # sys_ftruncate64
  0xc3:  lambda:                          None, # sys_stat64
  0xc4:  lambda:                          None, # sys_lstat64
  0xc5:  lambda:                          None, # sys_fstat64
  0xc6:  lambda:                          None, # sys_lchown
  0xc7:  lambda:                          None, # sys_getuid
  0xc8:  lambda:                          None, # sys_getgid
  0xc9:  lambda:                          None, # sys_geteuid
  0xca:  lambda:                          None, # sys_getegid
  0xcb:  lambda:                          None, # sys_setreuid
  0xcc:  lambda:                          None, # sys_setregid
  0xcd:  lambda:                          None, # sys_getgroups
  0xce:  lambda:                          None, # sys_setgroups
  0xcf:  lambda:                          None, # sys_fchown
  0xd0:  lambda:                          None, # sys_setresuid
  0xd1:  lambda:                          None, # sys_getresuid
  0xd2:  lambda:                          None, # sys_setresgid
  0xd3:  lambda:                          None, # sys_getresgid
  0xd4:  lambda:                          None, # sys_chown
  0xd5:  lambda:                          None, # sys_setuid
  0xd6:  lambda:                          None, # sys_setgid
  0xd7:  lambda:                          None, # sys_setfsuid
  0xd8:  lambda:                          None, # sys_setfsgid
  0xd9:  lambda:                          None, # sys_pivot_root
  0xda:  lambda:                          None, # sys_mincore
  0xdb:  lambda:                          None, # sys_madvise
  0xdc:  lambda:                          None, # sys_getdents64
  0xdd:  lambda:                          None, # sys_fcntl64
  0xe0:  lambda:                          None, # sys_gettid
  0xe1:  lambda:                          None, # sys_readahead
  0xe2:  lambda:                          None, # sys_setxattr
  0xe3:  lambda:                          None, # sys_lsetxattr
  0xe4:  lambda:                          None, # sys_fsetxattr
  0xe5:  lambda:                          None, # sys_getxattr
  0xe6:  lambda:                          None, # sys_lgetxattr
  0xe7:  lambda:                          None, # sys_fgetxattr
  0xe8:  lambda:                          None, # sys_listxattr
  0xe9:  lambda:                          None, # sys_llistxattr
  0xea:  lambda:                          None, # sys_flistxattr
  0xeb:  lambda:                          None, # sys_removexattr
  0xec:  lambda:                          None, # sys_lremovexattr
  0xed:  lambda:                          None, # sys_fremovexattr
  0xee:  lambda:                          None, # sys_tkill
  0xef:  lambda:                          None, # sys_sendfile64
  0xf0:  lambda:                          None, # sys_futex
  0xf1:  lambda:                          None, # sys_sched_setaffinity
  0xf2:  lambda:                          None, # sys_sched_getaffinity
  0xf3:  lambda:                          None, # sys_set_thread_area
  0xf4:  lambda:                          None, # sys_get_thread_area
  0xf5:  lambda:                          None, # sys_io_setup
  0xf6:  lambda:                          None, # sys_io_destroy
  0xf7:  lambda:                          None, # sys_io_getevents
  0xf8:  lambda:                          None, # sys_io_submit
  0xf9:  lambda:                          None, # sys_io_cancel
  0xfa:  lambda:                          None, # sys_fadvise64
  0xfc:  lambda:                          None, # sys_exit_group
  0xfd:  lambda:                          None, # sys_lookup_dcookie
  0xfe:  lambda:                          None, # sys_epoll_create
  0xff:  lambda:                          None, # sys_epoll_ctl
  0x100: lambda:                          None, # sys_epoll_wait 
  0x101: lambda:                          None, # sys_remap_file_pages 
  0x102: lambda:                          None, # sys_set_tid_address 
  0x103: lambda:                          None, # sys_timer_create 
  0x104: lambda:                          None, # sys_timer_settime 
  0x105: lambda:                          None, # sys_timer_gettime 
  0x106: lambda:                          None, # sys_timer_getoverrun 
  0x107: lambda:                          None, # sys_timer_delete 
  0x108: lambda:                          None, # sys_clock_settime 
  0x109: lambda:                          None, # sys_clock_gettime 
  0x10a: lambda:                          None, # sys_clock_getres 
  0x10b: lambda:                          None, # sys_clock_nanosleep 
  0x10c: lambda:                          None, # sys_statfs64 
  0x10d: lambda:                          None, # sys_fstatfs64 
  0x10e: lambda:                          None, # sys_tgkill 
  0x10f: lambda:                          None, # sys_utimes 
  0x110: lambda:                          None, # sys_fadvise64_64 
  0x112: lambda:                          None, # sys_mbind 
  0x113: lambda:                          None, # sys_get_mempolicy 
  0x114: lambda:                          None, # sys_set_mempolicy 
  0x115: lambda:                          None, # sys_mq_open 
  0x116: lambda:                          None, # sys_mq_unlink 
  0x117: lambda:                          None, # sys_mq_timedsend 
  0x118: lambda:                          None, # sys_mq_timedreceive 
  0x119: lambda:                          None, # sys_mq_notify 
  0x11a: lambda:                          None, # sys_mq_getsetattr 
  0x11b: lambda:                          None, # sys_kexec_load 
  0x11c: lambda:                          None, # sys_waitid
  0x11e: lambda:                          None, # sys_add_key 
  0x11f: lambda:                          None, # sys_request_key 
  0x120: lambda:                          None, # sys_keyctl 
  0x121: lambda:                          None, # sys_ioprio_set 
  0x122: lambda:                          None, # sys_ioprio_get 
  0x123: lambda:                          None, # sys_inotify_init 
  0x124: lambda:                          None, # sys_inotify_add_watch 
  0x125: lambda:                          None, # sys_inotify_rm_watch 
  0x126: lambda:                          None, # sys_migrate_pages 
  0x127: lambda:                          None, # sys_openat 
  0x128: lambda:                          None, # sys_mkdirat 
  0x129: lambda:                          None, # sys_mknodat 
  0x12a: lambda:                          None, # sys_fchownat 
  0x12b: lambda:                          None, # sys_futimesat 
  0x12c: lambda:                          None, # sys_fstatat64 
  0x12d: lambda:                          None, # sys_unlinkat 
  0x12e: lambda:                          None, # sys_renameat 
  0x12f: lambda:                          None, # sys_linkat 
  0x130: lambda:                          None, # sys_symlinkat 
  0x131: lambda:                          None, # sys_readlinkat 
  0x132: lambda:                          None, # sys_fchmodat 
  0x133: lambda:                          None, # sys_faccessat 
  0x134: lambda:                          None, # sys_pselect6 
  0x135: lambda:                          None, # sys_ppoll 
  0x136: lambda:                          None, # sys_unshare 
  0x137: lambda:                          None, # sys_set_robust_list 
  0x138: lambda:                          None, # sys_get_robust_list 
  0x139: lambda:                          None, # sys_splice 
  0x13a: lambda:                          None, # sys_sync_file_range 
  0x13b: lambda:                          None, # sys_tee 
  0x13c: lambda:                          None, # sys_vmsplice 
  0x13d: lambda:                          None, # sys_move_pages 
  0x13e: lambda:                          None, # sys_getcpu 
  0x13f: lambda:                          None, # sys_epoll_pwait 
  0x140: lambda:                          None, # sys_utimensat 
  0x141: lambda:                          None, # sys_signalfd 
  0x142: lambda:                          None, # sys_timerfd_create 
  0x143: lambda:                          None, # sys_eventfd 
  0x144: lambda:                          None, # sys_fallocate 
  0x145: lambda:                          None, # sys_timerfd_settime 
  0x146: lambda:                          None, # sys_timerfd_gettime 
  0x147: lambda:                          None, # sys_signalfd4 
  0x148: lambda:                          None, # sys_eventfd2 
  0x149: lambda:                          None, # sys_epoll_create1 
  0x14a: lambda:                          None, # sys_dup3 
  0x14b: lambda:                          None, # sys_pipe2 
  0x14c: lambda:                          None, # sys_inotify_init1 
  0x14d: lambda:                          None, # sys_preadv 
  0x14e: lambda:                          None, # sys_pwritev 
  0x14f: lambda:                          None, # sys_rt_tgsigqueueinfo 
  0x150: lambda:                          None, # sys_perf_event_open 
  0x151: lambda:                          None, # sys_recvmmsg 
}
__all__=[func_list]