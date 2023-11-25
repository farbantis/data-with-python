import pandas as pd


def migration(excel_file):
    country = pd.read_excel(excel_file, sheet_name='Country Migration')
    country = len(country['target_country_code'].unique())  # returns np array
    print(country)
    return country


excel_file = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'
actual = migration(excel_file)
expected = 140

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed expected", expected, "got", actual)
