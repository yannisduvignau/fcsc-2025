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
    python3 -m venv env
    source env/bin/activate
    echo "pwntools" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
    python3 decode.py
    deactivate
```

Résultat : FCSC{}