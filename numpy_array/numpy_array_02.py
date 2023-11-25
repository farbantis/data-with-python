import numpy as np


def make_array(numlist):
    new_array = np.array(numlist, np.int16)
    return new_array


my_arr = [31112, 32321, 24567], [456, 324, 789]
result = make_array(my_arr)
print(result)
