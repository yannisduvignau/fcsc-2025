import math

# Fonction pour résoudre le problème
def solve_equation():
    # On va tester différentes valeurs de a et calculer c, b, x et y à partir de là.
    for a in range(1, 10000):  # Tester les valeurs possibles pour a
        # Calcul de c en fonction de a
        if a % 487 != 0:
            continue
        c = a // 487
        
        # Calcul de b en fonction de a
        b = (159 * a) / 485
        if b != int(b):  # Vérifier que b est un entier
            continue
        b = int(b)

        # Vérifier que x^2 == a + b
        x_squared = a + b
        x = math.isqrt(x_squared)
        if x * x != x_squared:  # Vérifier que x est une solution entière
            continue

        # Résoudre l'équation quadratique pour y : y * (3 * y - 1) = 2 * b
        # y * (3y - 1) = 2b  -->  3y^2 - y - 2b = 0
        discriminant = 1 + 24 * b
        if discriminant < 0:
            continue
        sqrt_discriminant = math.isqrt(discriminant)
        if sqrt_discriminant * sqrt_discriminant != discriminant:
            continue
        # Trouver les racines de l'équation
        y1 = (1 + sqrt_discriminant) // 6
        y2 = (-1 - sqrt_discriminant) // 6
        if y1 > 0 and y1 * (3 * y1 - 1) == 2 * b:
            y = y1
        elif y2 > 0 and y2 * (3 * y2 - 1) == 2 * b:
            y = y2
        else:
            continue

        # Si on trouve une solution valide, calculer le hash SHA256
        from hashlib import sha256
        h = sha256(str(a).encode()).hexdigest()
        return f"FCSC{{{h}}}"

    return "Nope!"

# Résoudre l'équation
print(solve_equation())
