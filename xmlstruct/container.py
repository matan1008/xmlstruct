from collections import OrderedDict

class Container(OrderedDict):
    """
    Generic data holder.

    The Container may be used for both building and parsing
    """

    def __getattr__(self, name):
        try:
            return self[name]
        except KeyError:
            raise AttributeError(name)

    __delattr__ = OrderedDict.__delitem__
    __setattr__ = OrderedDict.__setitem__
