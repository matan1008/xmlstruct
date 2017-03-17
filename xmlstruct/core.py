from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import Container


class Struct(XmlElement):
    """
    A sequence of xml elements.

    The elements are parsed and built and the order they are defined
    """

    def __init__(self, tag, attrib, *children):
        XmlElement.__init__(self, tag, attrib)
        self.children = children

    def _build(self, obj):
        element = ElementTree.Element(self.tag, self.attrib)
        for child in self.children:
            sub_obj = Container({child.tag: obj[self.tag][child.tag]})
            element.append(child._build(sub_obj))
        return element

    def _parse(self, element):
        obj = Container()
        obj[self.tag] = Container()
        for child, subelement in zip(self.children, element):
            obj[self.tag].update(child._parse(subelement))
        return obj
