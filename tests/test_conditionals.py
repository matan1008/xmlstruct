from xmlstruct import Int, Optional, ValueContainer, Struct, Container


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


def test_optional_recursive_build_none():
    xml_struct = Struct(
            "test",
            Int("testint"),
            Optional(Int("optestint"))
    )
    obj = Container({"testint": 3}, xml_attrib={"attr": "attrv"})
    assert xml_struct.build(obj) == '<test attr="attrv"><testint>3</testint></test>'


def test_optional_recursive_parse_none():
    xml_struct = Struct(
            "test",
            Int("testint"),
            Optional(Int("optestint"))
    )
    obj = Container({"testint": 3, "optestint": None}, xml_attrib={"attr": "attrv"})
    assert xml_struct.parse('<test attr="attrv"><testint>3</testint></test>') == obj
