"""
Given an array of integers, return indices of the two numbers
such that they add up to a specific target.

You may assume that each input would have exactly one solution,
and you may not use the same element twice.

Example:
    Given nums = [2, 7, 11, 15], target = 9,

    Because nums[0] + nums[1] = 2 + 7 = 9,
    return (0, 1)
"""

def two_sum(array, target):
    dic = {}
    out = []
    for i, num in enumerate(array):
        print("---", i, num, dic)
        if num in dic:
            # return dic[num], i
            out.append((dic[num],i))
        else:
            dic[target - num] = i
    return out

if __name__ == '__main__':
    array = [2,7,11,15,16]
    target = 18
    print(two_sum(array, target))