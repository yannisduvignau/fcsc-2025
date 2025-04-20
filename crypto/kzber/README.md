# =====================
#  Epreuve Kzber
# =====================

Enoncé : 


```bash  
    1 fichier py
    nc chall.fcsc.fr 2155
```

Solution : 
```bash
    python3 -m venv env
    source env/bin/activate
    echo "pycryptodome" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
```

Résultat : FCSC{}