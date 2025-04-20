# =====================
#  Epreuve XORTP
# =====================

Enoncé : Vous pouvez chiffrer n'importe quel fichier du système avec un mécanisme inviolable digne des plus grands !


```bash  
    2 fichiers
    nc chall.fcsc.fr 2105
```

Solution : 
```bash
    gcc xortp.c -o xortp
    python3 -m venv env
    source env/bin/activate
    echo "binascii" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
    python3 rexor.py
    deactivate
```

Résultat : FCSC{}