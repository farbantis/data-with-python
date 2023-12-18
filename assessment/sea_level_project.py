import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import linregress


def sea_project(link):
    # there are only 21 row with date in 'NOAA Adjusted Sea Level' column

    df = pd.read_csv(link)
    print(df.info())
    print(df)
    # 2 scatter plot
    df.plot.scatter(x='Year', y='CSIRO Adjusted Sea Level', title='Sea level by time span')
    plt.show()
    # 3 cleaning df, producing new df
    df_noaa_cleaned = df.dropna(subset=['NOAA Adjusted Sea Level'])
    print(df_noaa_cleaned)
    diagram = df_noaa_cleaned.plot.scatter(x='Year', y='NOAA Adjusted Sea Level', title='NOAA by timespan')
    diagram.xaxis.set_major_locator(plt.MultipleLocator(base=1))
    plt.show()
    # 4 plot line of best fit for CSIRO
    # scipy.stats.linregress(x, y=None, alternative='two-sided')
    # x - know periods of time, y - known data
    slope, intercept, r_value, p_value, std_err = linregress(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
    # need to create array of years, from min in the cleaned df to 2050
    years_min_to_2050 = np.arange(df_noaa_cleaned['Year'].min(), 2050, 1)
    # the equasion of the linear trend is y=ax+b
    # where x is period (here years_min_to_2050), a is slope (ratio of slope), b (free trend value)
    sea_levels_forecast = slope * years_min_to_2050 + intercept
    plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'], label='Actual Data')
    plt.plot(years_min_to_2050, sea_levels_forecast, color='red', label='Line of Best Fit')
    plt.show()
    # 5 plot line of best fit for NOAA
    slope1, intercept1, r_value1, p_value1, std_err1 = linregress(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
    years_min_to_2030 = np.arange(df_noaa_cleaned['Year'].min(), 2030, 1)
    sea_levels_noaa = slope1 * years_min_to_2030 + intercept1
    plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'], label='Actual Data')
    plt.plot(years_min_to_2030, sea_levels_noaa, color='red', label='Line of Best Fit')
    plt.show()
    # 6 shorter range (starting 2000)

    # 6a add labels to the axes


link = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'
result = sea_project(link)
