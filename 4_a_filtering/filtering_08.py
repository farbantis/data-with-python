from filtering import industry_migration


def filter_industry_income(df):
    df = df[(df['industry_name'] == 'Computer Software') & (df['wb_income'] == 'Low income')]
    return df


filtered_df = filter_industry_income(industry_migration)
actual1 = filtered_df.index[0]
expected1 = 3699
actual2 = len(filtered_df)
expected2 = 1

if actual1 == expected1 and actual2 == expected2:
  print("Test passed!\nExpected: {} & {}\nActual: {} & {}".format(expected1, expected2, actual1, actual2))
else:
  print("Test failed!\nExpected: {} & {}\nActual: {} & {}".format(expected1, expected2, actual1, actual2))
