# =====================
#  Epreuve Smölkkey
# =====================

Enoncé : 

```bash
    2 fichiers (txt et py)
```

Solution : 
```bash
    python3 -m venv env
    source env/bin/activate
    echo "pycryptodome" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
    python3 decode.py
    deactivate
```

Résultat : FCSC{30f7c4b2fa7f0fb48bfbd9bbd413491c0a6da660764961b862fe38a83b4bc00f}