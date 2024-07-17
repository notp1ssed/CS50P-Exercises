from plates import is_valid

def test_lenght():
    assert is_valid("Helloman85") == False
    assert is_valid("Rui15") == True

def test_startalpha():
    assert is_valid("pt") == True
    assert is_valid("CS") == True
    assert is_valid("S5") == False

def test_numbers():
    assert is_valid("AAA222") == True
    assert is_valid("AAA22A") == False
    assert is_valid("AAA022") == False

def test_punct():
    assert is_valid("Rui.") == False
    assert is_valid("Joca") == True

#  para correr, no terminal: pytest nomeficheiro.py
