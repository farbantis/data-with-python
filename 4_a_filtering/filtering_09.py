from filtering import industry_migration


def filter_country(df):
    df = df[(df['country_name'].isin(['United States', 'United Kingdom'])) & (df['isic_section_index'] == 'M')]
    return df['net_per_10K_2015'].mean()


actual = round(filter_country(industry_migration), 2)
expected = 47.28

if actual == expected:
  print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
  print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))
