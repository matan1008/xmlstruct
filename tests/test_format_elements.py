from xmlstruct import Int, Float, String, Hex, Container


def test_int_build():
    obj = Container(test=6)
    assert Int("test", {"attr": "check"}).build(obj) == '<test attr="check">6</test>'


def test_int_parse():
    obj = Container(test=6)
    assert Int("test", {"attr": "check"}).parse('<test attr="check">6</test>') == obj


def test_float_build():
    obj = Container(test=4.2)
    assert Float("test", {}).build(obj) == '<test>4.2</test>'


def test_float_parse():
    obj = Container(test=4.2)
    assert Float("test", {}).parse('<test>4.2</test>') == obj


def test_string_build():
    obj = Container(ts="or")
    assert String("ts", {}).build(obj) == '<ts>or</ts>'


def test_string_parse():
    obj = Container(ts="or")
    assert String("ts", {}).parse('<ts>or</ts>') == obj


def test_empty_string_build():
    obj = Container(brooo="")
    assert String("brooo", {}).build(obj) in ('<brooo></brooo>', "<brooo />")


def test_empty_string_parse():
    obj = Container(brooo="")
    assert String("brooo", {}).parse('<brooo></brooo>') == obj
    assert String("brooo", {}).parse('<brooo />') == obj


def test_hex_build():
    obj = Container(test=255)
    assert Hex("test", {}).build(obj) == '<test>FF</test>'


def test_hex_parse():
    obj = Container(test=255)
    assert Hex("test", {}).parse('<test>FF</test>') == obj
