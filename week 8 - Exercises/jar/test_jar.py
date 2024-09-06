from jar import Jar
import pytest

def test_init():
    jar = Jar()


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(8)
    assert jar.size == 8

    with pytest.raises(ValueError):
        jar.deposit(13)


def test_withdraw():
    jar = Jar()
    jar.deposit(12)
    jar.withdraw(7)
    assert jar.size == 5


    with pytest.raises(ValueError):
        jar.withdraw(14)


#  para correr, no terminal: pytest nomeficheiro.py
