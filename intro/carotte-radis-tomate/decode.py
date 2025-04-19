from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from sympy.ntheory.modular import crt
from binascii import unhexlify

# Moduli (les nombres premiers)
mods = [
    17488856370348678479,
    16548497022403653709,
    17646308379662286151,
    14933475126425703583,
    17256641469715966189
]

# Restes
rests = [
    392278890668246705,
    4588810924820033807,
    17164682861166542664,
    12928514648456294931,
    5973470563196845286
]

# Résolution par CRT
K, _ = crt(mods, rests)

# Conversion en clé AES (32 octets)
key = int(K).to_bytes(32, 'big')

# Chiffrement à déchiffrer (en bytes)
enc_hex = "2da1dbe8c3a739d9c4a0dc29a27377fe8abc1c0feacc9475019c5954bbbf74dcedce7ed3dc3ba34fa14a9181d4d7ec0133ca96012b0a9f4aa93c42c61acbeae7640dd101a6d2db9ad4f3b8ccfe285e0d"
enc = unhexlify(enc_hex)

# Déchiffrement
cipher = AES.new(key, AES.MODE_ECB)
flag = unpad(cipher.decrypt(enc), 16)

print("🎉 FLAG =", flag.decode())
