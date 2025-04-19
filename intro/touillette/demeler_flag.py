def demeler_flag(scrambled):
    """
    Démêle un flag qui a été mélangé par le script touillette.py.

    Args:
        flag_melange (str): La chaîne de caractères du flag mélangé.

    Returns:
        str: Le flag original.
    """
    n = len(scrambled)
    if n != 64:
        return "La longueur du flag mélangé n'est pas de 64 caractères."


    # Étape 1 : Inverser x[1::2] + x[0::2]
    x = [""] * 64
    x[1::2] = list(scrambled[:32])
    x[0::2] = list(scrambled[32:])

    # Étape 2 : Inverser le mélange fait par:
    # x = flag[-8::-8] + flag[-7::-8] + ... + flag[-1::-8]

    # Pour chaque i de 0 à 7, flag[-(i+1):: -8] prend les positions:
    # 63 - i, 55 - i, 47 - i, ..., 7 - i

    # Créons une map de position : position du flag → index dans x
    flag_to_x = {}
    for i in range(8):
        for j in range(8):
            flag_index = (7 - j) * 8 + i  # ceci donne les index parcourus dans le flag
            x_index = i * 8 + j
            flag_to_x[flag_index] = x_index

    # Reconstruire le flag
    flag = [""] * 64
    for flag_index, x_index in flag_to_x.items():
        flag[flag_index] = x[x_index]

    return "".join(flag)

if __name__ == "__main__":
    flag_melange = open("output2.txt").read()
    flag_original = demeler_flag(flag_melange)
    print(f"Le flag original est : {flag_original}")
