### 1:instalation "pytest"--->pip install pytest
### creer un fichier python__>doit contienir le mot "test" au bebut
###pour executer les test on doit aller dans le dossier des tests et on execute la commande suivante
### pytest test_PremierTest.py -s -v

import pytest
def test_login():
    print("ce connecter sur qoogle")

def test_creerCompte():
    print("Creer  compte  sur qoogle")
