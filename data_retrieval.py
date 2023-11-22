import pandas as pd

data_from_my_github = "https://raw.githubusercontent.com/farbantis/data-with-python/master/Data_Sets/housing_in_london_yearly_variables.csv"
df = pd.read_csv(data_from_my_github)

print(df.iloc[0])

