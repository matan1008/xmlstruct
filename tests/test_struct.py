from xmlstruct import Struct, Container, Int, String, OrderedStruct, OrderedPairContainer, ValueContainer


def test_struct_build():
    xml_struct = Struct(
            "test",
            Int("testint"),
            String("teststring")
    )
    obj = Container({"testint": 3, "teststring": "night"}, xml_attrib={"attr": "attrv"})
    assert xml_struct.build(obj) == '<test attr="attrv"><testint>3</testint><teststring>night</teststring></test>'


def test_struct_parse():
    xml_struct = Struct(
            "test",
            Int("testint"),
            String("teststring")
    )
    obj = Container({"testint": 3, "teststring": "night"}, xml_attrib={"attr": "attrv"})
    assert xml_struct.parse('<test attr="attrv"><testint>3</testint><teststring>night</teststring></test>') == obj


def test_recursive_struct_build():
    xml_struct = Struct(
            "testa",
            Struct(
                    "testb",
                    Int("testint"),
                    String("string")
            )
    )
    obj = Container(testb={"testint": 3, "string": "night"})
    assert xml_struct.build(obj) == '<testa><testb><testint>3</testint><string>night</string></testb></testa>'


def test_recursive_struct_parse():
    xml_struct = Struct(
            "testa",
            Struct(
                    "testb",
                    Int("testint"),
                    String("string")
            )
    )
    obj = Container(testb={"testint": 3, "string": "night"})
    assert xml_struct.parse('<testa><testb><testint>3</testint><string>night</string></testb></testa>') == obj


def test_same_tags_subelements_build():
    xml_struct = OrderedStruct(
            "test",
            String("string"),
            String("string")
    )
    obj = OrderedPairContainer(("string", "3"), ("string", "4"))
    assert xml_struct.build(obj) == '<test><string>3</string><string>4</string></test>'


def test_same_tags_subelements_parse():
    xml_struct = OrderedStruct(
            "test",
            String("string"),
            String("string")
    )
    obj = OrderedPairContainer(("string", "3"), ("string", "4"))
    assert xml_struct.parse('<test><string>3</string><string>4</string></test>') == obj


def test_overriding_attributes():
    xml_struct = Struct(
            "testa",
            Struct(
                    "testb",
                    Int("testint", {"attr": "attra"}),
                    String("string", {"attr": "attrv"})
            )
    )
    obj = Container(testb={"testint": ValueContainer(3, xml_attrib={"attr": "attrb"}), "string": "night"})
    assert xml_struct.build(
        obj) == '<testa><testb><testint attr="attrb">3</testint><string attr="attrv">night</string></testb></testa>'
