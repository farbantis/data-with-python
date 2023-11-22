# import csv
#
# with open("./Data_Sets/housing_in_london_yearly_variables.csv", "r") as f:
#     content = csv.reader(f)
#     for line in content:
#         print(line)

import pandas as pd


data = pd.read_csv("./Data_Sets/housing_in_london_yearly_variables.csv")
print(data.describe())
