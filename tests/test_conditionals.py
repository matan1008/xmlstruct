from xmlstruct import Int, Optional, ValueContainer

def test_optional_int_build():
    obj = ValueContainer(6, xml_attrib={"attr": "check"})
    assert Optional(Int("test")).build(obj) == '<test attr="check">6</test>'


def test_optional_int_parse():
    obj = ValueContainer(6, xml_attrib={"attr": "check"})
    assert Optional(Int("test")).parse('<test attr="check">6</test>') == obj


def test_optional_int_build_none():
    obj = None
    assert Optional(Int("test")).build(obj) == ''


def test_optional_int_parse_none():
    obj = None
    assert Optional(Int("test"))._parse(None) == obj
