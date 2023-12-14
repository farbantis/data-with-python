import numpy as np
import pandas as pd

"""
1. df.info() shows us:
the obvious problem in this table is missing data. the solution can be either to
delete the rows with missing data or to fill them out with average data. Both approaches
have their pros and cons. If we remove total_vaccinations column the remaining dataset
would represent 9011/14994*100 = 60% of the original dataset.
2. dropna() 
removes blank rows based on indicated column. still keeps the rows where the value is 0 
"""


def challenge_1(df):
    print('challenge 1')
    df = df.dropna(subset=['total_vaccinations'])
    median_vaccination_per_100 = df['total_vaccinations_per_hundred'].median()
    mean_people_vac_dsc = df.dropna(subset=['people_vaccinated_per_hundred'])
    mean_people_vac_dsc = mean_people_vac_dsc.groupby("country")['people_vaccinated_per_hundred'].mean()
    mean_people_vac_dsc = mean_people_vac_dsc.sort_values(ascending=False).reset_index(name='mean_value')
    print(df.info())
    print(f'media vaccination per 100 is {median_vaccination_per_100}')
    print(mean_people_vac_dsc)


def challenge_2(df):
    print('challenge 2')
    median_daily_vaccination = df['daily_vaccinations_per_million'].median()
    print(median_daily_vaccination, 'vs 1475.0')
    print(df.describe())


def challenge_3(df):
    print('challenge 3')
    # task 1
    uk_vaccinations = df[df['country'] == 'United Kingdom']
    min_total_vaccinations = uk_vaccinations['total_vaccinations'].min()
    print(f'min UK vaccination: {min_total_vaccinations}')
    # task 2 (can be solved using python or pandas approach
    min_total_vacc_rnd_1 = min_total_vaccinations.astype(np.int64)
    min_total_vacc_rnd_2 = int(min_total_vaccinations)
    print(f'min UK vaccination: {min_total_vacc_rnd_1} or {min_total_vacc_rnd_2}')
    # task 3 - unclear what to do if country's vaccination = min UK vaccination
    df['total_vaccinations_1'] = [1 if num > min_total_vaccinations else 0 for num in df['total_vaccinations']]
    # df.loc[df['total_vaccinations'] > min_total_vaccinations, 'total_vaccinations'] = 1
    # df.loc[df['total_vaccinations'] <= min_total_vaccinations, 'total_vaccinations'] = 0
    print(df['total_vaccinations_1'])


    # task 4

def challenge_4(df):
    print('challenge 4')


link = "https://github.com/lilaceri/Working-with-data-/blob/342abab10d93c4bf23b5c55a50f189f12a137c5f/Data%20Sets%20for%20code%20divisio/Covid%20Vaccination%20Data.xlsx?raw=true"
df = pd.read_excel(link, sheet_name='by_country')

challenge_1(df)
challenge_2(df)
challenge_3(df)
challenge_4(df)
