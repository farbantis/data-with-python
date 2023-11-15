import pandas as pd
datatables1 = pd.read_html('https://en.wikipedia.org/wiki/Glasgow#Climate')
df1 = datatables1[7]  #Glasgow population data
print()

url_csv = "https://raw.githubusercontent.com/futureCodersSE/working-with-data/main/Data%20sets/Paisley-Weather-Data.csv"
df2 = pd.read_csv(url_csv)
print(df2)

url_excel = "https://github.com/futureCodersSE/working-with-data/blob/main/Data%20sets/public_use-talent-migration.xlsx?raw=true"
df3 = pd.read_excel(url_excel, sheet_name="Industry Migration")

