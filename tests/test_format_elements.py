from xmlstruct import Int, Float, String, Hex

def test_int_build():
    assert Int("test", {"attr":"check"}).build(6) == '<test attr="check">6</test>'

def test_int_parse():
    assert Int("test", {"attr":"check"}).parse('<test attr="check">6</test>') == 6

def test_float_build():
    assert Float("test", {}).build(4.2) == '<test>4.2</test>'

def test_float_parse():
    assert Float("test", {}).parse('<test>4.2</test>') == 4.2

def test_string_build():
    assert String("ts", {}).build("or") == '<ts>or</ts>'

def test_string_parse():
    assert String("test", {}).parse('<ts>or</ts>') == "or"
