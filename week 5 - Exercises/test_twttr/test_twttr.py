from twttr import value

def test_shorten():
    assert shorten("twitter") == "twttr"
    assert shorten("hello") == "hll"
    assert shorten("yau.") == "y."
    assert shorten("number 75") == "nmbr 75"
    assert shorten("RUI") == "R"

#  para correr, no terminal: pytest nomeficheiro.py
