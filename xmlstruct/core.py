from xml.etree import ElementTree
from xml_element import XmlElement
from container import Container

class Struct(XmlElement):
    """
    A sequence of xml elements.

    The elements are parsed and built and the order they are defined
    """
    def  __init__(self, tag, attrib, *children):
        XmlElement.__init__(tag, attrib)
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
