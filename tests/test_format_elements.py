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
    assert String("ts", {}).parse('<ts>or</ts>') == "or"

def test_empty_string_build():
    assert String("brooo", {}).build("") in ('<brooo></brooo>', "<brooo />")

def test_empty_string_parse():
    assert String("brooo", {}).parse('<brooo></brooo>') == ""
    assert String("brooo", {}).parse('<brooo />') == ""

def test_hex_build():
    assert Hex("test", {}).build(255) == '<test>FF</test>'

def test_hex_parse():
    assert Hex("test", {}).parse('<test>FF</test>') == 255
