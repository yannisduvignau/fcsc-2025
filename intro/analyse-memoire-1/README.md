# =====================
#  Epreuve Analyse mémoire - Pour commencer (1/2)
# =====================

Enoncé : Vous vous préparez à analyser une capture mémoire et vous notez quelques informations sur la machine avant de plonger dans l'analyse :

nom d'utilisateur,
nom de la machine,
adresse IPv4, non locale, de la machine.
Le flag est au format FCSC{<nom d'utilisateur>:<nom de la machine>:<adresse IPv4>} où :

<nom d'utilisateur> est le nom de l'utilisateur qui utilise la machine,
<nom de la machine> est le nom de la machine analysée et
<adresse IPv4> est l'adresse IPv4, non locale, de la machine.
Par exemple : FCSC{Arthur:Ordinateur-de-rct:192.168.1.150}.

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
    python3 volatility3/vol.py -f analyse-memoire.dmp windows.pslist
    python3 volatility3/vol.py -f analyse-memoire.dmp windows.psscan
    python3 volatility3/vol.py -f analyse-memoire.dmp windows.sessions
```
```bash
    nom d'utilisateur userfcsc-10 avec : python3 volatility3/vol.py -f analyse-memoire.dmp windows.registry.userassist
    nom de la machine DESKTOP-JV996VQ avec : 
     - python3 volatility3/vol.py -f analyse-memoire.dmp windows.registry.printkey
     - python3 volatility3/vol.py -f analyse-memoire.dmp windows.registry.printkey --offset 0xb88510266000 --key "ControlSet001\\Control\\ComputerName\\ComputerName"

     ou

     - python3 volatility3/vol.py -f analyse-memoire.dmp windows.envars | grep USERNAME
    ip 10.0.2.15 avec : python3 volatility3/vol.py -f analyse-memoire.dmp windows.netscan

```

Résultat : FCSC{userfcsc-10:DESKTOP-JV996VQ:10.0.2.15}