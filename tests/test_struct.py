from xmlstruct import Struct, Container, Int, String

def test_struct_build():
    xml_struct = Struct(
        "test",
        {"attr":"attrv"},
        Int("testint", {}),
        String("teststring", {})
    )
    obj = Container(test={"testint":3, "teststring":"night"})
    assert xml_struct.build(obj) == '<test attr="attrv"><testint>3</testint><teststring>night</teststring></test>'

def test_struct_parse():
    xml_struct = Struct(
        "test",
        {"attr":"attrv"},
        Int("testint", {}),
        String("teststring", {})
    )
    obj = Container(test={"testint":3, "teststring":"night"})
    assert xml_struct.parse('<test attr="attrv"><testint>3</testint><teststring>night</teststring></test>') == obj

def test_recursive_struct_build():
    xml_struct = Struct(
        "testa",
        {},
        Struct(
            "testb",
            {},
            Int("testint", {}),
            String("string", {})
        )
    )
    obj = Container(testa={"testb":{"testint":3, "string":"night"}})
    assert xml_struct.build(obj) == '<testa><testb><testint>3</testint><string>night</string></testb></testa>'

def test_recursive_struct_parse():
    xml_struct = Struct(
        "testa",
        {},
        Struct(
            "testb",
            {},
            Int("testint", {}),
            String("string", {})
        )
    )
    obj = Container(testa={"testb":{"testint":3, "string":"night"}})
    assert xml_struct.parse('<testa><testb><testint>3</testint><string>night</string></testb></testa>') == obj
