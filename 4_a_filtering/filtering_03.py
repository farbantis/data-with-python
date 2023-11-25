from filtering import skill_migration


def filter_skill_id(df):
    df = df[(df['skill_group_id'] == 2265) & (df['net_per_10K_2019'] > -500)]
    df = df.sort_values(by='net_per_10K_2019', ascending=True)
    return df.head(5)


filtered_df = filter_skill_id(skill_migration)
actual1 = filtered_df.index[0]
expected1 = 14550
actual2 = len(filtered_df)
expected2 = 5

if actual1 == expected1 and actual2 == expected2:
    print("Test passed!\nExpected: {} & {}\nActual: {} & {}".format(expected1, expected2, actual1, actual2))
else:
    print("Test failed!\nExpected: {} & {}\nActual: {} & {}".format(expected1, expected2, actual1, actual2))
