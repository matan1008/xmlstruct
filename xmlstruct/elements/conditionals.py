from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement


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


class Switch(XmlElement):
    """
    A conditional branch element. Switch will choose the right element according
    to a the value of keyfunc (which can be function or value).
    If default is specified, lack of match between keyfunc and cases will
    cause choosing default. If default is not specified, the result will be raising
    an Exception
    """

    def __init__(self, tag, keyfunc, cases, default=None, **kwargs):
        XmlElement.__init__(self, tag, kwargs.get("attrib"))
        self.keyfunc = keyfunc
        self.cases = cases
        self.default = default
