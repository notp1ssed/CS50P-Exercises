from bank import value

def test_value():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("hey") == 20
    assert value("Hallo") == 20
    assert value("what's up") == 100
    assert value("30 dollars") == 100
    assert value("bye") == 100

#  para correr, no terminal: pytest nomeficheiro.py
