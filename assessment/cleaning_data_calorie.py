import datetime
import pandas as pd


def calorie(url):
    # column "Date" has consequtive dates, so we should add date in row 22 which is 2020/12/22, same row 26
    # column "Data" also should be adjucted to date type
    # column "Calories" contains empty sell, which we can either delete (preferably) or fill out with average calorie
    df = pd.read_csv(url)
    print(df.info())
    df.loc[22, 'Date'] = datetime.date(2020, 12, 22)
    df.loc[26, 'Date'] = datetime.date(2020, 12, 26)
    df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
    df.dropna(subset=["Calories"], inplace=True)
    return df


url_calorie = "https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/Data%20Cleaning%20Data%20Sets/dirtydata.csv"
result = calorie(url_calorie)
print(result)
