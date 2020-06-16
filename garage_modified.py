
def garage(initial, final):
    initial = initial[::]
    seq = []
    steps = 0
    while (initial != final):
        for i in range(len(initial)):
            zero = initial.index(0)
            # print (zero, end=":")
            if initial[i] != final[i]:
                initial[i], initial[zero] = initial[zero], initial[i]
                # print (initial)
                seq.append(initial[::])
                steps += 1
                print (seq)
                print ("-"*15)
    return steps, seq

import time

if __name__ == '__main__':
    initial = [1,2,3,0,4]
    final = [0,3,2,1,4]

    bt = time.time()
    garage(initial, final)
    et = time.time()

    print ("running time:", str(et-bt))