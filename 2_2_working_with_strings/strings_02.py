import pandas as pd
import numpy as np


def get_int_year(link):
    df = pd.read_csv(link)
    df['year'] = df['date'].str.split('-').str[0].astype(np.int64)
    return df['year']


link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'

actual = get_int_year(link).dtype
expected = np.int64

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed, expected", expected, "got", actual)
