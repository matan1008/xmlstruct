from xmlstruct import Int, Range, GreedyRange, Array
from xmlstruct.exceptions import RangeError
import pytest


def test_range_build():
    xml_range = Range("test", 2, 4, Int("testint"))
    obj = [1, 2, 3]
    assert xml_range.build(obj) == r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>"


def test_range_parse():
    xml_range = Range("test", 2, 4, Int("testint"))
    obj = [1, 2, 3]
    assert xml_range.parse(r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>") == obj


def test_range_build_less():
    xml_range = Range("test", 2, 4, Int("testint"))
    obj = [1]
    with pytest.raises(RangeError):
        xml_range.build(obj)


def test_range_parse_less():
    xml_range = Range("test", 2, 4, Int("testint"))
    with pytest.raises(RangeError):
        xml_range.parse(r"<test><testint>1</testint></test>")


def test_range_build_more():
    xml_range = Range("test", 0, 2, Int("testint"))
    obj = [1, 2, 3]
    with pytest.raises(RangeError):
        xml_range.build(obj)


def test_range_parse_more():
    xml_range = Range("test", 0, 2, Int("testint"))
    with pytest.raises(RangeError):
        xml_range.parse(r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>")


def test_range_build_zero():
    xml_range = Range("test", 0, 2, Int("testint"))
    obj = []
    assert xml_range.build(obj) in (r"<test></test>", "<test />")


def test_range_parse_zero():
    xml_range = Range("test", 0, 2, Int("testint"))
    obj = []
    assert xml_range.parse(r"<test></test>") == obj
    assert xml_range.parse("<test />") == obj


def test_greedy_range_build():
    xml_greedy_range = GreedyRange("test", Int("testint"))
    obj = [1, 2, 3]
    assert xml_greedy_range.build(obj) == r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>"


def test_greedy_range_parse():
    xml_greedy_range = GreedyRange("test", Int("testint"))
    obj = [1, 2, 3]
    assert xml_greedy_range.parse(r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>") == obj


def test_array_build():
    xml_array = Array("test", 3, Int("testint"))
    obj = [1, 2, 3]
    assert xml_array.build(obj) == r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>"


def test_array_parse():
    xml_array = Array("test", 3, Int("testint"))
    obj = [1, 2, 3]
    assert xml_array.parse(r"<test><testint>1</testint><testint>2</testint><testint>3</testint></test>") == obj
