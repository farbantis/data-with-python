import numpy as np


def generate_array():
    array = np.zeros((8, 8), dtype='int16')
    print(array)
    print()
    array[3][3] = array[3][4] = 1
    array[4, 3] = array[4, 4] = 1
    print(array)
    print()
    array[0, 0] = array[0, -1] = array[-1, 0] = array[-1, -1] = 1
    print(array)


generate_array()
