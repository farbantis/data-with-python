import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import linregress


def get_array_of_years(start, finish, rate):
    """returns array of years based on start, finish, rate"""
    return np.arange(start, finish, rate)


def get_data_for_linear_trend(x, y):
    """as this is called several times it is better to make it as a separate function"""
    slope, intercept, r_value, p_value, std_err = linregress(x, y)
    return slope, intercept


def sea_project_1_2(link):
    """
    pd.info shows us, that there are only 21 row with date in 'NOAA Adjusted Sea Level' column
    while others are empty. it means that this data seems not enough for analysis as they represent
    21/134*100% = 16% of all data. Perhaps better to either use other column or to calculate the missing
    data based on other columns.
    """
    print('task 1 & 2')
    df = pd.read_csv(link)
    print(df.info())
    print(df['CSIRO Adjusted Sea Level'].describe())
    print(df)
    # 2 scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', title='Sea level by time span')
    plt.show()
    return df


def sea_project_3(df):
    """
    as the task is to make a diagram based on NOAA Adjusted Sea Level we should delete all empty cells
    """
    print('task 3')
    df_noaa_cleaned = df.dropna(subset=['NOAA Adjusted Sea Level'])
    print(df_noaa_cleaned.describe())
    print(df_noaa_cleaned)
    diagram = df_noaa_cleaned.plot.scatter(x='Year', y='NOAA Adjusted Sea Level', title='NOAA by timespan')
    diagram.xaxis.set_major_locator(plt.MultipleLocator(base=1))
    plt.show()
    return df_noaa_cleaned


def sea_project_4(df_noaa_cleaned):
    """
    task 4 plot line of best fit for CSIRO
    scipy.stats.linregress(x, y=None, alternative='two-sided')
    the equasion of the linear trend is y=ax+b
    where x is period (here years_min_to_2050), a is slope (ratio of slope), b (free trend value)
    """
    print('task 4')
    slope, intercept = get_data_for_linear_trend(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
    years = get_array_of_years(df_noaa_cleaned['Year'].min(), 2051, 1)
    forecast = slope * years + intercept
    plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'], label='Data')
    plt.plot(years, forecast, color='red', label='Linear Trend')
    plt.title('Linear Trend of CSIRO Adjusted Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.legend()
    plt.show()


def sea_project_5(df_noaa_cleaned):
    # 5 plot line of best fit for NOAA
    print('task 5')
    slope, intercept = get_data_for_linear_trend(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
    years = get_array_of_years(df_noaa_cleaned['Year'].min(), 2031, 1)
    forecast_noaa = slope * years + intercept
    plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'], label='Data')
    plt.plot(years, forecast_noaa, color='red', label='Linear Trend')
    plt.title('Linear Trend of CSIRO Adjusted Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.legend()
    plt.show()


def sea_project_6(df_noaa_cleaned):
    # 6 shorter range (starting 2000)
    # get data for the year 2000 and later
    print('task 6')
    df_from_year_2000 = df_noaa_cleaned[df_noaa_cleaned['Year'] >= 2000]
    slope, intercept = get_data_for_linear_trend(df_from_year_2000['Year'], df_from_year_2000['CSIRO Adjusted Sea Level'])
    years = get_array_of_years(2000, 2051, 1)
    sea_levels_noaa = slope * years + intercept
    plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
    plt.plot(years, sea_levels_noaa, color='red')
    plt.title('Linear Trend of CSIRO Adjusted Sea Level')
    plt.xlabel('Year')
    plt.ylabel('CSIRO Adjusted Sea Level')
    plt.legend()
    plt.show()


link = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'

df = sea_project_1_2(link)
df_noaa_cleaned = sea_project_3(df)
sea_project_4(df_noaa_cleaned)
sea_project_5(df_noaa_cleaned)
