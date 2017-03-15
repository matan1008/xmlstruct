
class RangeError(Exception):
    "Error for any range issue"
    def __init__(self, min_size, max_size, real_size):
        Exception.__init__(self)
        self.min_size = min_size
        self.max_size = max_size
        self.real_size = real_size

    def __str__(self):
        print ": expected from %d to %d elements, found %d" % (self.min_size, self.max_size, self.real_size)
