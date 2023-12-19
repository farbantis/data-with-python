import pandas as pd


def elections(url):
    """
    from df.info() we can learn that national_voteshare_3rd_lo column is totally empty, we dont need it
    3 columns contain inconsistent data: national_turnout, national_turnout_hi, national_turnout_lo
    timestamp is not a Datetime object
    df = df[df['national_turnout'].isna()] shows that all 3 columns go with blank data in same rows - we
    can delete those rows if they take part in calculations
    """
    df = pd.read_csv(url)
    print(df.info())
    # df.columns = df.columns.str.strip()
    df.drop('national_voteshare_3rd_lo', axis=1, inplace=True)
    df['timestamp'] = pd.to_datetime(df['timestamp'], format='%d/%m/%Y %H:%M')
    print(df.info())
    # pd.set_option('display.max_columns', None)
    # df.dropna(subset=['national_turnout', 'national_turnout_hi', 'national_turnout_lo'], inplace=True)
    return df


url = "https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/Data%20Cleaning%20Data%20Sets/presDirty.csv"
result = elections(url)
print(result.head())
