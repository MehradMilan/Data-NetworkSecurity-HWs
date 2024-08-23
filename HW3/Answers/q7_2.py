from Crypto.Cipher import AES
BLOCK_SIZE = 128 // 8

def enc_mac(k, m):
    # PKCS pad
    r = BLOCK_SIZE - len(m) % BLOCK_SIZE
    pad_size = r if r != 0 else BLOCK_SIZE
    m += pad_size.to_bytes(1, 'big') * pad_size
    # encrypt
    c = AES.new(mode=AES.MODE_OFB, key=k, iv=k).encrypt(m)
    # MAC
    t = AES.new(mode=AES.MODE_CBC, key=k, iv=c[:BLOCK_SIZE]).encrypt(m)[-BLOCK_SIZE:]
    return (c, t)

def xor_strings(xs, ys):
    return bytes(x ^ y for x, y in zip(bytes.fromhex(xs), bytes.fromhex(ys)))

def pad(m):
    r = BLOCK_SIZE - len(m) % BLOCK_SIZE
    pad_size = r if r != 0 else BLOCK_SIZE
    m += pad_size.to_bytes(1, 'big') * pad_size
    return m

c = "ad7fa3468caf0b5c01ec7be9b583fa350d2ce39b8cd57ee26270235cd6598592"
t = "905f6d5d03e5269a52aa3e33b558e764"
org_p_text = '1$ to original_destination'
fake_p_text = '99$ to attacker'
padded_fake_p_text = pad(fake_p_text.encode())
truncated_org_p_text = org_p_text[:BLOCK_SIZE]

c_prime = xor_strings(xor_strings(c, padded_fake_p_text.hex()).hex(), truncated_org_p_text.encode().hex())
print("c_prime: ", c_prime.hex())

# Test
random_key = '875faffbaeea63eb878613b98460f4d2'
c, t = enc_mac(bytes.fromhex(random_key), org_p_text.encode())
c_prime = xor_strings(xor_strings(c.hex(), padded_fake_p_text.hex()).hex(), truncated_org_p_text.encode().hex())

message = AES.new(mode=AES.MODE_OFB, key=bytes.fromhex(random_key), iv=bytes.fromhex(random_key)).decrypt(c_prime)
print("Message: ", message.decode())