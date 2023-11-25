import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    # for i in new_array:
    #     for j in i:
    #         print(j)
    [print(j) for i in new_array for j in i]
    

my_arr = [[[1,2],[3,4]],[[5,6],[7,8]]]
make_array(my_arr)

