import pandas as pd


def get_and(link):
    df = pd.read_csv(link)
    area = df[df['area'].str.contains(' and ')]
    return area


link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'

actual = len(get_and(link))
expected = 105

if actual == expected:
    print("Test passed", actual)
else:
    print("Test failed, expected", expected, "got", actual)
