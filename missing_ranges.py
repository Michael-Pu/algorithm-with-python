"""
Find missing ranges between low and high in the given array.
Ex) [3, 5] lo=1 hi=10 => answer: [(1, 2), (4, 4), (6, 10)]
"""

def missing_ranges(arr, lo, hi):
    res = []
    start = lo
    for n in arr:
        if n == start:
            start += 1
        elif n > start:
            if n-1 == start:
                res.append([start])
            else:
                res.append([start, n-1])
            start = n + 1
        print("---", res)
    if start < hi:                 # after done iterating thru array,
        res.append([start, hi])     # append remainder to list
    print("---", res)
    return res

if __name__ == '__main__':
    arr = [3,5]
    lo = 1
    hi = 10
    out = missing_ranges(arr, lo, hi)
    print(out)