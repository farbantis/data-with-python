import pandas as pd


def sorted_rank(df):
    df = pd.read_excel(df, sheet_name='Happiness-Data-2015')
    df = df.sort_values(by='Happiness Rank', ascending=False)
    print(df['Happiness Rank'].head(5))
    return df

happiness = 'https://github.com/futureCodersSE/working-with-data/blob/main/Happiness-Data/2015.xlsx?raw=true'
actual = sorted_rank(happiness).index[0]
expected = 157

if actual == expected:
  print("Well done, test passed")
else:
  print("Test failed","Should have got", expected, "got", actual)
