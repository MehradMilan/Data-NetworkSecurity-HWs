from pgpy import PGPKey, PGPUID
from pgpy.constants import PubKeyAlgorithm, KeyFlags, HashAlgorithm \
, SymmetricKeyAlgorithm, CompressionAlgorithm

NAME = "Mehrad Milanloo"
EMAIL = "milanloomehrad@gmail.com"

# Generate a new key pair
key = PGPKey.new(PubKeyAlgorithm.RSAEncryptOrSign, 2048)
uid = PGPUID.new(NAME, email=EMAIL)

# Add the UID to the key
key.add_uid(uid, usage={KeyFlags.Sign
                        , KeyFlags.EncryptCommunications
                        , KeyFlags.EncryptStorage}
                        , hashes=[HashAlgorithm.SHA256]
                        , ciphers=[SymmetricKeyAlgorithm.AES256]
                        , compression=[CompressionAlgorithm.ZLIB])

# Export the public key
with open("public_key.asc", "w") as f:
    f.write(str(key.pubkey))

# Export the private key
with open("private_key.asc", "w") as f:
    f.write(str(key))