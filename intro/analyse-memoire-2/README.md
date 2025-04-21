# =====================
#  Epreuve Analyse mémoire - Pour commencer (2/2)
# =====================

Enoncé : La capture mémoire a été réalisée pendant qu'un utilisateur était en train de travailler sur un document hautement sensible. Si une compromission du poste a eu lieu, ce document a peut-être été volé. Pouvez-vous retrouver :

le nom du logiciel d'édition du document,
le nom du document.
Le flag est au format FCSC{<nom du logiciel>:<nom du document>} où :

<nom du logiciel> est le nom de l'exécutable du logiciel d'édition et
<nom du document> est le nom du document en cours d'édition par l'utilisateur (sans le chemin du fichier).
Par exemple : FCSC{calc.exe:Mes comptes 2025.txt}.

Attention : pour cette épreuve, vous n'avez que 10 tentatives de flag.


```bash
    1 fichier tar
```

Solution : 
```bash
    tar -xvf analyse-memoire.tar.xz
    git clone https://github.com/volatilityfoundation/volatility3.git
    cd volatility3
    python3 -m venv venv && . venv/bin/activate
    pip install -e ".[dev]"
    cd ..
    echo ".gitignore\nanalyse-memoire*\nvolatility*" > .gitignore
    python3 volatility3/vol.py -f analyse-memoire.dmp windows.info
```
```bash
    
```

Résultat : FCSC{}