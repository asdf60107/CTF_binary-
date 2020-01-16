from pwn import*

context.terminal = ['tmux','splitw','-h']

#gdb.attach(proc.pidof(p)[0]

p = process('./loopy')
libc = ELF('./libc.so.6.so')


p.sendline(payload)

p.interactive()
