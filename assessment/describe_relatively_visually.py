import pandas as pd


url = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/Income-Data.xlsx?raw=true'
df = pd.read_excel(url)
print(df)

"""
1. 
2. dropna() 
removes blank rows based on indicated column. still keeps the rows where the value is 0 
    the obvious problem in this table is missing data. the solution can be either to
    delete the rows with missing data or to fill them out with average data. Both approaches
    have their pros and cons. If we remove total_vaccinations column the remaining dataset
    would represent 9011/14994*100 = 60% of the original dataset.
"""
