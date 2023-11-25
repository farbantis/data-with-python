import numpy as np


def generate_array(start, stop, rng=None):
    array = np.arange(start, stop, rng)
    array_zero = np.zeros(12, dtype='int16')
    array_ones = np.ones(4, dtype='int16')
    array_final = np.arange(10, 101, 10)
    print(array)
    print(array_zero)
    print(array_ones)
    print(array_final)


generate_array(1, 9)

