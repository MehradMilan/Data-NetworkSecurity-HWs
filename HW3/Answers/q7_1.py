from Crypto.Cipher import AES
BLOCK_SIZE = 128 // 8

k = '875faffbaeea63eb878613b98460f4d2'
c1, t1 = 'd8b8239628a3f44c81e50cbd57aaac62586cdf1376c25fa8c23e8becf6be4688', 'abb859c60dd1450bd789a40bc3638f4e'
c2, t2 = 'dfb3319a23e6bf4d88b20cf342a9ac62447cc04770dd2cd2bc5b87e0fab24a84', 'b893a8d5032f5c004f11543626fc942e'

def check_mac(k, c, t):
    m = AES.new(mode=AES.MODE_OFB, key=k, iv=k).decrypt(c)
    if AES.new(mode=AES.MODE_CBC, key=k, iv=c[:BLOCK_SIZE]).encrypt(m)[-BLOCK_SIZE:] == t:
        pad_size = m[-1]
        if pad_size < 1 or pad_size > BLOCK_SIZE:
            return m, False
        for i in range(1, pad_size + 1):
            if m[-i] != pad_size:
                return m, False
        m = m[:-pad_size]
        return m, True
    return m, False

m1, authenticity1 = check_mac(bytes.fromhex(k), bytes.fromhex(c1), bytes.fromhex(t1))
m2, authenticity2 = check_mac(bytes.fromhex(k), bytes.fromhex(c2), bytes.fromhex(t2))

if authenticity1:
    print("Message 1: ", m1.decode())
else:
    print("Message 1: ", "INVALID")

if authenticity2:
    print("Message 2: ", m2.decode())
else:
    print("Message 2: ", "INVALID - ", m2.decode())