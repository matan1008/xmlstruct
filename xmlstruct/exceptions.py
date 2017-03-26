# coding=utf-8
class XmlstructError(Exception):
    """General xmlstruct error"""
    pass


class FormatError(XmlstructError):
    """ Error for formatting problems """

    def __init__(self, data, format_type):
        XmlstructError.__init__(self)
        self.data = data
        self.format_type = format_type

    def __str__(self):
        return ": %s is can not be formatted as %s" % (str(self.data), str(self.format_type))


class RangeError(XmlstructError):
    """Error for any range issue"""

    def __init__(self, min_size, max_size, real_size):
        XmlstructError.__init__(self)
        self.min_size = min_size
        self.max_size = max_size
        self.real_size = real_size

    def __str__(self):
        return ": expected from %d to %d elements, found %d" % (self.min_size, self.max_size, self.real_size)


class TagMismatchError(XmlstructError):
    """ Error for when subobject or subelement doesn't match child"""

    def __init__(self, struct_tag, real_tag):
        XmlstructError.__init__(self)
        self.struct_tag = struct_tag
        self.real_tag = real_tag

    def __str__(self):
        return ": tag %s doesn't match expected %s" % (self.real_tag, self.struct_tag)


class SwitchNoMatchError(XmlstructError):
    """ Error for when a switch can't find a match in cases"""

    def __init__(self):
        XmlstructError.__init__(self)

    def __str__(self):
        return ": match not found in cases"


class SwitchSeveralMatchError(XmlstructError):
    """ Error for when a switch finds too many matches"""

    def __init__(self):
        XmlstructError.__init__(self)

    def __str__(self):
        return ": several matches found in switch"
