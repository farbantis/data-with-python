import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    print(new_array[0][0])
    print(new_array[0:2])
    print(new_array[-2][-2:], new_array[-1][-2:])


my_arr = [[1,2,3,4],[5,6,7,8],[9,1,2,3]]
make_array(my_arr)
