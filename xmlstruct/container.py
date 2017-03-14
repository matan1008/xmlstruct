from collections import OrderedDict

class Container(OrderedDict):
    """
    Generic data holder.

    The Container may be used for both building and parsing
    """
    def __init__(self, *args, **kwds):
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
