from os import urandom
from Crypto.Cipher import AES
import time

plain_text = '2f20cb8872c99b696e6461cb906c202f'
cipher_text = 'fd25a141381dbaef0fafc20ce028d934'

def aes_enc(p, k):
    E = AES.new(mode=AES.MODE_ECB, key=k).encrypt
    c = E(bytes.fromhex(p))
    return c.hex()

start = time.time()
for i in range(256):
    for j in range(256):
        k = bytes([i, j]) + b'\0' * 14
        if aes_enc(plain_text, k) == cipher_text:
            print('KEY: ', k.hex())
            break
end = time.time()

print("Runtime of the program is (in seconds): ", end - start)