from filtering import country_migration


def filter_migrations(df, region):
    df = df[(df['target_country_wb_income'].isin(['Upper Middle Income', 'High Income']))
            & (df['base_country_wb_region'] == region)]
    return df.shape[0]

# run test to see if you are getting the correct result
actual = filter_migrations(country_migration, "Middle East & North Africa")
expected = 432
if actual == expected:
    print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
    print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))

