# =====================
#  Epreuve La quete de l'anneau
# =====================

Enoncé : Sauron a mis au point un système de chiffrement pour communiquer avec les Nazgûl. Il n'a pas pu s'empêcher d'utiliser un anneau secret pour le sécuriser. Vos alliés elfes ont tendu leurs oreilles pour intercepter des messages. Saurez-vous montrer à Sauron que sa maîtrise des anneaux n'est pas encore au point ?


```bash  
    2 fichiers
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

Résultat : FCSC{96fd29a6fc2301da363a4392cd4a9b9465d65b029a52913add2fd4001d}