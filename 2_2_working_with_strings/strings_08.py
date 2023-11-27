import pandas as pd


def clean_skills(df):
    df = pd.read_excel(df, sheet_name='Skill Migration')
    columns = df.columns.tolist()
    df.rename(columns={column: column.replace('net_per_10K_', '') for column in columns if 'net_per_10K_' in column}, inplace=True)

    # [df.rename(columns={column: column.replace('net_per_10K_', '')}, inplace=True)
    #     for column in columns
    #     if 'net_per_10K_' in column]

    # for column in columns:
    #     if 'net_per_10K_' in column:
    #         df.rename(columns={column: column.replace('net_per_10K_', '')}, inplace=True)

    #df['skill_group_category'] = df['skill_group_category'].str.replace('Specialized', 'Specialised')
    df['skill_group_category'].replace('Specialized', 'Specialised', inplace=True, regex=True)
    return df


migration = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'
test_df = clean_skills(migration)

if (test_df['skill_group_category'].str.contains('Specialised').any() == True) and (test_df.columns.str.contains('net_per_10K_').any() == False):
  print("Test passed")
else:
  print("Test failed")
