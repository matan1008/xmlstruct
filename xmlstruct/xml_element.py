# coding=utf-8
from abc import abstractmethod, ABCMeta
from xml.etree import ElementTree


class XmlElement(object):
    r"""
    The most generic object possible.

    The object represents a xml element - it has a tag and attributes

    This object is an abstract object and must be inherited almost everywhere
    """
    __metaclass__ = ABCMeta

    def __init__(self, tag, attrib=None):
        self.tag = tag
        self.attrib = attrib if attrib is not None else {}

    def parse(self, data):
        """
        Parse data according the _parse function

        :param data: raw xml string
        """
        element = ElementTree.fromstring(data)
        return self._parse(element)

    def build(self, obj):
        """
        Build xml according the _build function

        :param obj: any object that has the needed attributes
            for the building process (preferably Container).
        """
        element = self._build(obj)
        return ElementTree.tostring(element)

    @abstractmethod
    def _build(self, obj):
        """
        To be overridden

        The function returns a xml.etree.ElementTree.Element object
        """
        raise NotImplementedError()

    @abstractmethod
    def _parse(self, element):
        """
        To be overridden

        The function receives a xml.etree.ElementTree.Element object as element
        """
        raise NotImplementedError()

    def get_tag(self, parent):
        """
        Used in order to get tag.
        Some elements may change their tag according to the building obj or
        parsing element so this function is needed
        """
        return self.tag
