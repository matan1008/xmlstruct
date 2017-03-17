class XmlstructError(Exception):
    """General xmlstruct error"""
    pass


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
    """ Eror for when subobject or subelement doen't match child"""

    def __init__(self, struct_tag, real_tag):
        XmlstructError.__init__(self)
        self.struct_tag = struct_tag
        self.real_tag = real_tag

    def __str__(self):
        return ": tag %s doesn't match expected %s" % (self.real_tag, self.struct_tag)
