from collections import OrderedDict


class Container(OrderedDict):
    """
    Generic data holder.
    Used for functional relations, meaning that for each key there is one value.
    The Container may be used for both building and parsing.
    """

    def __init__(self, *args, **kwds):
        self.xml_attrib = kwds.pop("xml_attrib", {})
        OrderedDict.__init__(self, *args, **kwds)
        # OrderedDict uses __setattr__ in his __init__, overriding it before
        # here calls to _OrderedDict___root, thus raising AttributeError
        self.__delattr__ = OrderedDict.__delitem__
        self.__setattr__ = OrderedDict.__setitem__

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)


class OrderedPairContainer(object):
    """
    Data holder for ordered structs that might have more than one
    value with the same key, when the order matters.
    Used for ordered pairs.
    The Container may be used for both building and parsing.
    """

    def __init__(self, *args, **kwds):
        self.xml_attrib = kwds.pop("xml_attrib", {})
        self.keys, self.values = zip(*args)

    def __len__(self):
        return len(self.keys)

    def __getitem__(self, key):
        return self.keys[key], self.values[key]

    def __setitem__(self, key, value):
        if isinstance(value, dict):
            self.keys[key], self.values[key] = value.items()[0]
        else:
            self.keys[key], self.values[key] = value

    def __delitem__(self, key):
        del self.keys[key]
        del self.values[key]

    def __iter__(self):
        return zip(self.keys, self.values).__iter__()

    def __eq__(self, other):
        return self.keys == other.keys and self.values == other.values


class ListContainer(list):
    """
    Generic data holder.
    Used for lists
    """

    def __init__(self, *args, **kwds):
        self.xml_attrib = kwds.pop("xml_attrib", {})
        list.__init__(self, list(args))


class ValueContainer(object):
    def __init__(self, value, **kwds):
        self.xml_attrib = kwds.pop("xml_attrib", {})
        self.value = value

    def __eq__(self, other):
        return self.value == other.value and self.xml_attrib == other.xml_attrib
