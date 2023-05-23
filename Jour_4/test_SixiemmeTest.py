"""
1:
"""

import pytest



@pytest.mark.charge
def test_1():
    # print("ouvrir le navigateur")
    print("test1")
    # print("fermer le navigateur")
@pytest.mark.regressiom
def test_2():
        # print("ouvrir le navigateur")
        print("test2")
        # print("fermer le navigateur")
@pytest.mark.charge
def test_3():
            # print("ouvrir le navigateur")
            print("test3")
            # print("fermer le navigateur")
@pytest.mark.charge
def test_4():
    # print("ouvrir le navigateur")
    print("test4")
    # print("fermer le navigateur")
@pytest.mark.skip
def test_5():
    # print("ouvrir le navigateur")
    print("test5")
    # print("fermer le navigateur")