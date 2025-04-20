# =====================
#  Epreuve Speak To Me
# =====================

Enoncé : Nous avons trouvé un microcontrôleur qui parle un protocole binaire inconnu sur une liaison série, pouvez-vous en trouver les secrets ?


```bash  
    nc chall.fcsc.fr 2303
```

Solution : 
```bash
    nc chall.fcsc.fr 2303 | tee capture.txt
```

Résultat : FCSC{}