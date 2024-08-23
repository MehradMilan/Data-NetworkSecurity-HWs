from Crypto.Cipher import AES
import time

plain_text = '2f20cb8872c99b696e6461cb906c202f'
cipher_text = 'a6addbf32d0c6c5c87e311d3a35f78d3'

start_time = time.time()

possible_keys = [bytes([i, j]) + b'\0' * 14 for i in range(256) for j in range(256)]

dec_dict = {}
for k1 in possible_keys:
    cipher = AES.new(mode=AES.MODE_ECB, key=k1).decrypt(bytes.fromhex(plain_text))
    c = AES.new(mode=AES.MODE_ECB, key=k1).decrypt(cipher)
    dec_dict[c] = k1

for k2 in possible_keys:
    intermediate = AES.new(mode=AES.MODE_ECB, key=k2).decrypt(bytes.fromhex(cipher_text))
    if intermediate in dec_dict.keys():
        print('Found keys:')
        print('SUB-KEY1: ', k1.hex())
        print('SUB-KEY2: ', dec_dict[intermediate].hex())
        break

end_time = time.time()
print("Runtime of the program is (in seconds): ", end_time - start_time)