import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    new_array += 20
    print(new_array)


my_arr = [1,2,3,4,5,6,7,8,1,2,3,4]
make_array(my_arr)
