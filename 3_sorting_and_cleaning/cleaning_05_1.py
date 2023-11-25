import pandas as pd


def drop_null(df):
    df = pd.read_csv(df)
    df = df['life_satisfaction'].dropna()
    return df

housing = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'
actual = drop_null(housing).index[0]
expected = 613

if actual == expected and len(drop_null(housing)) == 352:
    print("Test passed", actual)
else:
    print("Test failed", "Should have got", expected, "got", actual,
          "and length of series should have been 352 but was", len(drop_null(housing)))

