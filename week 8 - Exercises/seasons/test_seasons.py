from seasons import convert

def test_main():
    assert convert(365) == "Five hundred twenty-five thousand, six hundred minutes"
    assert convert(730) == "One million, fifty-one thousand, two hundred minutes"


#  para correr, no terminal: pytest nomeficheiro.py
