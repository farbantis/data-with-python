import pandas as pd


def get_ham(link):
    df = pd.read_csv(link)
    df['date'] = pd.to_datetime(df['date'])
    result = df[(df['area'].str.endswith('ham')) & (df['date'].dt.year == 2000)]
    return result

link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'

actual = len(get_ham(link))
expected = 4

if actual == expected:
    print("Test passed", actual)
else:
    print("Test failed, expected", expected, "got", actual)
