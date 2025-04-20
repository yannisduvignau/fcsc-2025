import os
import json
import zlib
import base64
import pickle
from Crypto.Cipher import AES
from Crypto.Util.Padding import pad
from sage.all import *

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

PKE = Kzber()
A, t = PKE.pk
sk = randint(0, 2 ** 128)
C = [ PKE.encrypt(int(m)) for m in f"{sk:0128b}" ]

flag = open("flag.txt", "rb").read()
iv = os.urandom(16)
E = AES.new(int.to_bytes(sk, 16), AES.MODE_CBC, iv = iv)
enc = E.encrypt(pad(flag, 16))

print(base64.b64encode(zlib.compress(pickle.dumps({
    "A": A,
    "t": t,
    "C": C,
    "flag" : {
        "iv": iv,
        "enc": enc,
    }
}))).decode())
