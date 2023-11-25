from filtering import country_migration


def filter_two_net(df):
    result = df[(df['net_per_10K_2015'] > 50) & (df['net_per_10K_2016'] > 50)]
    return result['net_per_10K_2015'].count()


actual = filter_two_net(country_migration)
expected = 3

if actual == expected:
  print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
  print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))
