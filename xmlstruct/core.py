from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import Container, OrderedPairContainer
from xmlstruct.exceptions import TagMismatchError


class Struct(XmlElement):
    """
    A sequence of unordered xml elements.

    The elements are parsed and built according to the order they are given
    in the __init__, without validating the order against the xml element 
    """

    def __init__(self, tag, *children, **kwargs):
        XmlElement.__init__(self, tag, kwargs.get("attrib"))
        self.children = children

    def _build(self, obj):
        if not isinstance(obj, Container):
            obj = Container(obj)
        attributes = self.attrib.copy()
        attributes.update(obj.xml_attrib)
        element = ElementTree.Element(self.tag, attributes)
        for child in self.children:
            element.append(child._build(obj[child.tag]))
        return element

    def _parse(self, element):
        obj = Container(xml_attrib=element.attrib)
        for child in self.children:
            obj.update({child.tag: child._parse(element.find(child.tag))})
        return obj


class OrderedStruct(XmlElement):
    """
    A sequence of ordered xml elements.

    The elements are parsed and built according to the order they are given
    in the __init__, with validating the order against the xml element
    """

    def __init__(self, tag, *children):
        XmlElement.__init__(self, tag)
        self.children = children

    def _build(self, obj):
        if not isinstance(obj, OrderedPairContainer):
            obj = OrderedPairContainer(obj)
        element = ElementTree.Element(self.tag, obj.xml_attrib)
        for index, child in enumerate(self.children):
            if child.tag != obj[index][0]:
                raise TagMismatchError(child.tag, obj[index][0])
            element.append(child._build(obj[index][1]))
        return element

    def _parse(self, element):
        parsed_elements = []
        for child, subelement in zip(self.children, list(element)):
            if child.tag != subelement.tag:
                raise TagMismatchError(child.tag, subelement.tag)
            parsed_elements.append((child.tag, child._parse(subelement)))
        return OrderedPairContainer(*parsed_elements, xml_attrib=element.attrib)
