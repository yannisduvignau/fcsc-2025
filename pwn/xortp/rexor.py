def xor_bytes(b1, b2):
    return bytes([x ^ y for x, y in zip(b1, b2)])

# Chiffré reçu du serveur pour le fichier xortp
xortp_cipher_hex = "7c594ebb87d5e8890d065f6c062f31d70b36bfc50ed011cc1f2a48fe9811bfd7a6f950773b11c75272405834983974126f7b6d1afc31e066a71a1f796682ba19b0d3a45edcef72"  # <= remplace par le long hex que tu as reçu
xortp_cipher = bytes.fromhex(xortp_cipher_hex)

# Charge le vrai binaire xortp localement
with open("xortp", "rb") as f:
    xortp_plain = f.read()

assert len(xortp_plain) == len(xortp_cipher), "Taille différente !"

# Récupère la clé OTP utilisée lors du chiffrement de xortp
otp_key = xor_bytes(xortp_plain, xortp_cipher)

# Chiffré du flag récupéré précédemment
flag_cipher_hex = "95ed724b4c9d2a03c925b4897ad1869b9d9ca17d7447ff6b6663266f11446c58e2ba0ae1fbeab93dc084a64c22bfef21892389e8a78fd248322d354e8d4859514e7bd0cd88fbdf"
flag_cipher = bytes.fromhex(flag_cipher_hex)

# Déchiffre le flag
flag_plain = xor_bytes(flag_cipher, otp_key[:len(flag_cipher)])

print("🔓 Flag :")
print(flag_plain.decode(errors="replace"))
