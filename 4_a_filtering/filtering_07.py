from filtering import industry_migration


def filter_industry(df):
    df = df[(df['isic_section_index'].str.lower() == 'm') & (df['industry_name'] == 'Biotechnology')]
    return df.shape[0]


actual = filter_industry(industry_migration)
expected = 32

if actual == expected:
  print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
  print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))
