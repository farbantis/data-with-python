import pandas as pd


def get_uk_mig(excel_file):
    country = pd.read_excel(excel_file, sheet_name='Country Migration')
    country = country[country['target_country_code'] == 'gb']
    return country


excel_file = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'
actual = len(get_uk_mig(excel_file))
expected = 122

if actual == expected:
  print("Test passed", actual)
else:
  print("Test failed expected", expected, "got", actual)
