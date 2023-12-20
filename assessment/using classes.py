import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
from scipy.stats import linregress


class Trend:
    def __init__(self, start, finish, rate, x, y):
        self.start = start
        self.finish = finish
        self.rate = rate
        self.x = x
        self.y = y

    def get_array_of_years(self):
        """returns array of years based on start, finish, rate"""
        return np.arange(self.start, self.finish, self.rate)

    def get_data_for_linear_trend(self):
        """as this is called several times it is better to make it as a separate function"""
        slope, intercept, r_value, p_value, std_err = linregress(self.x, self.y)
        return slope, intercept

    def diagram(self):
        slope, intercept = self.get_data_for_linear_trend()
        years = self.get_array_of_years()
        forecast = slope * years + intercept
        plt.scatter(self.x, self.y, label='Data')
        plt.plot(years, forecast, color='red', label='Linear Trend')
        plt.title('Linear Trend of CSIRO Adjusted Sea Level')
        plt.xlabel('Year')
        plt.ylabel('CSIRO Adjusted Sea Level')
        plt.legend()
        plt.show()


link = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'
df = pd.read_csv(link)
df_noaa_cleaned = df.dropna(subset=['NOAA Adjusted Sea Level'])

y_axis = df_noaa_cleaned['Year']
x_asix = df_noaa_cleaned['CSIRO Adjusted Sea Level']
year_start = df_noaa_cleaned['Year'].min()
year_finish = 2051
year_rate = 1
task_3 = Trend(year_start, year_finish, year_rate, x_asix, y_axis)
task_3.diagram()



# def sea_project_4(df_noaa_cleaned):
#     """
#     task 4 plot line of best fit for CSIRO
#     scipy.stats.linregress(x, y=None, alternative='two-sided')
#     the equation of the linear trend is y=ax+b
#     where x is period (here years_min_to_2050), a is slope (ratio of slope), b (free trend value)
#     """
#     print('task 4')
#     #slope, intercept = get_data_for_linear_trend(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'])
#     #years = get_array_of_years(df_noaa_cleaned['Year'].min(), 2051, 1)
#     #forecast = slope * years + intercept
#     plt.scatter(df_noaa_cleaned['Year'], df_noaa_cleaned['CSIRO Adjusted Sea Level'], label='Data')
#     plt.plot(years, forecast, color='red', label='Linear Trend')
#     plt.title('Linear Trend of CSIRO Adjusted Sea Level')
#     plt.xlabel('Year')
#     plt.ylabel('CSIRO Adjusted Sea Level')
#     plt.legend()
#     plt.show()
