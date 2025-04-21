# =====================
#  Epreuve SOCrate 1/6 - Technologie
# =====================

Enoncé : En juin 2023, un opérateur d'importance vitale est victime d'une attaque compromettant tout son système d'information. Vous avez reçu les logs Linux et Windows et vous devez répondre aux questions des enquêteurs.

Note : Les parties sont numérotées dans l'ordre chronologique de l'attaque, mais il n'est pas nécessaire de les résoudre dans l'ordre.
Sur la machine webserver, sous quel chemin tourne l'application web ?

Format du flag : FCSC{/var/www/***/************/}

```bash
    fichier tar
```

Solution : 
```bash
    tar -xvf socrate.tar.xz
    cd socrate
    rm -r windows
    cd linux
```
CTRL F "/var/www/"

Résultat : FCSC{/var/www/app/banque_paouf/}

```bash
    cd ../..
    rm -r socrate
```