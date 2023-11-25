import pandas as pd


def get_year(link):
    df = pd.read_csv(link)
    df['year'] = df['date'].str.split('-').str[0]
    return df['year']


link = 'https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/housing_in_london_yearly_variables.csv'
actual_len = len(get_year(link))
actual_value = get_year(link).iloc[0]
expected_len = 1071
expected_val = "1999"

if actual_len == expected_len and actual_value == expected_val:
  print("Test passed expected length 1071 and first value 1999 and got", actual_len, actual_value)
else:
  print("Test failed expected length 1071 and first value 1999 and got length", actual_len, "value", actual_value)

