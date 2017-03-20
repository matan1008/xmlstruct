from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import Container


class Optional(XmlElement):
    """
    An optional element.
    In _build, if obj is None don't build the element.
    In _parse, if element is None don't parse the element
    """

    def __init__(self, child):
        XmlElement.__init__(self, child.tag, child.attrib)
        self.child = child

    def _build(self, obj):
        if obj is None:
            return ElementTree.Element(None)
        else:
            return self.child._build(obj)

    def _parse(self, element):
        if element is None:
            return None
        else:
            return self.child._parse(element)
