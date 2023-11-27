import pandas as pd


def clean_country_mig(df):
    df = pd.read_excel(df, sheet_name='Country Migration')
    columns = df.columns.tolist()
    for column in columns:
        if 'country_codes' in column:
            df[column] = df[column].str.upper()
        if 'lat' in column or 'long' in column:
            del df[column]
        if 'net_per_10K_' in column:
            df.rename(columns={column: column.replace('net_per_10K_', '')}, inplace=True)
    df = df[
        (df['base_country_wb_region'].str.contains('Africa', case=False)) &
        (df['target_country_wb_region'].str.contains('Asia, case=False'))
        ]
    return df

link = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'

test_df = clean_country_mig(link)
actual_col_len = len(test_df.columns)
expected = 13

if actual_col_len == expected and (test_df['base_country_code'].str.islower().any() == False) and (
        test_df.columns.str.contains('net_per_10K_').any() == False):
    print("Test passed")
else:
    print("Test failed")
