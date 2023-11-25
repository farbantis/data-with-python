import pandas as pd


def get_middle(titanic):
    start = round(titanic.shape[0] / 2) - 10
    result = titanic.iloc[start: start+19]
    return result


titanic = pd.read_csv('https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv')
actual = get_middle(titanic).index[0]
expected = 436

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed expected index of", expected, "got", actual)
