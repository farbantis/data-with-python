import numpy as np
import pandas as pd
from scipy.stats import linregress
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt


def describing_data_1_2(link):
    # 1 - is age closely related to income?
    county_level_df = pd.read_excel(link, sheet_name='county-level')
    print(county_level_df.info())
    x = county_level_df['Age']
    y = county_level_df['Income']
    regression = linregress(x, y)
    print(regression)
    print(f'slope: {regression.slope}, intercept: {regression.intercept}, r_value: {regression.rvalue}')
    # 2. Could Population predict Income?
    x = county_level_df['Population']
    y = county_level_df['Income']
    regression = linregress(x, y)
    print(f'the r_value which shows correlations is {regression.rvalue}')
    # r-value is 0.11 which shows that the dependency is low.


def describing_data_3(link):
    """
    firstlanguage contains empty rows
    our task is to look through all columns which contains numbers and find correlation of these
    columns with 'Wellbeing'
    """
    # 3. Does Stress predict Wellbeing?
    df = pd.read_csv(link)
    print(df.info())
    columns = df.columns
    result = dict()
    for column in columns:
        if column != 'Wellbeing':
            try:
                x = pd.to_numeric(df[column])
                regression = linregress(x, df['Wellbeing'])
                if abs(regression.rvalue) > 0.5:
                    result[column] = regression.rvalue
            except ValueError:
                print()
    # best_r_value = max(result.values(), key=lambda x: abs(x))
    print(f'the good correlation is for: {result}')


def ex_4(df):
    print(df.info())
    net_migration = [column for column in df.columns if 'net_per_' in column]
    df_net_migration = df[net_migration]
    means = df_net_migration.mean()
    labels = net_migration
    plt.figure(figsize=(11, 5))
    plt.plot(labels, means)
    plt.title('Mean Net Migration Years 2015-2019')
    plt.xlabel('Year')
    plt.ylabel('Mean Net Migration per 10K')
    # plt.xticks(rotation=45)
    plt.grid()
    plt.show()
    return df_net_migration


def ex_5(df_net_migration):
    total_per_column = df_net_migration.sum()
    labels = np.arange(2015, 2020, 1)
    plt.bar(labels, total_per_column, color='yellow')
    for index, value in enumerate(total_per_column):
        plt.text(labels[index], value, str(int(value)), ha='center', va='center', color='black')
    plt.xlabel('Year')
    plt.ylabel('Total Net Migration')
    plt.title('Bar chart for yearly migration 2015-2019')
    plt.grid()
    plt.show()


url = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/Income-Data.xlsx?raw=true'
describing_data_1_2(url)

url3 = "https://github.com/lilaceri/Working-with-data-/blob/b157a2feceb7709cf82426932385706d65446270/Data%20Sets%20for%20code%20divisio/Positive_Psychology_2017.csv?raw=true"
describing_data_3(url3)

url4 = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true'
df = pd.read_excel(url4, sheet_name='Country Migration')
df_net_migrations = ex_4(df)
ex_5(df_net_migrations)

