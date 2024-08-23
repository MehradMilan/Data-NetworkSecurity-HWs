from Crypto.Cipher import AES
import time

plain_text = '2f20cb8872c99b696e6461cb906c202f'
cipher_text = 'e4714ee833977599b7ec0a8d83a62164'

start_time = time.time()

possible_keys = [bytes([i, j]) + b'\0' * 14 for i in range(256) for j in range(256)]

enc_dict = {}
for k1 in possible_keys:
    cipher = AES.new(mode=AES.MODE_ECB, key=k1).encrypt(bytes.fromhex(plain_text))
    enc_dict[cipher] = k1

for k2 in possible_keys:
    intermediate = AES.new(mode=AES.MODE_ECB, key=k2).encrypt(bytes.fromhex(cipher_text))
    if intermediate in enc_dict.keys():
        print('Found keys:')
        print('SUB-KEY1: ', enc_dict[intermediate].hex())
        print('SUB-KEY2: ', k2.hex())
        break

end_time = time.time()

print("Runtime of the program is (in seconds): ", end_time - start_time)