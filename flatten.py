"""
Implement Flatten Arrays.
Given an array that may contain nested arrays,
produce a single resultant array.
"""
from collections.abc import Iterable

# return list
def flatten(input_arr, output_arr=None):
    if output_arr is None:
        output_arr = []
    for ele in input_arr:
        if isinstance(ele, Iterable):
            flatten(ele, output_arr)    #tail-recursion
        else:
            output_arr.append(ele)      #produce the result
    return output_arr

# returns iterator
def flatten_iter(iterable):
    """
    Takes as input multi dimensional iterable and
    returns generator which produces one dimensional output.
    """
    for element in iterable:
        if isinstance(element, Iterable):
            yield from flatten_iter(element)    
        else:
            yield element

if __name__ == '__main__':
    _input_ = list(eval(input()))
    output = flatten(_input_)
    print("flatten:", type(output), ":", output)
    output = flatten_iter(_input_)
    # for o in output:
    #     print(o)
    print("flatten_iter:", type(output), ":", output)