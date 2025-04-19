# =====================
#  Epreuve Yabof
# =====================

Enoncé : Yet Another Buffer Overflow!

```bash
    1 fichier 
    nc chall.fcsc.fr 2109
```

Solution : 
```bash
    python3 -m venv env
    source env/bin/activate
    echo "pwntools" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
    python3 buffer.py
    deactivate
```

Résultat : FCSC{}