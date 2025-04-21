from pwn import *

HOST = 'chall.fcsc.fr'
PORT = 2105

FILENAME_KNOWN = 'xortp'
FILENAME_FLAG = 'flag.txt'

# Copie du code source (contenu connu)
with open('xortp.c', 'rb') as f:
    known_plaintext = f.read(128)  # Attention à bien caler sur le même début que le serveur lit

def get_cipher(filename):
    io = remote(HOST, PORT)
    io.recvuntil(b'Which file would like to encrypt?\n')
    io.sendline(filename.encode())
    cipher_hex = io.recvline().strip().decode()

    print(f"[DEBUG] Réponse reçue : {cipher_hex}")  # 🔥 Ajout ici

    io.close()
    return bytes.fromhex(cipher_hex)


def xor_bytes(a, b):
    return bytes(x ^ y for x, y in zip(a, b))

# Étape 1 : obtenir le chiffré de xortp.c
print("[*] Récupération du chiffré de xortp.c...")
c_xortp = get_cipher(FILENAME_KNOWN)

# Étape 2 : déduire la clé : clé = clair ⊕ chiffré
key = xor_bytes(known_plaintext[:len(c_xortp)], c_xortp)

# Étape 3 : récupérer le chiffré du flag
print("[*] Récupération du chiffré du flag...")
c_flag = get_cipher(FILENAME_FLAG)

# Étape 4 : déchiffrer le flag
flag = xor_bytes(c_flag, key[:len(c_flag)])

print("[+] FLAG (cleaned):", ''.join([chr(c) if 32 <= c < 127 else '.' for c in flag]))

for i in range(3):
    print(f"--- Tentative {i+1} ---")
    c = get_cipher('xortp')
    print(c.hex())
    print()