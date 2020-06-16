def josephus(int_list, skip):
    out = []
    skip = skip - 1                     # list starts with 0 index
    idx = 0
    len_list = (len(int_list))
    while len_list > 0:
        idx = (skip + idx) % len_list   # hash index to every 3rd
        out.append(int_list.pop(idx))
        len_list -= 1
    return out

if __name__ == '__main__':
    int_list = [1,2,3,4,5,6,7,8,9]
    skip = 3
    out = josephus(int_list, skip)
    print(out)