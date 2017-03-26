# coding=utf-8
from xml.etree import ElementTree
from xmlstruct.xml_element import XmlElement
from xmlstruct.container import ValueContainer
from xmlstruct.exceptions import SwitchNoMatchError, SwitchSeveralMatchError, XmlstructError


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

    def __init__(self, keyfunc, cases, default=None, **kwargs):
        XmlElement.__init__(self, None, kwargs.get("attrib"))
        self.keyfunc = keyfunc
        self.cases = cases
        self.default = default

    def get_key(self, obj):
        """
        For each use of keyfunc
        :param obj: param for keyfunc
        """
        return self.keyfunc(obj) if callable(self.keyfunc) else self.keyfunc

    def all_cases(self):
        if self.default is None:
            return self.cases.values()
        else:
            return self.cases.values() + [self.default]

    def get_tag(self, parent):
        case_tag = []
        for case in self.all_cases():
            if type(parent) == ElementTree.Element:
                # for parsing
                value_in_parent = parent.find(case.get_tag(parent))
            else:
                value_in_parent = parent.get(case.get_tag(parent))
            if value_in_parent is not None:
                case_tag.append(case.get_tag(parent))
        if len(case_tag) == 0:
            raise SwitchNoMatchError()
        elif len(case_tag) == 1:
            return case_tag[0]
        else:
            raise SwitchSeveralMatchError()

    def _build(self, obj):
        case = self.cases.get(self.get_key(obj), self.default)
        if case is not None:
            return case._build(obj)
        else:
            raise SwitchNoMatchError()

    def _parse(self, element):
        possible_objs = []
        for case in self.all_cases():
            try:
                obj = case._parse(element)
                if type(obj) == ValueContainer:
                    obj = obj.value
                if self.cases.get(self.get_key(obj), self.default) == case:
                    if ElementTree.tostring(element) == case.build(obj):
                        possible_objs.append(obj)
            except XmlstructError:
                continue
        if len(possible_objs) == 0:
            raise SwitchNoMatchError()
        elif len(possible_objs) == 1:
            return possible_objs[0]
        else:
            raise SwitchSeveralMatchError()
