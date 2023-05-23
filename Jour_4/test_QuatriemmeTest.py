"""
1:
"""

import pytest
###le module
# def setup_module(module):
#     print("ouvrir la base de donnee")
# def teardown_module(module):
#         print("fermer la base de donnee")
# def setup_function(function):
#     print("ouvrir le navigateur")
#  def teardown_function(function):
#         print("fermer le navigateur")
@pytest.fixture(scope="module")
def setup():
    print("ouvrir la base de donnee")
    yield
    print("fermer la base de donnee")
@pytest.fixture(scope="module")
def before():
    print("ouvrir le navigateur")
    yield
    print("fermer le navigateur")
@pytest.mark.usefixtures("setup" ,"before")
def test_login():
   # print("ouvrir le navigateur")
    print("ce connecter sur qoogle")
   # print("fermer le navigateur")
@pytest.mark.usefixtures("setup" ,"before")
def test_creerCompte():
    #print("ouvrir le navigateur")
    print("Creer un  compte  sur qoogle")
    #print("fermer le navigateur")
@pytest.mark.usefixtures("setup", "before")
def test_reenitialiserPass():
        # print("ouvrir le navigateur")
        print("Reenitialiser mot de pass")
        # print("fermer le navigateur")
