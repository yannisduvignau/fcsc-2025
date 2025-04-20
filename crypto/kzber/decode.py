import os
import json
import zlib
import base64
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad
from sage.all import *

# Définir la classe Kzber, tel qu'implémentée dans le code initial
class Kzber:
    def __init__(self, q = 3329, d = 256, k = 2, B = 2):
        self.q = q
        self.d = d
        self.k = k
        self.B = B
        Zq, Y = PolynomialRing(GF(q), 'Y').objgen()
        R, X = Zq.quotient_ring(Y**d - 1, 'X').objgen()
        self.R = R
        self.X = X
        self._keygen()

    def _sample_short_poly(self):
        coeffs = [randint(-self.B, self.B) for i in range(self.d)]
        return self.R(coeffs)

    def _sample_short_vector(self):
        return vector(self.R, [self._sample_short_poly(), self._sample_short_poly()]).column()

    def _keygen(self):
        A = random_matrix(self.R, 2, 2)
        s  = self._sample_short_vector()
        e1 = self._sample_short_vector()
        t = A * s + e1
        self.sk = s
        self.pk = (A, t)

    def encrypt(self, m):
        A, t = self.pk
        r  = self._sample_short_vector()
        e2 = self._sample_short_vector()
        e3 = self._sample_short_poly()
        u = r.transpose() * A + e2.transpose()
        v = r.transpose() * t + e3 + (int(round(self.q/2)) * self.R(m))
        return u, v
    
    def decrypt(self, c):
        u, v = c
        w = (v - u * self.sk)[0, 0]
        coeffs = list(w)
        coeffs = [int(wi) if int(wi) < self.q//2 else int(wi) - self.q for wi in coeffs]
        return [0 if abs(wi) <= self.q//4 else 1 for wi in coeffs]

# Base64 décodage et compression des données
data = base64.b64decode("VOTRE_BASE64_ICI")
data = zlib.decompress(data)
data = pickle.loads(data)

# Récupérer les informations de la sérialisation
A = data['A']
t = data['t']
C = data['C']
flag_info = data['flag']
iv = flag_info['iv']
enc = flag_info['enc']

# Recréer l'instance Kzber avec la clé publique
PKE = Kzber()
PKE.pk = (A, t)

# Déchiffrer la clé secrète 'sk' à partir de C
# 'C' contient les chiffres binaires de 'sk', déchiffrons-le.
sk_bits = []
for c in C:
    sk_bits.extend(PKE.decrypt(c))

# Convertir les bits en un nombre entier
sk_bin = ''.join(map(str, sk_bits))
sk = int(sk_bin, 2)

# Déchiffrer le flag avec AES
E = AES.new(sk.to_bytes(16, 'big'), AES.MODE_CBC, iv=iv)
flag = unpad(E.decrypt(enc), 16)

# Afficher le flag
print(flag.decode())
