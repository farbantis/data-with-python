import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    return new_array


my_arr = [3, 6, 2, 5, 8, 6]
result = make_array(my_arr)
print(result)


