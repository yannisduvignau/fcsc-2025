# =====================
#  Epreuve Intro to pwntools
# =====================

Enoncé : Ceci n'est pas une vraie épreuve, mais plutôt un exemple d'utilisation de Python pour communiquer avec les services distants du FCSC, de Hackropole, et plus généralement de n'importe quelle service exposant un port TCP.

Si vous n'êtes pas familier avec ces concepts, commencez par installer le package Python pwntools sur votre machine. Celui-ci est extrêmement utile en CTF et permet de simplifier l'écriture de beaucoup de choses.

Dans notre cas, nous allons uniquement nous en servir pour communiquer avec un service exposant un port TCP.

Ce service est accessible ici : nc chall.fcsc.fr 2053.

le port est le port TCP numéro 2053,
le serveur est situé à l'adresse chall.fcsc.fr,
nc (netcat) est un utilitaire permettant de se connecter à un port TCP.
Bien qu'il soit possible de résoudre cette épreuve à la main ou directement à partir du fichier template.py fourni, nous vous conseillons d'étudier les différentes fonctions utilisées dans template.py. Celles-ci sont les principales fonctions utilisées dans pwntools pour communiquer avec les services distants, et elles pourront vous être utiles pour les autres épreuves du FCSC ou de Hackropole.

```bash
    nc chall.fcsc.fr 2053
```

Solution : 
```bash
    python3 -m venv env
    source env/bin/activate
    echo "pwntools" > requirements.txt
    pip install -r requirements.txt
    echo ".gitignore\nenv/" > .gitignore
    python3 template.py
    deactivate
```

Résultat : FCSC{d31df42c489570dae488fa071326510903ef452dcde00a2dd22447c7d15ae104}