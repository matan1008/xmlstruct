from abc import abstractmethod, ABCMeta
from xml.etree import ElementTree

class XmlElement(object):
    r"""
    The most generic object possible.

    The object represents a xml element - it has a tag and attributes

    This object is an abstract object and must be inherited almost everywhere
    """
    __metaclass__ = ABCMeta

    def __init__(self, tag, attrib):
        self.tag = tag
        self.attrib = attrib

    def parse(self, data):
        """
        Parse data according the _parse function

        This function expects a string as a data parameter
        """
        element = ElementTree.fromstring(data)
        return self._parse(element)

    def build(self, obj):
        """
        Build xml according the _build function

        This function expects any object that has the needed attributes
        for the building process (preferebly Container).
        """
        element = self._build(obj)
        return ElementTree.tostring(element)

    @abstractmethod
    def _build(self, obj):
        """
        To be overrided

        The function returns a xml.etree.ElementTree.Element object
        """
        raise NotImplementedError()

    @abstractmethod
    def _parse(self, element):
        """
        To be overrided

        The function receives a xml.etree.ElementTree.Element object as element
        """
        raise NotImplementedError()
