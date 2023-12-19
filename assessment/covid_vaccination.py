import numpy as np
import pandas as pd



def challenge_1(link):
    """
    task 2. -> df.info() or df.isnull().sum()
    shows us that the following columns missing data: total_vaccinations, people_vaccinated,
    people_fully_vaccinated, daily_vaccinations_raw, daily_vaccinations, total_vaccinations_per_hundred,
     people_vaccinated_per_hundred, people_fully_vaccinated_per_hundred, daily_vaccinations_per_million
    """
    print('challenge 1')
    # task 1 - read data
    df = pd.read_excel(link, sheet_name='by_country')
    df1 = df
    # task 2 - find columns with empty data
    empty_columns = df.isnull().sum()
    print('following columns have the indicated amount of empty rows:')
    print(empty_columns)
    # task 3 - remove all rows with missing data in the total_vaccination column. need reset the index.
    # alternative option - df = df.dropna(subset=['total_vaccinations'])
    df.dropna(subset=['total_vaccinations'], inplace=True)
    df = df.reset_index(drop=True)
    print('task 3')
    print(df)

    # task 4. Find the median vaccinations per hundred
    # There is no column vaccinations_per_hundred, assume  it is total_vaccinations_per_hundred
    # median can be calculated with existing zeroes or without them -> remove zeroes
    median_vac_per_100 = df1.dropna(subset=['total_vaccinations_per_hundred'])
    median_vac_per_100_2 = median_vac_per_100[median_vac_per_100['total_vaccinations_per_hundred'] > 0]['total_vaccinations_per_hundred'].median()
    print(f'task 4, median vaccination per 100 without 0s {median_vac_per_100_2}')
    # task 5 - display the mean people vaccinated per hundred for each country in descending order
    # need to remove blanks in the columns people_vaccinated_per_hundred
    mean_people_vac_dsc = df.dropna(subset=['people_vaccinated_per_hundred'])
    # mean_people_vac_dsc = mean_people_vac_dsc[mean_people_vac_dsc['people_vaccinated_per_hundred'] > 0]
    mean_people_vac_dsc = mean_people_vac_dsc.groupby("country")['people_vaccinated_per_hundred'].mean()
    mean_people_vac_dsc = mean_people_vac_dsc.sort_values(ascending=False).reset_index(name='mean_value')
    print('task 5, mean in descending orders')
    print(mean_people_vac_dsc)
    # find the range
    range_of_vacc = df['total_vaccinations'].max() - df['total_vaccinations'].min()
    print(f'task 6, range (max - min of total_vaccinations) is {range_of_vacc}')


def challenge_2(link):
    """need to clean date removing empty rows first"""
    print('challenge 2')
    df = pd.read_excel(link, sheet_name='by_country')
    df1 = df
    # 1 Find the median daily vaccinations per million
    df = df.dropna(subset=['daily_vaccinations_per_million'])
    median_daily_vaccination = df['daily_vaccinations_per_million'].median()
    print(f'median daily vaccinations: {median_daily_vaccination}')
    # 2 normalise daily vaccinations per million, values >= to median = 1 and values < than median = 0
    df1['daily_vaccinations_per_million'] = [1 if num >= median_daily_vaccination else 0 for num in df1['daily_vaccinations_per_million']]
    print(df1['daily_vaccinations_per_million'].describe())


def challenge_3(link):
    print('challenge 3')
    df = pd.read_excel(link, sheet_name='by_country')
    # task 1. Find the minimum total vaccinations for the United Kingdom
    uk_vaccinations = df[df['country'] == 'United Kingdom']
    min_total_vaccinations = uk_vaccinations['total_vaccinations'].min()
    print(f'min UK vaccination: {min_total_vaccinations}')
    # task 2 Save this value in a variable rounded down to an integer
    min_total_vacc_rnd_1 = min_total_vaccinations.astype(np.int64)
    min_total_vacc_rnd_2 = int(min_total_vaccinations)
    print(f'min UK vaccination: {min_total_vacc_rnd_1} or {min_total_vacc_rnd_2}')
    # task 3 - normalise total_vaccinations column values < the UK's min are 0 and values >= to the UK's min are 1
    df['total_vaccinations'] = [1 if num >= min_total_vaccinations else 0 for num in df['total_vaccinations']]
    # df.loc[df['total_vaccinations'] > min_total_vaccinations, 'total_vaccinations'] = 1
    # df.loc[df['total_vaccinations'] <= min_total_vaccinations, 'total_vaccinations'] = 0
    print(df['total_vaccinations'])
    # task 4. Display the countries for which total vaccinated is at the same rate or more than the UK
    uk_max_vacc = df[df['country'] == 'United Kingdom']['total_vaccinations'].max()
    more_than_uk = df[df['total_vaccinations'] >= uk_max_vacc]['country'].unique()
    print(more_than_uk)


def challenge_4(link):
    print('challenge 4')
    # 1. read data from 'by_manufacturer' sheet from Covid data
    df = pd.read_excel(link, sheet_name='by_manufacturer')
    # 2. find the sum of total vaccinations for each manufacturer
    total_per_manufacturer = df.groupby(['vaccine'])['total_vaccinations'].sum().apply(lambda x: '{:,.0f}'.format(x))
    print(f'total vaccinations per manufacturer is: {total_per_manufacturer}')
    # 3. create a new column that has the total vaccinations as a percentage of the overall sum of total vaccinations
    df['percent_of_total'] = df['total_vaccinations'] / (df['total_vaccinations'].sum()) * 100
    print(df.head())
    print(df.tail())
    # 4. find the median percentage
    median_percentage = df['percent_of_total'].median()
    print(f'median percentage is {median_percentage}')
    # 5. create a new column called 'normalised_percentages' which duplicates the percentages column
    # copy() allows to copy format
    df['normalized_percentage'] = df['percent_of_total'].copy()
    print(df)
    # 6. normalise normalised_percentages so values >= to the median percentage = 1 and any < = 0
    df['normalized_percentage'] = [1 if value >= median_percentage else 0 for value in df['normalized_percentage']]
    print(df)


link = "https://github.com/lilaceri/Working-with-data-/blob/342abab10d93c4bf23b5c55a50f189f12a137c5f/Data%20Sets%20for%20code%20divisio/Covid%20Vaccination%20Data.xlsx?raw=true"


challenge_1(link)
#challenge_2(link)
#challenge_3(link)
#challenge_4(link)
