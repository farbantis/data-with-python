import datetime
import pandas as pd


def calorie(url):
    """
    We also see, that colum Date in not Datetime object, moreover it misses 2 values. As the dates are
    consecutive, we can add missing value, without deleting rows. As dates are strings here, we can
    change their format to Datetime.
    Guess rows with missing values in calories column should be deleted, as the value is not knows,
    still maybe there is correlation between Pulse, Maxpulse and Calories
    """
    df = pd.read_csv(url)
    print(df.info())
    print(df)
    df.loc[22, 'Date'] = datetime.date(2020, 12, 22)
    df.loc[26, 'Date'] = datetime.date(2020, 12, 26)
    df['Date'] = pd.to_datetime(df['Date'])
    df.dropna(subset=["Calories"], inplace=True)
    print(df.info())
    return df


url_calorie = "https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/Data%20Cleaning%20Data%20Sets/dirtydata.csv"
result = calorie(url_calorie)
print(result)
