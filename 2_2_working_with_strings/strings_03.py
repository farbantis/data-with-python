import pandas as pd
import numpy as np


def get_title_areas(link):
    df = pd.read_csv(link)
    df['area'] = df['area'].str.title()
    return df['area']


link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'

actual = get_title_areas(link).iloc[0]
expected = "City Of London"

if actual == expected:
    print("Test passed", actual)
else:
    print("Test failed, expected", expected, "got", actual)
