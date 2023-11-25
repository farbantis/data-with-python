import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    return new_array[:3], new_array[-1]


my_arr = [1,2,3,4,5]
result = make_array(my_arr)
print(result)
