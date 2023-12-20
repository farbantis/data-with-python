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

    @staticmethod
    def get_array_of_years(start, finish, rate):
        """returns array of years based on start, finish, rate"""
        return np.arange(start, finish, rate)

    @staticmethod
    def get_data_for_linear_trend(x, y):
        slope, intercept, r_value, p_value, std_err = linregress(x, y)
        return slope, intercept, r_value, p_value, std_err

    @staticmethod
    def get_forecast(slope, years, intercept):
        return slope * years + intercept

    def diagram(self, title='', title_x='', title_y='', grid=False):
        slope, intercept, r_value, p_value, std_err = self.get_data_for_linear_trend(self.x, self.y)
        years = self.get_array_of_years(self.start, self.finish, self.rate)
        forecast = self.get_forecast(slope, years, intercept)
        diagram = plt.scatter(self.x, self.y)
        plt.plot(years, forecast, color='red')
        plt.title(title)
        plt.xlabel(title_x)
        plt.ylabel(title_y)
        if grid:
            plt.grid()
        plt.legend([])
        # plt.show()
        return diagram


link = 'https://raw.githubusercontent.com/freeCodeCamp/boilerplate-sea-level-predictor/master/epa-sea-level.csv'
df = pd.read_csv(link)
df_noaa_cleaned = df.dropna(subset=['NOAA Adjusted Sea Level'])

x_asix = df_noaa_cleaned['Year']
y_axis = df_noaa_cleaned['CSIRO Adjusted Sea Level']

year_start = df_noaa_cleaned['Year'].min()
year_finish = 2051
year_rate = 1

# initiate class
task_3 = Trend(year_start, year_finish, year_rate, x_asix, y_axis)
title, title_x, title_y = 'Linear Trend of CSIRO Adjusted Sea Level', 'Year', 'CSIRO Adjusted Sea Level'
result = task_3.diagram(title, title_x, title_y, True)
plt.show()
