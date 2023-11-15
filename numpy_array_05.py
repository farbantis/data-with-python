import numpy as np


def make_array(numlist):
    new_array = np.array(numlist)
    return new_array.shape


my_arr = [3,7,56]
result = make_array(my_arr)
message = f'layers: {result[0]}, ' \
          f'rows: {result[1] if len(result)>1 else 0}, ' \
          f'columns: {result[2] if len(result)>2 else 0}'

print(message)
