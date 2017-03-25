# coding=utf-8
from xmlstruct import Int, Optional, ValueContainer, Struct, Container, Switch, Float, String
from xmlstruct.exceptions import SwitchNoMatchError, SwitchSeveralMatchError
import pytest


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


def test_switch_build():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")})
    obj = 7
    assert xml_switch.build(obj) == "<int>7</int>"


def test_switch_parse():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")})
    obj = 7
    assert xml_switch.parse("<int>7</int>") == obj


def test_switch_same_tag_parse():
    xml_switch = Switch(type, {int: Int("int"), float: Float("int")})
    obj = 7.7
    assert xml_switch.parse("<int>7.7</int>") == obj


def test_switch_default_build():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")}, String("string"))
    obj = "7"
    assert xml_switch.build(obj) == "<string>7</string>"


def test_switch_default_parse():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")}, String("string"))
    obj = "7"
    assert xml_switch.parse("<string>7</string>") == obj


def test_recursive_switch_build():
    xml_switch = Switch(
            type,
            {float: Float("float"), int: Switch(
                    lambda x: x % 2,
                    {0: Int("even"), 1: Int("odd")}
            )}
    )
    obj = 3.4
    assert xml_switch.build(obj) == "<float>3.4</float>"
    obj = 3
    assert xml_switch.build(obj) == "<odd>3</odd>"


def test_recursive_switch_parse():
    xml_switch = Switch(
            type,
            {float: Float("float"), int: Switch(
                    lambda x: x % 2,
                    {0: Int("even"), 1: Int("odd")}
            )}
    )
    obj = 3.4
    assert xml_switch.parse("<float>3.4</float>") == obj
    obj = 3
    assert xml_switch.parse("<odd>3</odd>") == obj


def test_switch_no_match_build():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")})
    obj = "7"
    with pytest.raises(SwitchNoMatchError):
        xml_switch.build(obj)


def test_switch_no_match_parse():
    xml_switch = Switch(type, {int: Int("int"), float: Float("float")})
    with pytest.raises(SwitchNoMatchError):
        xml_switch.parse("<string>7</string>")
    with pytest.raises(SwitchNoMatchError):
        xml_switch.parse("<int>a</int>")


def test_switch_several_match_parse():
    xml_switch = Switch(type, {int: Int("int"), str: String("int")})
    with pytest.raises(SwitchSeveralMatchError):
        xml_switch.parse("<int>7</int>")


def test_structured_switch_build():
    xml_struct = Struct(
            "test",
            Switch(type, {int: Int("int"), float: Float("float")}),
            String("description")
    )
    obj = Container(int=3, description="What")
    assert xml_struct.build(obj) == "<test><int>3</int><description>What</description></test>"


def test_structured_switch_parse():
    xml_struct = Struct(
            "test",
            Switch(type, {int: Int("int"), float: Float("float")}),
            String("description")
    )
    obj = Container(int=3, description="What")
    assert xml_struct.parse("<test><int>3</int><description>What</description></test>") == obj
