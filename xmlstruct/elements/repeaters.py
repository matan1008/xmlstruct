import sys
from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.exceptions import RangeError
from xmlstruct.container import ListContainer


class Range(XmlElement):
    """
    A sequence of the same element.
    Build and parse must be between minsize and maxsize
    child is the repeated element
    """

    def __init__(self, tag, minsize, maxsize, child):
        XmlElement.__init__(self, tag)
        self.minsize = minsize
        self.maxsize = maxsize
        self.child = child

    def check_size(self, size):
        """ Make sure all size is between min and max
        :param size: int
        """
        if not 0 <= self.minsize <= size <= self.maxsize <= sys.maxsize:
            raise RangeError(self.minsize, self.maxsize, size)

    def _build(self, obj):
        if not isinstance(obj, ListContainer):
            obj = ListContainer(*obj)
        self.check_size(len(obj))
        element = ElementTree.Element(self.tag, obj.xml_attrib)
        for child_index in xrange(len(obj)):
            element.append(self.child._build(obj[child_index]))
        return element

    def _parse(self, element):
        self.check_size(len(list(element)))
        values = map(self.child._parse, list(element))
        return ListContainer(*values, xml_attrib=element.attrib)


class Array(Range):
    """ Range of "count" size """

    def __init__(self, tag, count, child):
        Range.__init__(self, tag, count, count, child)


class GreedyRange(Range):
    """ Range of any size """

    def __init__(self, tag, child):
        Range.__init__(self, tag, 0, sys.maxsize, child)
