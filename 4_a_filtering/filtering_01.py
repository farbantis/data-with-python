from filtering import skill_migration


def filter_income(df):
    df = df[df['wb_income'] == 'High income']
    return len(df)


actual = filter_income(skill_migration)
expected = 8904

if actual == expected:
    print("Test passed!\nExpected: {}\nActual: {}".format(expected, actual))
else:
    print("Test failed!\nExpected: {}\nActual: {}".format(expected, actual))

