import pandas as pd


def check_null(df):
    df = pd.read_csv(df)
    check = df.isna().any().any()
    print(f'total rows {len(df)}, min filled rows {min(df.count())}')
    print(check)
    return check


housing = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'
actual = check_null(housing)
expected = True

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed","Should have got", expected, "got", actual)

