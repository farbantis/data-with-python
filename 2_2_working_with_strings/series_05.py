import pandas as pd


def get_ba(link):
    df = pd.read_csv(link)
    area = df[df['area'].str.startswith('ba')]
    return area


link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'

actual = len(get_ba(link))
expected = 42

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed, expected", expected, "got", actual)

