import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    for part in new_array:
        print(part)


my_arr = [[1,2,3],[4,5,6],[7,8,9]]
make_array(my_arr)
