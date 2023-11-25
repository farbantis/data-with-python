import pandas as pd


def create_new_df(link):
    df = pd.read_excel(link, sheet_name='Skill Migration')
    df['skill_group_category'] = df['skill_group_category'].str.rstrip('Skills')
    df['country_code'] = df['country_code'].str.upper()
    del df['skill_group_id']
    df.drop('wb_income', axis=1, inplace=True)
    df = df[df['wb_region'].str.contains('Asia', case=False)]
    return df


link = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'
test_df = create_new_df(link)
actual_len = len(test_df)
actual_col = len(test_df.columns)
expected_len = 9969
expected_col = 10
actual_skill = test_df['skill_group_category'].iloc[0]
expected_skill = 'Tech '

if actual_len == expected_len and actual_col == expected_col and actual_skill == expected_skill:
       print("Test passed", actual_len, "x", actual_col, actual_skill)
else:
       print("Test failed, expected", expected_len, "x", expected_col, expected_skill, "got", actual_len, "x",
             actual_col, actual_skill)



