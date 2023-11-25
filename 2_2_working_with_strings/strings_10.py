import pandas as pd


def get_married(df):
    df = pd.read_csv(df)
    just_married = df[(df['Sex'] == 'female') & (df['Name'].str.contains('Mrs'))]
    # just_married.columns.get_loc('Name') = 3
    for index, name in enumerate(just_married['Name']):
        just_married.iloc[index, 3] = name[0:name.index(',')]
    return just_married



titanic = 'https://raw.githubusercontent.com/pandas-dev/pandas/master/doc/data/titanic.csv'
test_df = get_married(titanic)
actual_len = len(test_df)
expected_len = 129
actual_name = test_df['Name'].iloc[0]
expected_name = 'Cumings'

if actual_len == expected_len and actual_name == expected_name:
  print("Test passed, ", actual_len, actual_name)
else:
  print("Test failed expected ", expected_len, expected_name, "got", actual_len, actual_name)
