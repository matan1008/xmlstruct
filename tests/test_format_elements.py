from xmlstruct import Int, Float, String, Hex

def test_int_build():
    assert Int("test", {"attr":"check"}).build(6) == '<test attr="check">6</test>'

def test_int_parse():
    assert Int("test", {"attr":"check"}).parse('<test attr="check">6</test>') == 6
