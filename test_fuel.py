from fuel import convert, guage


def test_convert():
    assert convert("1/2") == 50
    assert convert("2/5") == 40
    assert convert("3/0") == None
    assert convert("c/g") == None
    assert convert("12") == None
    assert convert("ef") == None


def test_guage():
    assert guage(0) == "E"
    assert guage(1) == "E"
    assert guage(75) == "75%"
    assert guage(99) == "F"
    assert guage(100) == "F"
    assert guage(None) == "Input not right"
