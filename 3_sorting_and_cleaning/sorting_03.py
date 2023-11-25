import pandas as pd


def get_descending(df):
    df = pd.read_excel(df)
    df = df.sort_values(by=['Freedom', 'Trust (Government Corruption)'], ascending=False)
    return df[-5:][['Country', 'Region']]


happiness = 'https://github.com/futureCodersSE/working-with-data/blob/main/Happiness-Data/2015.xlsx?raw=true'
actual = get_descending(happiness).index[0]
expected = 136

if actual == expected and (len(get_descending(happiness)) == 5):
    print("Test passed", actual)
else:
    print("Test failed", "Should have got", expected, "got", actual, "and length of series should have been 5 but was",
          len(get_descending(happiness)))
