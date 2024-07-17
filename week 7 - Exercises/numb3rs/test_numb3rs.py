import pytest
from numb3rs import validate

def test_validate():
    assert validate("127.472.398.647") == False
    assert validate("1.1.1.1") == True
    assert validate("127.01.01.0") == True
    assert validate("255.255.255.255") == True
    assert validate("512.512.512.512") == False
    assert validate("512.01.25.25") == False
    assert validate("127.0.0.0") == True
    assert validate("512.0.0.0") == False
    assert validate("cat") == False



#  para correr, no terminal: pytest nomeficheiro.py
