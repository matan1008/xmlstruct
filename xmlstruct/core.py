from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import Container
from xmlstruct.exceptions import TagMismatchError


class Struct(XmlElement):
    """
    A sequence of unordered xml elements.

    The elements are parsed and built according to the order they are given
    in the __init__, without validating the order against the xml element 
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
        for child in self.children:
            obj[self.tag].update(child._parse(element.find(child.tag)))
        return obj


class OrderedStruct(XmlElement):
    """
    A sequence of ordered xml elements.

    The elements are parsed and built according to the order they are given
    in the __init__, with validating the order against the xml element
    """

    def __init__(self, tag, attrib, *children):
        XmlElement.__init__(self, tag, attrib)
        self.children = children

    def _build(self, obj):
        element = ElementTree.Element(self.tag, self.attrib)
        for index, child in enumerate(self.children):
            if child.tag != obj[self.tag][index][0]:
                raise TagMismatchError()
            sub_obj = Container({child.tag: obj[self.tag][index][1]})
            element.append(child._build(sub_obj))
        return element

    def _parse(self, element):
        obj = Container()
        obj[self.tag] = Container()
        for child, subelement in zip(self.children, list(element)):
            if child.tag != subelement.tag:
                raise TagMismatchError()
            obj[self.tag].update(child._parse(subelement))
        return obj
