
import pytest

### le module: est la suite de tests / le fichier python dans le quel nous avons ecris nos tests
### Le parametre (scoop/porté) "module" fait que la fonction définie s'execute UNE SEULE fois pour tout les tests
def setup_module(module):
print("ouvrire la base de donnée")

def teardown_module(module):
  print("Fermer la base de donnée")

def setup_function(function):
  print("ouvrire le navigateur")

def teardown_function(function):
  print("Fermer le navigateur")



def test_login():
#print("ouvrire le navigateur")
  print("Ce connecter sur google")
#print("Fermer le navigateur")
def test_creerCompte():
#print("ouvrire le navigateur")
 print("Creer un compte google")
#print("Fermer le navigateur")


def test_reenitialiserPass():
#print("ouvrire le navigateur")
  print("Reenitialiser mot de pass")
#print("Fermer le navigateur")