import pytest
from working import convert

def test_convert():
    assert convert("9:30 AM to 2:35 PM") == "09:30 to 14:35"
    assert convert("3 PM to 5 PM") == "15:00 to 17:00"
    assert convert("6 AM to 6 PM") == "06:00 to 18:00"


def test_error():
    with pytest.raises(ValueError):
        convert("9AM - 5PM")
    with pytest.raises(ValueError):
        convert("09:00 to 17:00")
    with pytest.raises(ValueError):
        convert("15:00 AM to 25:00 PM")
    with pytest.raises(ValueError):
        convert("9:60 AM to 5:60 PM")


#  para correr, no terminal: pytest nomeficheiro.py
