import pandas as pd


def get_gdp_health(df):
    df = pd.read_excel(df)
    df = df.sort_values(by=['Economy (GDP per Capita)', 'Health (Life Expectancy)'])
    print(df.head(5))
    return df



happiness = 'https://github.com/futureCodersSE/working-with-data/blob/main/Happiness-Data/2015.xlsx?raw=true'
test = get_gdp_health(happiness)

actual = test['Happiness Score'].iloc[0]
expected = 4.517

if actual == expected:
    print("Well done, test passed")
else:
    print("Test failed", "Should have got", expected, "got", actual)
