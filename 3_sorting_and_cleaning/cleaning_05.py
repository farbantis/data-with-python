import pandas as pd


def filter_null(df):
    df = pd.read_csv(df)
    df = df[~df['number_of_jobs'].isna()]
    return df


housing = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'
actual = len(filter_null(housing))
expected = 931

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed expected", expected, "got", actual)
