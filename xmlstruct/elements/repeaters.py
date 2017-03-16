import sys
from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import Container
from xmlstruct.exceptions import RangeError


class Range(XmlElement):
    """
    A sequence of the same element.
    Build and parse must be between minsize and maxsize
    child is the repeated element
    """

    def __init__(self, tag, attrib, minsize, maxsize, child):
        XmlElement.__init__(self, tag, attrib)
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
        self.check_size(len(obj[self.tag]))
        element = ElementTree.Element(self.tag, self.attrib)
        for child_index in xrange(len(obj[self.tag])):
            sub_obj = Container({
                self.child.tag: obj[self.tag][child_index][self.child.tag]
            })
            element.append(self.child._build(sub_obj))
        return element

    def _parse(self, element):
        self.check_size(len(list(element)))
        obj = Container()
        obj[self.tag] = map(self.child._parse, list(element))
        return obj


class Array(Range):
    """ Range of "count" size """

    def __init__(self, tag, attrib, count, child):
        Range.__init__(self, tag, attrib, count, count, child)


class GreedyRange(Range):
    """ Range of any size """

    def __init__(self, tag, attrib, child):
        Range.__init__(self, tag, attrib, 0, sys.maxsize, child)
