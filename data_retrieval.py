import pandas as pd
# datatables = pd.read_html('https://en.wikipedia.org/wiki/Glasgow#Climate')
# df = datatables[7]  #Glasgow population data
# print()


url = "https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/Paisley-Weather-Data.csv"
df = pd.read_csv(url)
print(df)

