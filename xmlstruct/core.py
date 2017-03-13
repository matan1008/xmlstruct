from xml.etree import ElementTree
from abc import ABCMeta, abstractmethod
from xml_element import XmlElement
from container import Container

class Struct(XmlElement):
    """
    A sequence of xml elements.

    The elements are parsed and built and the order they are defined
    """
    def  __init__(self, tag, attrib, *children):
        XmlElement.__init__(self, tag, attrib)
        self.children = children

    def _build(self, obj):
        element = ElementTree.Element(self.tag, self.attrib)
        for child in self.children:
            element.append(child._build(obj[child.tag]))
        return element

    def _parse(self, element):
        obj = Container()
        for child, subelement in zip(self.children, element):
            obj[subelement.tag] = subelement._parse(child)
        return obj


class FormatElement(XmlElement):
    """
    A leaf element that requires formatting (any leaf when thinking about it)

    The element is parsed and built with parse_func and build_func accordingly
    """
    __metaclass__ = ABCMeta

    def  __init__(self, tag, attrib):
        XmlElement.__init__(self, tag, attrib)

    @abstractmethod
    def parse_func(self, text):
        """
        This function parses element text

        It return any wanted value
        """
        raise NotImplementedError()

    @abstractmethod
    def build_func(self, value):
        """
        This function "builds" a value

        The function gets the value and returns string
        """
        raise NotImplementedError()

    def _build(self, obj):
        element = ElementTree.Element(self.tag, self.attrib)
        element.text = self.build_func(obj)
        return element

    def _parse(self, element):
        return self.parse_func(element.text)


class String(FormatElement):
    """
    A FormatElement that for string

    Sounds unnecessary, but makes the project cleaner and clearer
    """
    def build_func(self, value):
        return value

    def parse_func(self, text):
        return text if text is not None else ""


class Int(FormatElement):
    """
    A FormatElement that for int
    """
    def build_func(self, value):
        return str(value)

    def parse_func(self, text):
        return int(text)


class Float(FormatElement):
    """
    A FormatElement that for float
    """
    def build_func(self, value):
        return str(value)

    def parse_func(self, text):
        return float(text)


class Hex(FormatElement):
    """
    A FormatElement that for hexadecimal, receives int as value
    """
    def build_func(self, value):
        return "%X" % value

    def parse_func(self, text):
        return int(text, 16)
