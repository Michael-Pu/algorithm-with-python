"""
In mathematics, a (real) interval is a set of real
 numbers with the property that any number that lies
 between two numbers in the set is also included in the set.
"""

class Interval:
    """
    A set of real numbers with methods to determine if other
     numbers are included in the set.
    Includes related methods to merge and print interval sets.
    """
    def __init__(self, start=0, end=0):
        self.start = start
        self.end = end

    def __repr__(self):
        return "Interval ({}, {})".format(self.start, self.end)

    def __iter__(self):
        return iter(range(self.start, self.end))

    def __getitem__(self, index):
        if index < 0:
            return self.end + index
        return self.start + index

    def __len__(self):
        return self.end - self.start

    def __contains__(self, item):
        if self.start <= item <= self.end:
            return True
        return False

    def __eq__(self, other):
        if self.start == other.start and self.end == other.end:
            return True
        return False

    def as_list(self):
        """ Return interval as list. """
        return list(self)

    @staticmethod
    def merge(intervals):
        """ Merge two intervals into one. """
        out = []
        for i in sorted(intervals, key=lambda i: i.start):
            if out and i.start <= out[-1].end:
                out[-1].end = max(out[-1].end, i.end)
            else:
                out += i,
        return out

    @staticmethod
    def print_intervals(intervals):
        """ Print out the intervals. """
        res = []
        for i in intervals:
            res.append(repr(i))
        print("".join(res))

def merge_intervals(intervals):
    """ Merge intervals in the form of a list. """
    if intervals is None:
        return None
    intervals.sort(key=lambda i: i[0])
    out = [intervals.pop(0)]
    for i in intervals:
        if out[-1][-1] >= i[0]:
            print(out[-1][-1],i[0])
            # out[-1][-1] = max(out[-1][-1], i[-1])
        else:
            out.append(i)
    return out

if __name__ == '__main__':
    intervals = Interval(3,7)
    print("intervals.start:", intervals.start)
    print("intervals.end:", intervals.end)
    print("intervals.__repr__():", intervals.__repr__())
    print("intervals.__iter__():", intervals.__iter__())
    print(">>>: ", end='')
    for i in intervals.__iter__():
        print(i, end=' ')
    print()
    print("intervals.__getitem__(2):", intervals.__getitem__(2))
    print("intervals.__len__():", intervals.__len__())
    print("intervals.__contains__(2):", intervals.__contains__(2))
    print("intervals.__contains__(4):", intervals.__contains__(4))
    intervals1 = Interval(3,7)
    print("intervals.__eq__(intervals1):", intervals.__eq__(intervals1))
    print("intervals.as_list():", intervals.as_list())
    intervals2 = Interval(1,2)
    interval_s = []
    interval_s.append(intervals1)
    interval_s.append(intervals2)
    print("interval_s:", interval_s)
    print("intervals.merge:", intervals.merge(interval_s))
    print("intervals1.print_intervals(intervals2): ", end='')
    intervals1.print_intervals(intervals2)
    print("merge_intervals(intervals3):", merge_intervals(interval_s))
