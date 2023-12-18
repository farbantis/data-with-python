import pandas as pd


url = 'https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/Income-Data.xlsx?raw=true'
df = pd.read_excel(url)
print(df)
