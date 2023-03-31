from ecdsa import SigningKey, SECP256k1

# sk = signing key / verifying key
# vk = verifying key

sk = SigningKey.generate(curve=SECP256k1)

print(sk.to_string().hex())

vk = sk.verifying_key

print(vk.to_string().hex())

signature = sk.sign(b"Not your keys, not your coins!")

print(signature.hex())

assert vk.verify(signature, b"Not your keys, not your coins!")
