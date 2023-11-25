import pandas as pd


def drop_duplicates(df):
    df = pd.read_csv(df)
    df = df['area'].drop_duplicates()
    return df


housing = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'
actual = drop_duplicates(housing).index[0]
expected = 0

if actual == expected and len(drop_duplicates(housing)) == 51:
    print("Test passed", actual)
else:
    print("Test failed", "Should have got", expected, "got", actual, "and length of series should have been 51 but was",
          len(drop_duplicates(housing)))
