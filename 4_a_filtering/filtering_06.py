from filtering import country_migration


def filter_two_income(df):
    df = df[(df['base_country_wb_region'] == df['target_country_wb_region'])
            & (df['target_country_wb_income'].isin(['Low Income', 'Low Middle Income', 'Upper Middle Income']))]
    return df.shape[0]


actual = filter_two_income(country_migration)
expected = 15

if actual == expected:
  print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
  print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))
